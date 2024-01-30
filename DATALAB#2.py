# -*- coding: utf-8 -*-
"""
Anthony Giang
DATA Initiative Research Lab

Filename:DATALAB#2

    

Description: Find insight from small a csv file. 

    


"""
# Import csv and matplotlib.pyplot for later use
import csv
import matplotlib.pyplot as plt


# File name
FILENAME = "table_2.csv"


def insight():
    '''
    Input: None
    Output: return a name from the user
    Get the user input and return the input for usage
    '''
    
    name = input("Which department do you want to have more insight about?\n")
    
    return name


def read(filename):
    '''
    Input: File that is going to be read
    
    Output: 5 lists consist of:
    
    department : A list of string from the "department" column in 
    the excel file
    order_dow : A list of string from the "order_dow" column in 
    the excel file
    num_order : A list of string from the "num_order" column in 
    the excel file
    num_reorder : A list of string from the "num_reorder" column in 
    the excel file
    per_order : A list of string from the "per_order" column in 
    the excel file.
    
    The function is going to read the data file and return 5 lists consists of 
    5 rows from the excel file.

    '''
    # Create multiple lists for later use
    department = []
    order_dow = []
    num_order = []
    num_reorder = []
    per_order = []
    
    # Open and read the file using a csv reader
    with open(filename) as file:
        data = csv.reader(file, delimiter = ",")
        #skip the header
        next(data)


        # Sort the data into list represent by each column from the file 
        for col in data:
            categories = col[0]
            dow = col[1]
            numord = col[2]
            numreord = col[3]
            perord = col[4]

            
            department.append(categories)
            order_dow.append(dow)
            num_order.append(numord)
            num_reorder.append(numreord)
            per_order.append(perord)
        
        # Return the lists
        return department, order_dow, num_order, num_reorder,per_order
def general(department, num_order, num_reorder):
    '''
    Input:3 lists
    List of Department, List of number of order in each department per day,
    List of number of reorder in each department perday
    
    Return : 2 dicts consist of the department as the keys 
    and the total order/reorder as the values
    
    The function is also going to generate a genral report of which
    department has the most order/reorder per week, and the total number of 
    orders from the total of how many departments there are.


    '''
    # Create lists  and dicts for later use
    dctorder = {}
    dctreorder ={}
    index = []
    change = []
    numcate = []
    genorder = []
    order = []
    deporder = []
    genreorder = []
    reorder = []
    depreorder = []
        
    # Converting the values in num_order to int and append them into a 
    # new list
    for i in num_order:
        i = int(i)
        genorder.append(i)
    
    # Get the index that of each variable in the department
    for i in range(len(department)):
        index.append(i)
    
    # Find the index where the department is changing say like from
    # alcohol to produce what is the index of produce
    for i in index:
        if department[i] != department[i-1]:
            change.append(i)
    change.append(len(department) - 1)

    # Creat a list in list using consist of weekly order within each day for
    # each department so every department would have a list of what the user 
    # order within the period of one week
    for i in change:
        a = genorder[i:i+7]
        order.append(a)
        numcate.append(department[i])

    # Get rid of the last value because I had to do with the changing index. 
    # Because at the end of the list, the value is going to be different, its
    # not accountable in this case
    order.pop()
    numcate.pop()
    
    
    # Find the total amount of order each department get per week
    for i in order:
        a = sum(i)
        deporder.append(a)
    
    # Converting the values in num_reorder to int and append them into a 
    # new list
    for i in num_reorder:
        i = int(i)
        genreorder.append(i)
    
    # Creat a list in list using consist of weekly reorder within each day for
    # each department so every department would have a list of what the user 
    # reorder within the period of one week
    for i in change:
        a = genreorder[i:i+7]
        reorder.append(a)
    
    # Get rid of the last value also
    reorder.pop()
    
    # Find the total amount of reorder each department get per week
    for i in reorder:
        a = sum(i)
        depreorder.append(a)
        
    # Creat two dict which the department's name is the key and their total 
    # order/reorder as their vales
    for i in range(len(order)):
        dctorder[numcate[i]] = sum(order[i])
    
    for i in range(len(reorder)):
        dctreorder[numcate[i]] = sum(reorder[i])


    
    
    # Create the report on number of orders
    print("\nOrder stats:")
    # Find the department with the most order
    for i in deporder:
        if i == max(deporder):
            j = deporder.index(i)
            print("The department with the most sales per week is", 
                  numcate[j], "with", deporder[j],"sales.")  
    
    # Find the total order that the store recieve with their total amount of 
    # department
    print("The store have", sum(genorder),"order per week through", 
          len(numcate), "departments.")
    
    
    # Create the report on number of reorders
    print("\nReorder stats:")
    # Find the department with the most reorders
    for i in depreorder:
        if i == max(depreorder):
            j = depreorder.index(i)
            print("The department with the most reorder per week is", 
                  numcate[j],"with", depreorder[j],"reorders.")  
    
    # Find the total order that the store recieve with their total amount of 
    # department    
    print("The store have", sum(genreorder),"reorders per week through", 
          len(numcate), "departments.")
    
    # Return the 2 dicts created before for later use (Department as key and 
    # total order/reorder as values)
    return dctorder, dctreorder

