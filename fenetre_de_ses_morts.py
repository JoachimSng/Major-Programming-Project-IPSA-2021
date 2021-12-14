import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd

tkwindow = Tk()
tkwindow.geometry('1300x400')
tkwindow.title('Student Management')
tkwindow.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")
n = ttk.Notebook(tkwindow)

entry_frame = Frame(n)
entry_frame = Frame(tkwindow, width=1300, height=800)
entry_frame.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")


table_frame = Frame(entry_frame).grid(row=0, column=5)
table_frame = Frame(entry_frame, padx=5, pady=5, width=600, height=300)
table_frame.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")

button_frame = Frame(n)
button_frame = Frame(tkwindow, width=200, height=100)
button_frame.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")


table_grade = Frame(n)
table_grade.config(highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3")

n.add(entry_frame, text="STUDENT")
n.add(table_grade, text ='GRADES')
n.pack(expand = 1, fill ="both")



#frame label
log_FrameLabel = Label(entry_frame, fg='black', text="Student", highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=0, column=5)


#first name label and text entry box
log_FnameLabel = Label(entry_frame, fg='black', text="First name").grid(row=2, column=0)
log_Fname = StringVar()
log_FnameEntry = Entry(entry_frame, fg='black', textvariable=log_Fname, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=2, column=5)


#last name label and password entry box
log_LnameLabel = Label(entry_frame, fg='black', text="Last name").grid(row=4, column=0)
log_Lname = StringVar()
log_LnameEntry = Entry(entry_frame, fg='black', textvariable=log_Lname, show='*', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=4, column=5)


#ID label and password entry box
log_IDLabel = Label(entry_frame, fg='black', text="ID").grid(row=6, column=0)
log_ID = StringVar()
log_IDEntry = Entry(entry_frame, fg='black', textvariable=log_ID, show='*', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=6, column=5)


#gender label and password entry box
log_genderLabel = Label(entry_frame, fg='black', text="Gender").grid(row=8, column=0)
log_gender = StringVar()
button1_gender = Radiobutton(entry_frame, text="Male", variable = log_gender, value=1, tristatevalue=0).grid(row = 8, column = 4)
button2_gender = Radiobutton(entry_frame, text="Female", variable = log_gender, value=2, tristatevalue=0).grid(row = 8, column = 5)


#email label and password entry box
log_emailLabel = Label(entry_frame, fg='black', text="Email").grid(row=10, column=0)
log_email = StringVar()
log_emailEntry = Entry(entry_frame, fg='black', textvariable=log_email, show='*', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=10, column=5)


#Add button
AddButton = Button(entry_frame, text="Add New", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=12, column=4)


#Delete button
DelButton = Button(entry_frame, text="Delete", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=12, column=6)


#Update button
ModifyButton = Button(entry_frame, text="Modify", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=13, column=5)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

vsb = ttk.Scrollbar(table, orient="horizontal", command=table.xview)
vsb.pack(side=BOTTOM,fill='x')
table.configure(xscrollcommand=vsb.set)


ID = list((data_stu['ID'].values.tolist()))
Firstname = list((data_stu['FIRST NAME'].values.tolist()))
LastName = list((data_stu['LAST NAME'].values.tolist()))
Sex = list((data_stu['SEX'].values.tolist()))
Email = list((data_stu['EMAIL'].values.tolist()))

    
#School report button
SchoolButton = Button(button_frame, text="School report", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=12, column=4)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#grades

#frame label
log_FrameLabel = Label(table_grade, fg='black', text="Student", highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=0, column=5)


#ID label and text entry box
log_IDLabel = Label(table_grade, fg='black', text="ID").grid(row=2, column=0)
log_ID = StringVar()
log_IDEntry = Entry(table_grade, fg='black', textvariable=log_ID, highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=2, column=5)


#grade label and password entry box
log_GradeLabel = Label(table_grade, fg='black', text="Grade").grid(row=4, column=0)
log_Grade = StringVar()
log_GradeEntry = Entry(table_grade, fg='black', textvariable=log_Grade, show='*', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=4, column=5)




#Add button
AddButton2 = Button(table_grade, text="Add New", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=12, column=4)


#Delete button
DelButton2 = Button(table_grade, text="Delete", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=12, column=6)


#Update button
ModifyButton2 = Button(table_grade, text="Modify", fg='black', highlightthickness=2, highlightbackground = "RoyalBlue3", highlightcolor= "RoyalBlue3").grid(row=13, column=5)

#Grade table

data_gra = pd.read_csv('./data/grades.csv')
data_cou = pd.read_csv('./data/courses.csv')

table = ttk.Treeview(table_grade, columns=('ID', 'YEAR', 'STUDENT', 'COURSE', 'GRADES'))


table.heading('ID', text='ID')
table.heading('YEAR', text='YEAR')
table.heading('STUDENT', text='STUDENT')
table.heading('COURSE', text='COURSE')
table.heading('GRADES', text='GRADES')


table['show']='headings'



    
tkwindow.mainloop()