#Each purchase takes 6 lines, so therefore the total lineCount is 6 times the number of purchases
def get_number_purchases(filename):
    fhand = open(filename)
    lineCount = 0
    for line in fhand:
        lineCount+=1
    return int(lineCount/6)

#Every 6th line has the purchase total, so if the lineCount is divisible by 6, it is the purchase total
def get_total_purchases(filename):
    fhand = open(filename)
    lineCount, totalPurchases = 0,0

    for line in fhand:
        lineCount+=1
        if lineCount%6 == 0:
            totalPurchases+=float(line)
    return totalPurchases

def get_average_purchases(filename):
    return get_total_purchases(filename)/get_number_purchases(filename)

#If the line (with the \n taken away) is equal to the customer's name, customerPurchaseCount increments as that is the customer's purchase
def get_number_customer_purchases(filename, customer):
    fhand = open(filename)
    customerPurchaseCount = 0
    for line in fhand:
        if line[:len(line)-1] == customer:
            customerPurchaseCount+=1
    return customerPurchaseCount

#Check if it's the customer's purchase, and once that happens, make customerLineCount equal to lineCount.
#Once 5 lines have passed from that point, we will be at the purchases line, and add that to totalPurchases
def get_total_customer_purchases(filename, customer):
    fhand = open(filename)
    lineCount, totalPurchases = 0, 0 
    #-6, because if linecount gets to line 5 and customerLineCount hasn't change, lineCount - 5 = 0 which is customerLineCount's default
    customerLineCount = -6 

    for line in fhand:
        lineCount+=1
        if line[:len(line)-1] == customer:
            customerLineCount = lineCount
        if customerLineCount == lineCount-5:
                    totalPurchases+=int(line)
    return totalPurchases

def get_average_customer_purchases(filename, customer):
    if get_number_customer_purchases(filename, customer) == 0: #To avoid divide by zero
        return 0
    return get_total_customer_purchases(filename, customer)/get_number_customer_purchases(filename, customer)

#Every 6 lines, reset lineCount to 0 so that I can go to the next purchase and find all the individual sales
def get_most_popular_product(filename):
    fhand = open(filename)
    desktopsSold, laptopsSold, tabletsSold, toastersSold, lineCount = 0,0,0,0,0
    for line in fhand:
        lineCount+=1
        if lineCount == 2:
            desktopsSold+=float(line)
        elif lineCount == 3:
            laptopsSold+=float(line)
        elif lineCount == 4:
            tabletsSold+=float(line)
        elif lineCount == 5:
            toastersSold+=float(line)
        elif lineCount == 6:
            lineCount = 0
    maxCount = max(desktopsSold,laptopsSold,tabletsSold,toastersSold)
    if desktopsSold == maxCount:
        return "Desktop"
    elif laptopsSold == maxCount:
        return "Laptop"
    elif tabletsSold == maxCount:
        return "Tablet"
    else:
        return "Toaster"