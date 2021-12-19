import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
from lib_grades import addGrade, modifyGrade, deleteGrade
from lib_students import addStudent, modifyStudent, deleteStudent


tkwindow = Tk()
tkwindow.geometry('1300x400')
tkwindow.title('Student Management')
tkwindow.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
n = ttk.Notebook(tkwindow)


table_frame = Frame(n)
table_frame.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
table_frame.pack(side=LEFT, padx=5, pady=5) 


entry_frame = Frame(table_frame)
entry_frame.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
entry_frame.pack(side=LEFT, padx=5, pady=5)


table_frame2 = Frame(n)
table_frame2.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
table_frame2.pack(side=LEFT, padx=5, pady=5)


entry_frame2 = Frame(table_frame2)
entry_frame2.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
entry_frame2.pack(side=LEFT, padx=5, pady=5)


n.add(table_frame, text="STUDENT")
n.add(table_frame2, text ='GRADES')
n.pack(expand = 1, fill ="both")

#--------------------------------------------------------------------------------------------------------------------------------
#first tab
#--------------------------------------------------------------------------------------------------------------------------------


#frame label
log_FrameLabel = Label(entry_frame, fg='black', text="Student", highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=0, column=5)


#first name label and text entry box
log_FnameLabel = Label(entry_frame, fg='black', text="First name", padx=5, pady=5).grid(row=2, column=0)
log_Fname = StringVar()
log_FnameEntry = Entry(entry_frame, fg='black', textvariable=log_Fname, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=2, column=5)

#last name label entry box
log_LnameLabel = Label(entry_frame, fg='black', text="Last name", padx=5, pady=5).grid(row=4, column=0)
log_Lname = StringVar()
log_LnameEntry = Entry(entry_frame, fg='black', textvariable=log_Lname, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=4, column=5)


#ID label and entry box
log_IDLabel = Label(entry_frame, fg='black', text="ID", padx=5, pady=5).grid(row=6, column=0)
log_ID = StringVar()
log_IDEntry = Entry(entry_frame, fg='black', textvariable=log_ID, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=6, column=5)


#gender label entry box
log_genderLabel = Label(entry_frame, fg='black', text="Gender", padx=5, pady=5).grid(row=8, column=0)
log_gender = StringVar()
button1_gender = Radiobutton(entry_frame, text="Male", variable = log_gender, value="M", tristatevalue=0).grid(row = 8, column = 4)
button2_gender = Radiobutton(entry_frame, text="Female", variable = log_gender, value="F", tristatevalue=0).grid(row = 8, column = 5)


#group label and entry box
log_groupLabel = Label(entry_frame, fg='black', text="Group", padx=5, pady=5).grid(row=9, column=0)
log_group = StringVar()
button1_group = Radiobutton(entry_frame, text="Group 1", variable = log_group, value=1, tristatevalue=0).grid(row = 9, column = 4)
button2_group = Radiobutton(entry_frame, text="Group 2", variable = log_group, value=2, tristatevalue=0).grid(row = 9, column = 5)


#email label and entry box
log_emailLabel = Label(entry_frame, fg='black', text="Email", padx=5, pady=5).grid(row=10, column=0)
log_email = StringVar()
log_emailEntry = Entry(entry_frame, fg='black', textvariable=log_email, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=10, column=5)

#data list student
studentData=[]
studentData.append(log_Fname.get())
studentData.append(log_Lname.get())
studentData.append(log_ID.get())
studentData.append(log_gender.get())
studentData.append(log_group.get())
studentData.append(log_email.get())