def ordergraph(dctorder):
    '''
    Input: A dict of department as keys and total number of order per 
    department as values
    
    Output: A horizontal bar graph of total order in every department
    
    The function is going to make a graph of total order per department and 
    save the graph.
    '''
    # Create 2 list of department and total order from the input dict
    department = list(dctorder.keys())
    totalorder = dctorder.values()
    
    # Create the graph of department vs. total order with labels, and save the 
    # picture file
    plt.barh(department, totalorder)
    plt.xlabel("Number of Order")
    plt.ylabel("Department")
    plt.title("Total Order per Department")
    plt.savefig("total_order.png",bbox_inches='tight')
    plt.show()
def reordergraph(dctreorder):
    '''
    Input: A dict of department as keys and total number of reorder per 
    department as values
    
    Output: A horizontal bar graph of total reorder in every department
    
    The function is going to make a graph of total reorder per department and 
    save the graph.
    '''
    # Create 2 list of department and total order from the input dict
    department = list(dctreorder.keys())
    totalorder = dctreorder.values()
    
    # Create the graph of department vs. total order with labels, and save the 
    # picture file
    plt.barh(department, totalorder)
    plt.xlabel("Number of Order")
    plt.ylabel("Department")
    plt.title("Total Reorder per Department")
    plt.savefig("total_reorder.png",bbox_inches='tight')
    plt.show()
    # plt.show()
    

def order(name, department, order_dow, num_order):
    '''
    Input: Name( The user input), Department(The list of department),
    order_dow(The list of days of the week), num_order
    (The list of order per day)

    Output: A general report of the department that the user would like to know 
    about(its orders number per day, total orders per week, and the day with
    the most order.) 
   
    '''
   
    # Create a dict and lists for later usage
    dct = {}
    index = []
    change = []
    genorder = []
    sale = []
    numcate = []
    totalorder = []

    
    
    # Repeat the same progress as before converting the values in list of 
    # order into int
    for i in num_order:
        i = int(i)
        genorder.append(i)
    
    # Get the index of the department list
    for i in range(len(department)):
        index.append(i)
    
    # Geting index when the department is changing 
    for i in index:
        if department[i] != department[i-1]:
            change.append(i)
    change.append(len(department) - 1)

   # Create two lists, one is a list of departments, and a list in a list
   # of every department weekly order     
    for i in change:
        a = genorder[i:i+7]
        sale.append(a)
        numcate.append(department[i])
    

    # Remove the last variable because the index at the end of the list is also
    # consider as a changing index
    sale.pop()
    numcate.pop()

    # Creat a dict with departments as the keys and the list of orders every 
    # day for each department as the value.
    for i in range(len(sale)):
        dct[numcate[i]] = sale[i]
    
    # Get the value of the department the user wants
    orderperweek = dct[name]   
    
    # Create a report of the order of the department that the user wants to 
    # about
    print("\nOrder stats:")
    print("\nThe department of", name,"have:")

    # Create a loop to print out the number of order which the customer ordered
    # from on each day of the week
    for i in orderperweek:
        day = orderperweek.index(i)
        order = orderperweek[day]
        totalorder.append(order)
        print(order, "orders on day", day)
    
    # Create a loop to print out the day with most orders and that number of 
    # orders
    for i in orderperweek:
        if i == max(orderperweek):
            print("\nThe day which has the most orders is day", 
                  orderperweek.index(i), "with", i, "orders")
    # Report the total number of order in that department
    print("The total number of orders per week of the", name,"department is", 
          sum(totalorder),"orders.")
    
    # Return the dct created before for later use
    return dct
        
