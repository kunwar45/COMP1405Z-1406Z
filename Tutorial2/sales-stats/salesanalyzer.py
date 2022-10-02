def get_number_purchases(filename):
    
    file = open(filename, "r")
    
    i = 0
    for line in file:
        i += 1

    return i/6

def get_total_purchases(filename):
    file = open(filename, "r")

    counter = 0
    sum = 0

    for line in file:
       counter += 1
       if (counter % 6 == 0):
        sum += int(line)


    return sum

def get_average_purchases(filename):
    # average cost of all purchases       

    return get_total_purchases(filename)/get_number_purchases
    
def get_number_customer_purchases(filename, customer):
    # return number of purchases made by that customer

    file = open(filename, "r")
    num_purchases = 0

    for line in file:
        if (line.strip('\n') == customer):
            num_purchases += 1

    return num_purchases

def get_total_customer_purchases(filename, customer):
    # return total cost of purchases made by that customer

    file = open(filename, "r")
    sum = 0
    
    line = file.readline()

    while line != "":
        if (line.strip('\n') == customer):
            for i in range(5):
                line = file.readline()
            sum += int(line)
        else:
            line = file.readline()


    return sum

def get_average_customer_purchases(filename, customer):
    # return average cost of purchases made by that customer

    file = open(filename, "r")
    sum = 0
    frequency = 0

    line = file.readline()

    while line != "":
        if (line.strip('\n') == customer):
            frequency += 1
            for i in range(5):
                line = file.readline()
            sum += int(line)
        else:
            line = file.readline()

    if (frequency == 0):
        return sum
    else:
        return sum/frequency

def get_most_popular_product(filename):
    # return string of product that sold highest number of units when tie return either

    file = open(filename, "r")
    counter = 1
    desktopSum = 0
    laptopSum = 0
    tabletSum = 0
    toasterSum = 0

    for line in file:
        if (counter == 2):
            desktopSum += int(line)
        elif (counter == 3):
            laptopSum += int(line)
        elif (counter == 4):
            tabletSum += int(line)
        elif (counter == 5):
            toasterSum += int(line)
        elif (counter == 6):
            counter = 0
        
        counter += 1

    if (desktopSum >= laptopSum and desktopSum >= tabletSum and desktopSum >=toasterSum):
        return "Desktop"
    elif (laptopSum >= desktopSum and laptopSum >= tabletSum and laptopSum >= toasterSum):
        return "Laptop"
    elif (tabletSum >= desktopSum and tabletSum >= laptopSum and tabletSum >= toasterSum):
        return "Tablet"
    elif (toasterSum >= desktopSum and toasterSum >= laptopSum and toasterSum >= tabletSum):
        return "Toaster"

    main()