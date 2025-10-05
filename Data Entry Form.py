from tkinter import *
from tkinter import ttk
from tkinter import messagebox
ain=Tk()

def show():
    name=entry1.get().strip()
    last=entry2.get().strip()
    title=combox1.get().strip()
    age_str=spine1.get().strip()
    national=combox2.get().strip()
    registeration=var1.get()
    course_str=spine2.get().strip()
    semester_str=spine3.get().strip()
    term=var2.get()
    # print(f"First Name: {title} {name} {lastname}")           # print in Terminal
    # print(f"Age: {age}")
    # print(f"Nationality: {national}")
    # print(f"Registration Status: {registeration}")
    # print(f"Completed Courses: {course}")
    # print(f"Semester: {semester}")
    # print(f"Term & Conditions: {term}")
  
    if name=="" and last=="" and title=="" and age_str=="" and national=="" and course_str=="" and semester_str=="" :   #  All entry box empty 
        messagebox.showerror("Error", "Please Fill All the details ")
        return
   
    if name==""  :                                                             #only First Name Entry box Empty
        messagebox.showerror("Error", "Please Fill Your First Name ")
        return
  
    if  last=="" :                                                             #only Last Name Entry box Empty
        messagebox.showerror("Error", "Please Fill Your Last Name ")
        return
  
    if  title=="":                                                             #only Title box Empty
        messagebox.showerror("Error", "Please Choise Your Title ")
        return
  
    if  national=="" :                                                         #only National box Empty
        messagebox.showerror("Error", "Please Choise Your Nationallity ")
        return
    if  age_str==""  :                                                         #only age box Empty
        messagebox.showerror("Error", "Please Fill Your Age ")
        return
    if  course_str==""  :                                                      #only course box Empty
        messagebox.showerror("Error", "Please Fill Your Course  ")
        return
    if  semester_str=="" :                                                     #only Semster box Empty
        messagebox.showerror("Error", "Please Fill Your Semester ")
        return
   
    try:                                      # Valid Input Only for integer
        age=int(age_str)
        course=int(course_str)
        semester=int(semester_str)
    except ValueError:
        messagebox.showerror("Error","Age, Course, Semester Must be number")

    if  age<=16  :                                                             #valid input Age or integer value
        messagebox.showerror("Error", "Please Fill Your Valid Age")
        return
  
    if  course<0:                                                              #valid input integer
        messagebox.showerror("Error", "Please Fill Your Valid Course Time Period")
        return
    if  semester<0 :                                                           #valid input integer
        messagebox.showerror("Error", "Please Fill Your Valid Semester Time Period")
        return
    
    if registeration==0 and term==0:           #multiple empty                                # Checkbox==0 means "No tick" ,checkbox==1 means "Tick"
        messagebox.showerror("Error","Please Tick the Registration Box and Term & Conditions box")
        return
    if registeration ==0:                      #single empty
        messagebox.showerror("Error","Please Tick the Registration Box")
        return
    if term ==0:
        messagebox.showerror("Error","Please Tick the Term & Condition Box")
        return

    messagebox.showinfo("Success","Your Registration is Successfully Completed")

    
    with open(r"D:\Github\My project\metplot\Tkinter.py\uer1","a") as f:         #Save File in txt format
        f.write(f"Name: {title} {name} {last}"+"\n")
        f.write(f"Age: {age}"+"\n")
        f.write(f"Nationality: {national}"+"\n")
        f.write(f"Completed Courses: {course}"+"\n")
        f.write(f"Semester: {semester}"+"\n")
        

    ain.destroy()           #After complete Registration Atomatically close the window

ain.title("Data Entry Form")
ain.geometry("510x370")
ain.config(bg="lightblue")
ain.resizable(False,False)
# Label Frame (main Frame)
label_frame1=LabelFrame(ain,text="User Information",labelanchor=NW)
label_frame1.place(x=10,y=10,height=150,width=480)

#label1(first name)
label1=Label(ain,text="First Name")
label1.place(x=43,y=30)
entry1=Entry(ain)              #Entry of the First Name
entry1.place(x=20,y=55,width=120)

#label2(Last name)
label2=Label(ain,text="Last Name")
label2.place(x=225,y=30)
entry2=Entry(ain)             #Entry of the Last Name
entry2.place(x=190,y=55)

#label3(Title)
label3=Label(ain,text="Title")
label3.place(x=390,y=30)
lis1=["Mr.","Mrs.","None"]
combox1=ttk.Combobox(ain,value=lis1)            #Title
combox1.place(x=330,y=55)

#label4(age)
label4=Label(ain,text="Age")
label4.place(x=59,y=80)
spine1=Spinbox(ain,from_=1,to=100,wrap=True)            #Age
spine1.place(x=20,y=110)

#label5(Nationality)
label5=Label(ain,text="Nationality")
label5.place(x=240,y=80)
lis2=["Indian","USA","United kingdom","Russia","China","Japan","Other"]
combox2=ttk.Combobox(ain,value=lis2)           #Nationality
combox2.place(x=200,y=110)

#frame2
label_frame2=LabelFrame(ain)
label_frame2.place(x=10,y=180,height=80,width=480)
label6=Label(ain,text="Registration Status")
label6.place(x=40,y=190)
var1=IntVar()
checkbox1=Checkbutton(ain,text="Currently Registered",variable=var1)#,onvalue="Registretion Status: Completed",offvalue="Registretion Status: Not Completed")
checkbox1.place(x=20,y=220)

#Completed courses
label7=Label(ain,text="# Completed Courses")
label7.place(x=200,y=190)
spine2=Spinbox(ain,from_=1,to=20,wrap=True)            #course
spine2.place(x=190,y=225)

#semester
label8=Label(ain,text="# Semester")
label8.place(x=370,y=190)
spine3=Spinbox(ain,from_=1,to=8,wrap=True)            #semester
spine3.place(x=340,y=225)

#FrameLabel 3
label_frame3=LabelFrame(ain,text="User Information",labelanchor=NW)
label_frame3.place(x=10,y=280,height=50,width=480)
var2=IntVar()
checkbox2=Checkbutton(ain,text="I accept the term and conditions.",variable=var2)#onvalue="Term & Conditons: Accepted",offvalue="Term & condition: Not Accepted")
checkbox2.place(x=15,y=296)

#button(Enter Data)
button=Button(ain,text="Enter Data",command=show)
button.place(x=10,y=340,width=480)

ain.mainloop()