def reorder(name, department, order_dow, num_reorders):
    
    '''
    Input: Name( The user input), Department(The list of department),
    order_dow(The list of days of the week), num_reorders
    (The list of reorder per day)

    Output: A general report of the department that the user would like to know 
    about(its reorders number per day, total reorders per week, and the day with
    the most reorder.) 
  
    '''
    
   
    # Create a dict and lists for later usage 
    dct = {}
    index = []
    change = []
    genreorder = []
    reorder = []
    numcate = []
    totalreorder = []

   
   
    # Converting the numbers from the num_reorders list into int and append
    # them into a list new list
    for i in num_reorders:
        i = int(i)
        genreorder.append(i)
   
    # Create a list of index from the list of department
    for i in range(len(department)):
        index.append(i)
   
    # Create a list of index when the department is changing
    for i in index:
        if department[i] != department[i-1]:
            change.append(i)
    change.append(len(department) - 1)

    # Create two lists, one is a list of departments, and a list in a list
    # of every department weekly reorder    
    for i in change:
        a = genreorder[i:i+7]
        reorder.append(a)
        numcate.append(department[i])
   

    # Remove the last variable because the index at the end of the list is also
    # consider as a changing index
    reorder.pop()
    numcate.pop()
   

    # Create a dict of departments as the keys, and their list of reorder every
    # day as the value
    for i in range(len(reorder)):
        dct[numcate[i]] = reorder[i]
   
    # Get the list of reorder every day for the department that the user wants
    reorderperweek = dct[name]  
   
    # Create the reorder report for the department that the user wants
    print("\nReorder stats:")
    print("\nThe department of", name,"have:")

    # Create a loop to print out which the number of reorder that department
    # have on each day and on what day.
    for i in reorderperweek:
        day = reorderperweek.index(i)
        order = reorderperweek[day]
        totalreorder.append(order)
        print(order, "orders on day", day)
    # Find out which day that department has the most reorder
    for i in reorderperweek:
        if i == max(reorderperweek):
            print("\nThe day which has the most reorders is day", 
                  reorderperweek.index(i), "with", i, "orders")
    # Find the total reorder made by user on that department
    print("The total number of orders per week of the", name,"department is", 
         sum(totalreorder),"orders.")
    
    # Return the dict above for later use
    return dct
    
    



def moving_average(L, window_size = 10):
    
    '''
    Input: y-values of the graph
    Output: The changing value( the best fit line)
                
    Computing a moving average using a specified window size
    '''
    mavg = []
    
    # Create a loop to get a list of moving average of the y-values
    for i in range(len(L)):
        lower = max(i - window_size // 2,0)
        upper = i + window_size // 2
        window = L[lower:upper]
        smooth = sum(window)/len(window)
        mavg.append(smooth)
    # Return the list of moving average for function use
    return mavg        
    
def plot(name, numorder, numreorder):
    '''
    Input: The name of the department that the user wants to know about,
    The 2 dicts of departments as a key and their orders/reorders everyday per
    week
    
    Output: A line graph consists of 4 lines, the line of orders/reorders per
    day from the user's department, and 2 best fit line for the 2 lines of
    department's orders and reorders 

    Compute a line graph of orders/reorders at the user's department and their 
    best fit line. And also save the graph as the 'department.png'.
    '''
    # Create a list of days for later use
    days = []
    
    # Get the list of values for the user's department
    reorder = numreorder[name]
    order = numorder[name]
    
    # Append the number of days from the index of the graph
    for i in order:
        day = order.index(i)
        days.append(day)
        
    # Use the moving average function to create the value for the best fit
    # line
    ordermavg = moving_average(order, window_size = 4)
    reordermavg = moving_average(reorder, window_size = 4)
    
    # Compute the graph with title, labels, legends, and saving the graph.
    plt.title("{} order/reorder per week".format(name))
    plt.xlabel("Day")
    plt.ylabel("Number of Order/Reorder")
    plt.plot(days, order, color = "red", label = "Number of Order")
    plt.plot(days,reorder, color = "cornflowerblue",
             label = "Number of Reorder")
    plt.plot(days, ordermavg, color = "darkred", 
             label = "Order moving average")
    plt.plot(days, reordermavg, color = "darkblue", 
             label = "Reorder moving average")
    plt.legend(bbox_to_anchor=(1.04,1), loc = "upper left")
    plt.savefig("{}.png".format(name),bbox_inches='tight')
    
        
def main():
    '''
    Input: None
    Output: Excute all of the functions above.
    
    The main function to run all of the function above
    '''
    # Get 5 list from the reading functions
    department, order_dow, num_order, num_reorder,per_order = read(FILENAME)
    
    # Use 3 list fromt the reading functions to compute 2 dicts from the
    # general function
    dctorder, dctreorder = general(department, num_order, num_reorder)
    
    # Graph the 2 bar graph using the 2 dicts from the general function
    ordergraph(dctorder)
    reordergraph(dctreorder)
    
    # Ask the user for the department which they would like to know more
    name = insight()
    
    # Create order, reorder report for that department and return 2 dicts 
    # consists of department as keys and list of order/reorder per week of that
    # department as values
    daydictorder = order(name,department,order_dow, num_order)
    daydictreorder = reorder(name, department, order_dow, num_reorder)
    
    # Excute the function plot to plot the graph using the 2 dicts from order 
    # and reorder function
    plot(name, daydictorder, daydictreorder)
    
# Run the main function
main()
            