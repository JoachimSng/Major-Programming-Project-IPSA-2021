# -*- coding: utf-8 -*-
from lib_common import read_csv_file, write_csv_file, append_csv_file

def gradesManagement() :
    """
    This function performs
    IN :
    OUT :
    """
    def addGrade(*gradeData) :
        """
        This function performs
        IN :
        OUT :
        """
        filename1 = "courses.csv"
        filename2 = "grades.csv" 
        data1 = read_csv_file(filename1)
        data2 = read_csv_file(filename2)
        id_ = len(data2)-1
        row = list(gradeData)
        row.insert(0, id_)
        course = str(gradeData[2])
        for i in range (0, len(data2)):
            if course in data1:
                append_csv_file(row, filename2)
                print("Grade has been added")
                return
            else:
                print("This is not a valid course")
            return
    
    def modifyGrade(*gradeData) :
        """
        This function performs
        IN :
        OUT :
        """
        filename1 = "courses.csv"
        filename2 = "grades.csv" 
        data1 = read_csv_file(filename1)
        data2 = read_csv_file(filename2)
        row = list(gradeData)
        course = str(gradeData[2])
        id_ = int(gradeData[0])
        if course in data1:
            for i in range (1, len(data2)):
                if course == data2[i][3]:
                    if id_ == data2[i][2]:
                        grade = input("Whats the new grade?")
                        row.insert(4, grade)
                        data2[i][0] = row
                        write_csv_file(data2, filename2)
                        print("Grade has been modified")
                        return
                    else:
                        print("This id doesn't have an existing grade in this course,\n please add a grade for this person before modifying it")
                        return
                else:
                    print("There is no student who has a grade in this course")
                    return
        else:
            print("This is not a valid course")
        return

    def deleteGrade(*gradeData) :
        """
        This function performs
        IN :
        OUT :
        """
        filename1 = "courses.csv"
        filename2 = "grades.csv" 
        data1 = read_csv_file(filename1)
        data2 = read_csv_file(filename2)
        defaultRow = list()
        course = str(gradeData[2])
        id_ = int(gradeData[0])
        if course in data1:
            for i in range (1, len(data2)):
                if course == data2[i][3]:
                    if id_ == data2[i][2]:
                        data2[i][0] = defaultRow
                        write_csv_file(data2, filename2)
                        print("Grade has been deleted")
                        return
                    else:
                        print("This id doesn't have an existing grade in this course,\n please add a grade for this person before deleting it, or don't")
                        return
                else:
                    print("There is no student who has a grade in this course")
                    return
        else:
            print("This is not a valid course")
        return
    
    def displayGrades() :
        """
        This method is called to diplay all informations from students grade's file.
        Example : ID, Year, Course, Grade
        IN : no input
        OUT : no output
        """
        ##################################################
        #open and read file contents
        ##################################################
        filename = "grades.csv"
        data = read_csv_file(filename)



        print("***********************************************************************************************************")
        print("*                                          School Management                                               *")
        print("***********************************************************************************************************")
        print("*   Students ID                        *       Course                           *        Grade             *")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<40}  * {:<40}  * {:>3} *" . format(data[i][2], data[i][3], data[i][4]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #
    ##################################################
    while True:
        choice = int(input("Choose from menu ( value in 1-5): \n 1- Add grade \n 2- Modify grade\n 3- Delete grade\n 4- Display grades\n 5- Exit\n\n Response:\n"))

        if choice == 1 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            grade = input("Enter the grade\n->")
            addGrade(year,id_,course,grade)

        if choice == 2 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            grade = input("Enter the grade\n->")
            modifyGrade(id_,year,course,grade)

        if choice == 3 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            deleteGrade(id_,year,course)

        if choice == 4 :
            displayGrades() 


        if choice == 5 :
            return 

