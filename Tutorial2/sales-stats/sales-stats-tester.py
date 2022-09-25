import salesanalyzer

#get_number_purchases
try:
    print("Testing get_number_purchases(filename) function...")
    solution = 5
    print("salesinfo0.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo0.txt")
    print("Your result was " + str(student))
    solution = 181
    print("salesinfo1.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo1.txt")
    print("Your result was " + str(student))
    solution = 137
    print("salesinfo2.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo2.txt")
    print("Your result was " + str(student))
    solution = 191
    print("salesinfo3.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo3.txt")
    print("Your result was " + str(student))
    solution = 73
    print("salesinfo4.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo4.txt")
    print("Your result was " + str(student))
    solution = 209
    print("salesinfo5.txt should be " + str(solution))
    student = salesanalyzer.get_number_purchases("salesinfo5.txt")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_number_purchases(filename) function")
    raise    
print()
print()

#get_total_purchases
try:
    print("Testing get_total_purchases(filename) function...")
    solution = 20735
    print("salesinfo0.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo0.txt")
    print("Your result was " + str(student))
    solution = 1505310
    print("salesinfo1.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo1.txt")
    print("Your result was " + str(student))
    solution = 1032605
    print("salesinfo2.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo2.txt")
    print("Your result was " + str(student))
    solution = 1228090
    print("salesinfo3.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo3.txt")
    print("Your result was " + str(student))
    solution = 390090
    print("salesinfo4.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo4.txt")
    print("Your result was " + str(student))
    solution = 825505
    print("salesinfo5.txt should be ~" + str(solution))
    student = salesanalyzer.get_total_purchases("salesinfo5.txt")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_total_purchases(filename) function")
    raise
print()
print()

#get_total_purchases
try:
    print("Testing get_average_purchases(filename) function...")
    solution = 4147
    print("salesinfo0.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo0.txt")
    print("Your result was " + str(student))
    solution = 8316.63
    print("salesinfo1.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo1.txt")
    print("Your result was " + str(student))
    solution = 7537.26
    print("salesinfo2.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo2.txt")
    print("Your result was " + str(student))
    solution = 6429.79
    print("salesinfo3.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo3.txt")
    print("Your result was " + str(student))
    solution = 5343.70
    print("salesinfo4.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo4.txt")
    print("Your result was " + str(student))
    solution = 3949.78
    print("salesinfo5.txt should be ~" + str(solution))
    student = salesanalyzer.get_average_purchases("salesinfo5.txt")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_average_purchases(filename) function")
    raise
print()
print()