#Add button
AddButton = Button(entry_frame, text="Add New", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", padx=5, pady=5, command=addStudent(studentData)).grid(row=12, column=4)


#Delete button
DelButton = Button(entry_frame, text="Delete", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", padx=5, pady=5, command=deleteStudent(studentData)).grid(row=12, column=6)


#Update button
ModifyButton = Button(entry_frame, text="Modify", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", padx=5, pady=5, command=modifyStudent(studentData)).grid(row=13, column=5)


#First table
data_stu = pd.read_csv('./data/students.csv')


table = ttk.Treeview(table_frame, columns=('ID', 'SEX','FIRST NAME', 'LAST NAME', 'EMAIL','GROUP'))


table.heading('ID', text='ID')
table.heading('SEX', text='SEX')
table.heading('FIRST NAME', text='FIRST NAME')
table.heading('LAST NAME', text='LAST NAME')
table.heading('EMAIL', text='EMAIL')
table.heading('GROUP', text='GROUP')


table['show']='headings'
table.pack(padx=10, pady=10)


for i in range(len(data_stu)):
    table.insert('', tk.END, values=list(data_stu.loc[i]))


Scroll = ttk.Scrollbar(table_frame, orient="horizontal", command=table.xview)
Scroll.pack(fill='x')
table.configure(xscrollcommand=Scroll.set)


ID = list((data_stu['ID'].values.tolist()))
Firstname = list((data_stu['FIRST NAME'].values.tolist()))
LastName = list((data_stu['LAST NAME'].values.tolist()))
Sex = list((data_stu['SEX'].values.tolist()))
Email = list((data_stu['EMAIL'].values.tolist()))

    
#School report button
SchoolButton = Button(table_frame, text="School report", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
SchoolButton.pack(padx=5, pady=5)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Tab2
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#grades
data_gra = pd.read_csv('./data/grades.csv')
data_cou = pd.read_csv('./data/courses.csv')


#frame label
log_FrameLabel = Label(entry_frame2, fg='black', text="Grades", highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", padx=5, pady=5).grid(row=0, column=5)


#grade ID label and text entry box
log_gIDLabel = Label(entry_frame2, fg='black',padx=5, pady=5, text="Grade ID").grid(row=2, column=0)
log_gID = StringVar()
log_gIDEntry = Entry(entry_frame2, fg='black', textvariable=log_ID, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=2, column=5)


#student ID label and entry box
log_ID2Label = Label(entry_frame2, fg='black', text="Student ID", padx=5, pady=5).grid(row=5, column=0)
log_ID2 = StringVar()
log_ID2Entry = Entry(entry_frame2, fg='black', textvariable=log_ID2, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=5, column=5)


#grade label and entry box
log_GradeLabel = Label(entry_frame2, fg='black', text="Grade", padx=5, pady=5).grid(row=6, column=0)
log_Grade = StringVar()
log_GradeEntry = Entry(entry_frame2, fg='black', textvariable=log_Grade, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=6, column=5)

#Year Spinbox
l=[]
log_YearLabel = Label(entry_frame2, fg='black', text="Year", padx=5, pady=5).grid(row=1, column=0)
log_Year = StringVar()
f = pd.read_csv('./data/grades.csv')
for i in f['YEAR']:
    if i in l:
        pass
    else:
        l.append(i)
log_Year = Spinbox(entry_frame2, values=l)
log_Year.grid(row=1, column=1)

#Course Spinbox
m=['Mathematique', 'Aeronautique', 'Informatique', 'Anglais', 'Electronique', 'Physique', 'Mechanique', 'Grand Projet', 'Sciences Humaines', 'Sciences Fondamentales']
log_CoursesLabel = Label(entry_frame2, fg='black', text="Course", padx=5, pady=5).grid(row=2, column=0)
log_Courses = StringVar()

log_Courses = Spinbox(entry_frame2, values=m)
log_Courses.grid(row=2, column=1)

#grade data list
gradeData=[]
gradeData.append(log_gID.get())
gradeData.append(log_ID2.get())
gradeData.append(log_gGrade.get())
gradeData.append(log_Year.get())
gradeData.append(log_Courses.get())

#Add button
AddButton2 = Button(entry_frame2, text="Add New", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", command=addGrade(gradeData)).grid(row=12, column=4)


#Delete button
DelButton2 = Button(entry_frame2, text="Delete", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", command=deleteGrade(gradeData)).grid(row=12, column=6)


#Update button
ModifyButton2 = Button(entry_frame2, text="Modify", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3", command=modifyGrade(gradeData)).grid(row=13, column=5)


#Grade table
table2 = ttk.Treeview(table_frame2, columns=('ID', 'YEAR', 'STUDENT', 'COURSE', 'GRADES'))


table2.heading('ID', text=' GRADE ID')
table2.heading('YEAR', text='YEAR')
table2.heading('STUDENT', text='STUDENT')
table2.heading('COURSE', text='COURSE')
table2.heading('GRADES', text='GRADES')


table2['show']='headings'
table2.pack(padx=10, pady=10)


for i in range(len(data_gra)):
    table2.insert('', tk.END, values=list(data_gra.loc[i]))


Scroll2 = ttk.Scrollbar(table_frame2, orient="horizontal", command=table2.xview)
Scroll2.pack(fill='x')
table2.configure(xscrollcommand=Scroll2.set)


ID = list((data_gra['ID'].values.tolist()))
Year = list((data_gra['YEAR'].values.tolist()))
Student_ID = list((data_gra['STUDENT_ID'].values.tolist()))
Course = list((data_gra['COURSE'].values.tolist()))
Grades = list((data_gra['GRADE'].values.tolist()))
    

mainloop()