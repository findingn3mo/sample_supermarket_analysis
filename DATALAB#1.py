# -*- coding: utf-8 -*-
"""
Anthony Giang
DATA Initiative Research Lab


Filename: DATALAB #1

    

Description: Find insight from a big csv file

    


"""
# Import pandas and random for later use
import pandas as pd
import random

# Filename
FILENAME_1 = "table_1.csv"


def read(filename):
    '''
    Input: The file that is going to be read
    Output: The data from that file that was read and formated in using
    pandas
    
    The function read and compute organize the data in the format of pandas 
    since this is a very large data file
    '''
    # Read the data using pandas
    df = pd.read_csv(filename)
    
    
    # Return the function that was read and pandas formated
    return df
def userinput():
    
    name = input("Which department do you want to know more about?\n")
    
    return name
def categories(data):
    '''
    Input The data that has been read and formated by pandas
    Output: A small report of what data has to offer
    The function is going to create a report from the data of the csv file
    the report consists of how many sales, how many users, how products, aisle,
    department there are , etc
    '''
    
    # Create sets for later use
    cusnum = set()
    aisle = set()
    department = set()
    product = set()
    reordered = set()
    addtocart = set()
    
    # Create lists consists of columns corresponding to that of the data file
    a = data['user_id']
    b = data['product_name']
    c = data['aisle']
    d = data['department']
    e = data['order_dow']
    f = data['order_hour_of_day']
    g = data['days_since_prior_order']
    h = data['add_to_cart_order']
    i = data['reordered']
    
    # Add all of the values from the lists above into sets for exclusive
    for k in a:
        cusnum.add(k)
    for k in b:
        product.add(k)
    for k in c:
        aisle.add(k)
    for k in d:
        department.add(k)
    for k in i:
        reordered.add(k)
    for k in h:
        addtocart.add(k)
        
        
    
    # Count how many transaction there are
    transnum = a.count()
    
    # What is the maximum reorder count from users
    maxreordered = max(reordered)
    
    # What is the maximum add to cart to order 
    maxaddtocart = max(addtocart)
    
    # See which day and which hour of the week where people usually order
    day = e.value_counts().idxmax()
    hour = f.value_counts().idxmax()
    
    
    # See what is the usual time where people reorder again
    max_prior_order = g.value_counts().idxmax()
    
    # Create a pandas formated display for products name and user id whom and 
    # what the customer that usally order on the day and hour when people 
    # usually order
    sold_product = data.loc[(e == day) & (f == hour), 'product_name']
    sold_id = data.loc[(e == day) & (f == hour), 'user_id']
    # Create a pandas formated displayed with products that has the maximum 
    # reorder
    mostreordered = data.loc[(i == maxreordered), 'product_name']
    # Create a pandas formated displayed with products and user id that has 
    # the maximum add to cart
    mostaddtocart = data.loc[(h == maxaddtocart), 'product_name']
    mostaddtocartid = data.loc[(h == maxaddtocart), 'user_id']

    
    # Create a small report of insight as how many transaction are ther with 
    # how many user , how aisle, department, products, ...
    print("There are",transnum, "sales within",len(cusnum),"users")
    print("There are", len(department), "department such as", 
          random.choice(tuple(department)))
    print("There are", len(aisle), "aisle such as", 
          random.choice(tuple(aisle)))
    print("There are", len(product), "product such as", 
          random.choice(tuple(product)))
    print("The period of time that past since most user placed their order "
          , max_prior_order)
    print("------------------------------------------------------------------")
    print("The day when people order the most is day", day, 
          "and the hour that people order the most is", hour)
    print("The products that are being purchase these days and hours are:")
    print(sold_product)
    print("\nAnd their user_id are:")
    print(sold_id)  
    print("------------------------------------------------------------------")
    print("The most reordered times from customers is",maxreordered, "times")
    print("The product that has the most reordered are:")
    print(mostreordered)
    print("------------------------------------------------------------------")
    print("The product that has the most add to cart times is",
          maxaddtocart,"times")
    print("The product that has the most add to cart is:")
    print(mostaddtocart.to_string(index = False))
    print("And the buyer id is:")
    print(mostaddtocartid.to_string(index = False))
    print("------------------------------------------------------------------")


