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
        data = read_csv_file(filename)
        id_ = len(data)
        row = list(studentData)
        row.insert(0, id_)
        append_csv_file(row, filename)
        print("Student has been added")
        return
    
    def modifyStudent(*studentData) :
        """
        This function performs
        IN : studentData 
        OUT : Altered CSV file with modified student info for a specific ID
        """
        id_ = int(input("Enter student's id"))
        filename = "students.csv"
        data = read_csv_file(filename)
        row = list(studentData)       #creation of a list
        row.insert(0, id_)
        for i in range (1, len(data)):
            if id_ == int(data[i][0]):
                data[i] = row
                write_csv_file(data, filename) 
                print("Student has succesfully been modified")
                return
            else:
                print("This student id hasn't been attributted ")
                return
        return
    
    def deleteStudent(student) :
        """
        This function performs
        IN : student ID
        OUT : Altered CSV file with deleted line
        """
        id_ = int(student[0])
        filename = "students.csv"
        data = read_csv_file(filename)
        row = [0, 0, 0, 0, 0, 0] #lists()
        for i in range (1, len(data)+1):
            if id_ == int(data[i][0]):
                data[i] = row
                write_csv_file(data, filename)
                print("Student has been deleted")
                return
            else:
                print("This student id hasn't been attributted ")
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
