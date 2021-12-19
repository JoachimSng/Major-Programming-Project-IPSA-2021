# -*- coding: utf-8 -*-
from lib_common import read_csv_file, write_csv_file, append_csv_file

def studentsManagement() :
    """
    This function performs
    IN : user choice
    OUT : desired function has been perforemed / altered CSV file
    """
    def addStudent(*studentData) :
        """
        This function performs
        IN : studentData information given by user
        OUT : Updated CSV file with new student info
        """
        filename = "students.csv" 
        data = read_csv_file(filename)  # Data becomes an array which we'll modify then rewreite into the csv file
        id_ = len(data)  #we geneerate an Id from the length of our csv file 
        row = list(studentData)   #create a row from the values held by studentData
        row.insert(0, id_) # insert in the first space of the list the generated id
        append_csv_file(row, filename)  # we then make use of the append fucntion from the common library
        print("Student has been added")  #confirmation message for the user
        return
    
    def modifyStudent(*studentData) :
        """
        This function performs
        IN : studentData 
        OUT : Altered CSV file with modified student info for a specific ID
        """
        id_ = int(input("Enter student's id"))  #ask for an Id
        filename = "students.csv"
        data = read_csv_file(filename)  #open the file
        row = list(studentData)       #creation of a list with the entered data
        row.insert(0, id_)              #add the id to the list
        for i in range (1, len(data)):      #making sure we scan the whole csv file
            if id_ == int(data[i][0]):      #checking if the id has been attributed to a student
                data[i] = row   #if it has then we change the line into the row we've built
                write_csv_file(data, filename)  #the write function deletes whats in the csv file and rewrites everything with our desired array
                print("Student has succesfully been modified")  #confirms to the user that we have succesfully changed the student's information
                return
            else:
                print("This student id hasn't been attributted ") #the if condition hasn't been fulfilled so we tell the user that the student has yet to exist in the csv file
                return
        return
    
    def deleteStudent(student) :
        """
        This function performs
        IN : student ID
        OUT : Altered CSV file with deleted line
        """
        id_ = int(student[0])  #extract the id given by the user into a local variable
        filename = "students.csv"
        data = read_csv_file(filename)
        defaultRow = list("")*4 #lists() create a default empty row that will allow us to delete a line of the array
        for i in range (1, len(data)+1):  #making sure we scan the whole array
            if id_ == int(data[i][0]):      #now we check if the id is present in the extracted array from the csv file
                data[i] = defaultRow        #we delete the row where the id has been found
                write_csv_file(data, filename) #rewrite the csv file with our modified array
                print("Student has been deleted") #for the user
                return
            else:
                print("This student id hasn't been attributted ")   #same as before
                return
        return
    
    def displayStudents() :
        """
        This method is called to diplay all informations from student's file.
        Example : ID,SEX,LAST NAME,FIRST NAME,EMAIL,GROUP
        IN : no input
        OUT : no output
        """
        ##################################################
        #open and read file contents
        ##################################################
        filename = "students.csv"
        data = read_csv_file(filename)



        print("****************************************************************************************************************")
        print("*                                            School Management                                                 *")
        print("****************************************************************************************************************")
        print("*   ID   *   Sex    *     Lastname    *        Firstname        *        Email adresse       *        Group    *")
        print("****************************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<8}  * {:<8}  * {:<15}  *  {:<15}  *  {:<30} * {:>3} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #
    ##################################################
    while True:
        choice = int(input("Choose from menu ( value in 1-5): \n 1- Add student \n 2- Modify student\n 3- Delete student\n 4- Display students\n 5- Exit\n\n Reply :\n"))

        if choice == 1 :
            sex = input("Enter student's sex\n->")
            lastname = input("Enter student's last name\n->")
            firstname = input("Enter student's first name\n->")
            email = input("Enter student's email\n->")
            group = input("Enter student's group\n->")
            addStudent(sex,lastname,firstname,email,group)

        if choice == 2 :
            sex = input("Enter student's sex\n->")
            lastname = input("Enter student's last name\n->")
            firstname = input("Enter student's first name\n->")
            email = input("Enter student's email\n->")
            group = input("Enter student's group\n->")
            modifyStudent(sex,lastname,firstname,email,group)

        if choice == 3 :
            id_ = input("Enter student's ID\n->")
            deleteStudent(id_)

        if choice == 4 :
            displayStudents() 


        if choice == 5 :
            return