def department(name, data):
    '''
    Input: The name of the department which the user would like to know more 
    about, and the data that has been read and formated by pandas
    Output: A small report of what data has to offer
    The function is going to create a report from the data of the csv file
    the report consists of how many sales, how many users, how products, aisle,
    department there are , etc of the department which the user wants to know 
    about
    '''
    
    # Create sets for later uses
    product = set()
    customer = set()
    aisle = set()
    # Create lists consists of columns corresponding to that of the data file
    d = data['department']
    e = data['order_dow']
    f = data['order_hour_of_day']
    
    # See how many sales there are in that department
    numsales = len(data.loc[(d == name)])
    
    # See how many customer there are and who are they 
    departmentid = data.loc[(d == name), 'user_id']
    for k in departmentid:
        customer.add(k)
        
    # See what product does the department have and what are they    
    departmentproduct = data.loc[(d == name), 'product_name']
    for k in departmentproduct:
        product.add(k)
    
    # See how many aisles does the department have and what are they    
    departmentaisle = data.loc[(d == name), 'aisle']
    for k in departmentaisle:
        aisle.add(k)
    
    # See which days that has the most and least product bought
    departmentday = data.loc[(d == name), 'order_dow']
    mostday =  departmentday.value_counts().idxmax()
    leastday = departmentday.value_counts().idxmin()
    
    # See which hours that has the most and least product bought
    departmenthour = data.loc[(d == name), 'order_hour_of_day']
    mosthour = departmenthour.value_counts().idxmax()
    leasthour = departmenthour.value_counts().idxmin()
    
    # See how many sales during the days and hours that has the most and least
    # product bought
    timemostsale = data.loc[(d == name) & (e == mostday) & (f == mosthour)]
    timeleastsale = data.loc[(d == name) & (e == leastday) & (f == leasthour)]
    
    # See how many total reorder does the store have
    departmentreorder = data.loc[(d == name), 'reordered']
    totalreorder = departmentreorder.sum()
    
    # See how many add to cart does the products in this department generate    
    departmentratoc = data.loc[(d == name), 'add_to_cart_order']
    totalatoc = departmentratoc.sum()

    # See many days does the user spent since their last order
    departmentreorder = data.loc[(d == name), 'days_since_prior_order']
    mostreorder = departmentreorder.value_counts().idxmax()
    

    
    # Create the report for that department 
    print("The department of", name, "has total of", len(aisle), 
          "aisle such as", random.choice(tuple(aisle)))
    print("The department of", name, "has total of", len(product), 
          "products such as", random.choice(tuple(product)))
    print("The department of", name,"have", numsales,"sales with", 
          len(customer), "users")
    print("The department sales the most products on day", mostday,
          "and on the", mosthour, "hour with", len(timemostsale), "sales")
    print("The department sales the least products on day", leastday,
          "and on the", leasthour,"hour with", len(timeleastsale), "sales")
    print("The department has a total of",totalreorder, "reorders" )
    print("The total add to cart for this deparment is", totalatoc)
    print("The period of time that past since users placed their",
          "order from this department is",mostreorder, "days")
    
    
    
    
    
    
def main():    
    ''' 
    Input: None
    Output: Excute all of the functions above
    
    The main functions where all of the code are excuted
    '''
    # Read the data from the file using the pandas and get the formated pandas
    # as a return
    data = read(FILENAME_1)
    
     
    # Use the formated pandas from the function above to create a report
    categories(data)
    
    # Get the user input for the department which they want to know more
    # about
    name = userinput()
    
    # Excute the function which create another report for that specific 
    # department which the users want to know about
    department(name, data)


# Run the main function
main()