#get_number_customer_purchases
try:
    print("Testing get_number_customer_purchases(filename, customer) function...")
    solution = 2
    print("salesinfo0.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo0.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 1
    print("salesinfo0.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo0.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 0
    print("salesinfo0.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo0.txt", "Dave")
    print("Your result was " + str(student))

    solution = 21
    print("salesinfo1.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo1.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 13
    print("salesinfo1.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo1.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 14
    print("salesinfo1.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo1.txt", "Dave")
    print("Your result was " + str(student))

    solution = 8
    print("salesinfo2.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo2.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 17
    print("salesinfo2.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo2.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 5
    print("salesinfo2.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo2.txt", "Dave")
    print("Your result was " + str(student))

    solution = 15
    print("salesinfo3.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo3.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 11
    print("salesinfo3.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo3.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 22
    print("salesinfo3.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo3.txt", "Dave")
    print("Your result was " + str(student))

    solution = 6
    print("salesinfo4.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo4.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 2
    print("salesinfo4.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo4.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 5
    print("salesinfo4.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo4.txt", "Dave")
    print("Your result was " + str(student))

    solution = 16
    print("salesinfo4.txt and Adrian should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo5.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 22
    print("salesinfo4.txt and Pascal should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo5.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 16
    print("salesinfo4.txt and Dave should be " + str(solution))
    student = salesanalyzer.get_number_customer_purchases("salesinfo5.txt", "Dave")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_number_customer_purchases(filename, customer) function")
    raise
print()
print()

#get_total_customer_purchases
try:
    print("Testing get_total_customer_purchases(filename, customer) function...")
    solution = 4940
    print("salesinfo0.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo0.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 5255
    print("salesinfo0.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo0.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 0
    print("salesinfo0.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo0.txt", "Dave")
    print("Your result was " + str(student))

    solution = 171225
    print("salesinfo1.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo1.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 108950
    print("salesinfo1.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo1.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 112515
    print("salesinfo1.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo1.txt", "Dave")
    print("Your result was " + str(student))

    solution = 59365
    print("salesinfo2.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo2.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 119115
    print("salesinfo2.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo2.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 34135
    print("salesinfo2.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo2.txt", "Dave")
    print("Your result was " + str(student))

    solution = 93705
    print("salesinfo3.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo3.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 72950
    print("salesinfo3.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo3.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 153215
    print("salesinfo3.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo3.txt", "Dave")
    print("Your result was " + str(student))

    solution = 30300
    print("salesinfo4.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo4.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 7935
    print("salesinfo4.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo4.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 22415
    print("salesinfo4.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo4.txt", "Dave")
    print("Your result was " + str(student))

    solution = 57880
    print("salesinfo4.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo5.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 74805
    print("salesinfo4.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo5.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 50155
    print("salesinfo4.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_total_customer_purchases("salesinfo5.txt", "Dave")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_total_customer_purchases(filename, customer) function")
    raise
print()
print()

#get_average_customer_purchases
try:
    print("Testing get_average_customer_purchases(filename, customer) function...")
    solution = 2470
    print("salesinfo0.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo0.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 5255
    print("salesinfo0.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo0.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 0
    print("salesinfo0.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo0.txt", "Dave")
    print("Your result was " + str(student))

    solution = 8153.57
    print("salesinfo1.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo1.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 8380.77
    print("salesinfo1.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo1.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 8036.79
    print("salesinfo1.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo1.txt", "Dave")
    print("Your result was " + str(student))

    solution = 7420.63
    print("salesinfo2.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo2.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 7006.76
    print("salesinfo2.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo2.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 6827
    print("salesinfo2.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo2.txt", "Dave")
    print("Your result was " + str(student))

    solution = 6247
    print("salesinfo3.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo3.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 6631.82
    print("salesinfo3.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo3.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 6964.32
    print("salesinfo3.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo3.txt", "Dave")
    print("Your result was " + str(student))

    solution = 5050
    print("salesinfo4.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo4.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 3967.50
    print("salesinfo4.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo4.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 4483
    print("salesinfo4.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo4.txt", "Dave")
    print("Your result was " + str(student))

    solution = 3617.5
    print("salesinfo4.txt and Adrian should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo5.txt", "Adrian")
    print("Your result was " + str(student))
    solution = 3400.23
    print("salesinfo4.txt and Pascal should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo5.txt", "Pascal")
    print("Your result was " + str(student))
    solution = 3134.69
    print("salesinfo4.txt and Dave should be ~" + str(solution))
    student = salesanalyzer.get_average_customer_purchases("salesinfo5.txt", "Dave")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_average_customer_purchases(filename, customer) function")
    raise
print()
print()


#get_most_popular_product
try:
    print("Testing get_most_popular_product(filename) function...")
    solution = "Desktop"
    print("salesinfo0.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo0.txt")
    print("Your result was " + str(student))
    solution = "Laptop"
    print("salesinfo1.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo1.txt")
    print("Your result was " + str(student))
    solution = "Laptop"
    print("salesinfo2.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo2.txt")
    print("Your result was " + str(student))
    solution = "Tablet"
    print("salesinfo3.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo3.txt")
    print("Your result was " + str(student))
    solution = "Tablet"
    print("salesinfo4.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo4.txt")
    print("Your result was " + str(student))
    solution = "Tablet"
    print("salesinfo5.txt should be " + str(solution))
    student = salesanalyzer.get_most_popular_product("salesinfo5.txt")
    print("Your result was " + str(student))
except:
    print("There was a problem with your get_most_popular_product(filename) function")
    raise    
print()
print()
