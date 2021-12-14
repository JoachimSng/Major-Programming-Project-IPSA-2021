#--*-- coding:utf-8 --*--
#-------------------------------------------------------------------------------
# Name:       Projet GP211 Student Data Management
#
# Lastname :
# Firstname :
#
# Class :
# Group :
#
#-------------------------------------------------------------------------------


from lib_students import *

from lib_grades import *



#***************************************************************************
#---------------------------------------------------------------------------
#                                Main program
#---------------------------------------------------------------------------
#***************************************************************************

option_menu = 0


# Run the program
#displayMenu()

while True:
    choice = int(input("Choose from menu ( value in 1-3): \n 1- Students management \n 2- Grades management\n 3- Exit\n\n Response:\n"))
    if choice == 1:
        studentsManagement()

    elif choice == 2:
        gradesManagement()

    elif choice == 3:
        break


print("Thanks for using our program. Bye.")
 






