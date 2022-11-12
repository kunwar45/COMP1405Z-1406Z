def print_sorted_grades(filename):
    fhand = open(filename)
    line = "default"
    studentDetails = ""

    #Takes all of the student details and formats it into "*<fname> <lname> with grade <grade>_"
    while(True):
        if (fName:= (fhand.readline().strip())) == "":
            break
        lName = (fhand.readline().strip())
        studentDetails += "*" + fName + " " + lName + " "
        fhand.readline()
        studentDetails +="with grade " + str( format( ((float(fhand.readline().strip()) * 25) + (float(fhand.readline().strip()) * 30) + (float(fhand.readline().strip()) * 45))/ (100), ".2f" )) + "_"
    studentDetailsSorted = ""
    studentSorted = 0

    #Loops the sorting of the grades using * and _
    while(len(studentDetails)>1):
        maxAverage = 0
        for i in range(len(studentDetails)):
            if studentDetails[i] == '*':
                startName = i
            if studentDetails[i] == '_':
                if float(studentDetails[i-5:i]) > float(maxAverage):
                    maxAverage = studentDetails[i-5:i]
                    studentSorted = studentDetails[startName:i+1]
        studentDetailsSorted += studentSorted
        studentDetails = extract(studentDetails,studentSorted)
    
    #Formats the string into the expected output
    detailsFormatted = ""
    for i in studentDetailsSorted[1:]:
        if i == '*':
            detailsFormatted+='\n'
        elif i == '_':
            pass
        else:
            detailsFormatted+=i
    fhand.close()
    print (detailsFormatted)
    
#removes a substring from the main string (to remove the best grades from the original string)
def extract(string,substring):
    for i in range(len(string)):
        if string[i] == substring[0]:
            start = i
            flag = 0
            for j in range(len(substring)-1):
                if string[start+j] != substring[j]:
                    flag = 1
            if flag == 0:
                string = string[:start] + string[start+len(substring):]
                break
    return string

print_sorted_grades("studentinfo1.txt")