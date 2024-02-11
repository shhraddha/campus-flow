import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import tkinter.font as font
import mysql.connector as sql
from PIL import Image, ImageTk
from tkinter import *
#main window
def mainWindow():
    main_win = tk.Tk(className="welcome window")
    main_win.geometry("1530x790+0+0")

    bgImage = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\Homepage.jpg")
    canvas = Canvas(main_win)
    canvas.create_image(0, 0, image=bgImage, anchor=NW)
    canvas.pack(fill="both", expand=True)
    f = font.Font(size=25, slant='roman', family='elephant', weight="normal")

    btn = tk.Button(main_win, text="admin", width=15, height=2, command=adminLogin)
    btn.place(x=200, y=550)
    btn.config(foreground='black')
    btn1 = tk.Button(main_win, text="student", width=15, height=2,command=studentLogin)
    btn1.place(x=400, y=550)
    btn2 = tk.Button(main_win, text="faculty", width=15, height=2,command=faclogin2)
    btn2.place(x=600, y=550)
    btn3 = tk.Button(main_win, text="guardian", width=15, height=2,command=parentlogin3)
    btn3.place(x=800, y=550)
    main_win.mainloop()
    #admin login window
def adminLogin():


    admin_window = tk.Toplevel()
    admin_window.geometry("1530x790+0+0")

    bgImage1 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas1 = Canvas(admin_window)
    canvas1.create_image(0, 0, image=bgImage1, anchor=NW)
    canvas1.pack(fill="both", expand=True)

    f = font.Font(size=25,slant='roman',family='elephant',weight="normal")
    lab3 = tk.Label(admin_window,text="admin login",bg='black' ,font=f, foreground='white',height=1,width=10 )
    lab3.place(x=700,y=10)



    username_label = tk.Label(admin_window, text="Username:",bg="black")
    username_label.place(x=720,y=100)
    username_entry = tk.Entry(admin_window)
    username_entry.place(x=700,y=130)
#    place(x=700,y=)


    password_label = tk.Label(admin_window, text="Password:")
    password_label.place(x=720,y=160)
    password_entry = tk.Entry(admin_window, show="*")
    password_entry.place(x=700,y=190)


    def login():
        user = username_entry.get()
        passw = password_entry.get()
        print("Username:", user)
        print("Password:", passw)

        # checking empty fields
        if(user=="" or passw==""):
            msg.showerror("Error","All fields are required!")
        else:
            conn = sql.connect(host="localhost", username="root", password="you8tube5",database="collage_mag")
            mycursor = conn.cursor()
            mycursor.execute("select * from admin where username=%s and password=%s",(user,passw))
            gotData = mycursor.fetchone()

            if gotData == None:
                msg.showerror("Error","Invalid Id Or Password")

            else:
                msg.showinfo("Sucess", f"Welcome Dear,{user}")

                main_win = tk.Toplevel()

                main_win.geometry("1530x790+0+0")

                bgImage2 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
                canvas2 = Canvas(main_win)
                canvas2.create_image(0, 0, image=bgImage2, anchor=NW)
                canvas2.pack(fill="both", expand=True)

                lab1 = tk.Label(main_win, text="admin block", bg='grey', foreground='white', height=1, width=24)
                lab1.place(x=700,y=10)

                btn = tk.Button(main_win, text="Add Faculty", width=15, height=2, bg='pink',command=addfaculty)
                btn.place(x=700,y=60)
                btn.config(foreground='black')
                btn1 = tk.Button(main_win, text="student details", width=15, height=2, bg='pink',command=showstudentdetail)
                btn1.place(x=700,y=110)
                btn2 = tk.Button(main_win, text="faculty details", width=15, height=2, bg='pink',command=showteacherdetail)
                btn2.place(x=700,y=170)
                btn4 = tk.Button(main_win, text=" Add faculty's schedule", width=15, height=2, bg='pink',command=addschedule)
                btn4.place(x=700,y=210)
                btn3 = tk.Button(main_win, text="faculty's schedule", width=15, height=2, bg='pink',command=showschedule)
                btn3.place(x=700,y=270)
                regBtn = tk.Button(main_win, text="Create new admin", width=15, height=2, bg='pink', command=regForm)
                regBtn.place(x=700,y=310)

            conn.commit
            main_win.mainloop()



    login2_button = tk.Button(admin_window, text="Login",bg='brown',fg='white', command=login)
    login2_button.place(x=900,y=200)
    login_button = tk.Button(admin_window, text="back", bg='brown', fg='white', command=mainWindow)
    login_button.place(x=700, y=230)
    admin_window.mainloop()

# student login
def studentLogin():
    std_window =tk.Toplevel()
    std_window.geometry("1530x790+0+0")

    bgImage3 = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\WhatsApp Image 2023-12-21 at 23.19.51_e5314bf2.jpg")
    canvas3 = Canvas(std_window)
    canvas3.create_image(0, 0, image=bgImage3, anchor=NW)
    canvas3.pack(fill="both", expand=True)


    f = font.Font(size=25, slant='roman', family='elephant', weight="normal")
    lab4 = tk.Label(std_window, text="student login", bg='black', font=f, foreground='white', height=1, width=10)
    lab4.place(x=700,y=10)
    studentname_label = tk.Label(std_window, text="student name:")
    studentname_label.place(x=700,y=40)
    studentname_entry = tk.Entry(std_window)
    studentname_entry.place(x=700,y=70)

    rollno_label = tk.Label(std_window, text="roll no:")
    rollno_label.place(x=700,y=100)
    rollno_entry = tk.Entry(std_window, )
    rollno_entry.place(x=700,y=130)

    def login1():

        studentname = studentname_entry.get()
        rollno = rollno_entry.get()
        print(" student name:", studentname)
        print("roll no:", rollno)

        # checking empty fields
        if (studentname == "" or rollno == ""):
            msg.showerror("Error", "All fields are required!")
        else:
            conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")

            mycursor = conn.cursor()
            mycursor.execute("select * from student where name=%s and student_id=%s", (studentname, rollno))
            gotData = mycursor.fetchone()

            if gotData == None:
                msg.showerror("Error", "Invalid Id Or Password")

            else:
                msg.showinfo("Sucess", f"Welcome Dear,{studentname}")

                file = open("details.txt","w")
                file.write(rollno)
                file.close()
                main_win = tk.Toplevel()
                main_win.geometry("1530x790+0+0")

                bgImage4 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
                canvas4 = Canvas(main_win)
                canvas4.create_image(0, 0, image=bgImage4, anchor=NW)
                canvas4.pack(fill="both", expand=True)

                myframe = tk.Frame(main_win, highlightbackground='black', highlightthickness=3, width=300, height=300)
                myframe.place(x=700,y=10)

                f = font.Font(size=25, slant='roman', family='elephant', weight="normal")
                lab1 = tk.Label(myframe, text="Student block", bg='grey', font=f, foreground='white', height=1,width=20)
                lab1.place(x=700,y=20)

                btn = tk.Button(myframe, text="My details", width=15, height=2,command=myd)
                btn.place(x=700,y=50)
                btn.config(foreground='black')

                btn2 = tk.Button(myframe, text="feedback", width=15, height=2,command=myf)
                btn2.place(x=700,y=70)
                btn3 = tk.Button(myframe, text="result", width=15, height=2,command=showresulttostudent)
                btn3.place(x=700,y=180)
                main_win.mainloop()




    login_button = tk.Button(std_window, text="Login", command=login1)
    login_button.place(x=700,y=150)
    login_button = tk.Button(std_window, text="back", bg='brown', fg='white', command=mainWindow)
    login_button.place(x=700,y=190)
    std_window.mainloop()


# faculty login
def faclogin2():
    faculty_window = tk.Toplevel()
    faculty_window.geometry("1530x790+0+0")

    bgImage5 = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\WhatsApp Image 2023-12-21 at 23.28.42_caa0469c.jpg")
    canvas5 = Canvas(faculty_window)
    canvas5.create_image(0, 0, image=bgImage5, anchor=NW)
    canvas5.pack(fill="both", expand=True)

    f = font.Font(size=25, slant='roman', family='elephant', weight="normal")
    lab1 = tk.Label(faculty_window, text="Faculty member login", bg='black', font=f, foreground='white', height=1,width=24)
    lab1.place(x=700,y=20)

    name_label = tk.Label(faculty_window, text="teacher name:")
    name_label.place(x=700,y=70)
    name_entry = tk.Entry(faculty_window)
    name_entry.place(x=700,y=130)

    faculty_label = tk.Label(faculty_window, text="faculty_id:")
    faculty_label.place(x=700,y=150)
    faculty_entry = tk.Entry(faculty_window)
    faculty_entry.place(x=700,y=200)

    def login6():
        user = name_entry.get()
        id = faculty_entry.get()
        print("Username:", user)
        print("faculty_id:", id)
    # checking empty fields
        if (user == "" or id == ""):
            msg.showerror("Error", "All fields are required!")
        else:
            conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
            mycursor = conn.cursor()
            mycursor.execute("select * from faculty where name=%s and faculty_id=%s", (user, id))
            gotData = mycursor.fetchone()

            if gotData == None:
                msg.showerror("Error", "Invalid Id Or Password")

            else:
                msg.showinfo("Sucess", f"Welcome Dear,{user}")
                file = open("teacherdetails.txt", "w")
                file.write(id)
                file.close()
                main_win = tk.Tk(className="welcome window")
                main_win.geometry("1530x790+0+0")
                main_win.configure(bg='purple')
                btn = tk.Button(main_win, text="schedule", width=15, height=2, bg='pink',command=mys)
                btn.place(x=700,y=10)
                btn.config(foreground='black')
                btn1 = tk.Button(main_win, text="student record", width=15, height=2, bg='pink',command=showstudentdetail)
                btn1.place(x=700,y=50)
                btn2 = tk.Button(main_win, text="add new student", width=15, height=2, bg='pink',command=addstudent)
                btn2.place(x=700,y=90)
                btn3 = tk.Button(main_win, text="My details", width=15, height=2,bg='pink', command=mytd)
                btn3.place(x=700,y=130)
                btn4 = tk.Button(main_win, text="show results", width=15, height=2, bg='pink',command= showresult)
                btn4.place(x=700,y=170)
                btn5 = tk.Button(main_win, text="add results", width=15, height=2, bg='pink', command=addresult)
                btn5.place(x=700,y=210)
                btn6 = tk.Button(main_win, text="add feedback", width=15, height=2, bg='pink', command=addfeedback)
                btn6.place(x=700,y=250)
                btn7 = tk.Button(main_win, text="show feedback", width=15, height=2, bg='pink',command=showfeedback)
                btn7.place(x=700,y=290)
            conn.commit
            main_win.mainloop()


    login_button = tk.Button(faculty_window, text="Login", command=login6)
    login_button.place(x=700,y=240)
    login_button = tk.Button(faculty_window, text="back", bg='brown', fg='white', command=mainWindow)
    login_button.place(x=700,y=270)
    faculty_window.mainloop()
# parent login
def parentlogin3():
    std_window = tk.Toplevel()
    std_window.geometry("1530x790+0+0")
    bgImage6 = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\WhatsApp Image 2023-12-21 at 23.19.52_8e9627f8.jpg")
    canvas6 = Canvas(std_window)
    canvas6.create_image(0, 0, image=bgImage6, anchor=NW)
    canvas6.pack(fill="both", expand=True)

    f = font.Font(size=25, slant='roman', family='elephant', weight="normal")
    lab4 = tk.Label(std_window, text="student login", bg='black', font=f, foreground='white', height=1, width=10)
    lab4.place(x=700,y=10)
    studentname_label = tk.Label(std_window, text="student name:")
    studentname_label.place(x=700,y=50)
    studentname_entry = tk.Entry(std_window)
    studentname_entry.place(x=700,y=90)

    rollno_label = tk.Label(std_window, text="roll no:")
    rollno_label.pack()
    rollno_entry = tk.Entry(std_window, )
    rollno_entry.place(x=700,y=130)
    def login7():
        studentname = studentname_entry.get()
        rollno = rollno_entry.get()
        print(" student name:", studentname)
        print("roll no:", rollno)

        # checking empty fields
        if (studentname == "" or rollno == ""):
            msg.showerror("Error", "All fields are required!")
        else:
            conn = sql.connect(host="localhost", username="root", password="you8tube5",database="collage_mag")
            mycursor = conn.cursor()
            mycursor.execute("select * from student where name=%s and student_id=%s", (studentname, rollno))
            gotData = mycursor.fetchone()

            if gotData == None:
                msg.showerror("Error", "Invalid Id Or Password")

            else:
                msg.showinfo("Sucess", f"Welcome Dear,{studentname}")
                file = open("gdetails.txt", "w")
                file.write(rollno)
                file.close()
                main_win = tk.Toplevel()
                main_win.geometry("1530x790+0+0")
                bgImage7 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
                canvas7 = Canvas(main_win)
                canvas7.create_image(0, 0, image=bgImage7, anchor=NW)
                canvas7.pack(fill="both", expand=True)

                myframe = tk.Frame(main_win, highlightbackground='black', highlightthickness=3, width=300, height=300)
                myframe.pack()
                f = font.Font(size=25, slant='roman', family='elephant', weight="normal")
                lab1 = tk.Label(myframe, text="Student block", bg='grey', font=f, foreground='white', height=1, width=20)
                lab1.place(x=700,y=10)

                btn = tk.Button(myframe, text="attendance", width=15, height=2,command=mya)
                btn.place(x=700,y=50)
                btn.config(foreground='black')
                btn3 = tk.Button(myframe, text="result", width=15, height=2,command=showresulttoparent)
                btn3.place(x=700,y=90)
                btn3 = tk.Button(myframe, text="student's feedback", width=15, height=2,command=mygf)
                btn3.place(x=700,y=130)
                main_win.mainloop()


    login_button = tk.Button(std_window, text="Login", command=login7)
    login_button.place(x=700,y=170)
    login_button = tk.Button(std_window, text="back", bg='brown', fg='white', command=mainWindow)
    login_button.place(x=700,y=200)
    std_window.mainloop()
# create new account form (admin)
def regForm():
    myframe = tk.Toplevel()
    myframe.geometry("1530x790+0+0")
    bgImage9 = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\WhatsApp Image 2023-12-21 at 23.57.16_cc310e04.jpg")
    canvas9 = Canvas(myframe)
    canvas9.create_image(0, 0, image=bgImage9, anchor=NW)
    canvas9.pack(fill="both", expand=True)


    lbl1 = tk.Label(myframe,text="User Name")
    lbl2 = tk.Label(myframe, text="Password")
    lbl3 = tk.Label(myframe, text="Email")

    ent1 = tk.Entry(myframe)
    ent2 = tk.Entry(myframe)
    ent3 = tk.Entry(myframe)


    def reg():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()

        nm = ent1.get()
        pw = ent2.get()
        em = ent3.get()
        cursor.execute("insert into admin values(%s,%s,%s)", (nm, pw, em))

        conn.commit()
        conn.close()
        msg.showinfo("success", "data inserted succesfully")
        # ent1.delete(0,tk.END)
        # ent2.delete(0,tk.END)
        # ent3.delete(0,tk.END)

    reg6 = tk.Button(myframe, text="Register", command=reg)
    reg6.place(x=700,y=150)

    lbl1.place(x=20, y=20)
    ent1.place(x=120, y=20)

    lbl2.place(x=20, y=50)
    ent2.place(x=120, y=50)

    lbl3.place(x=20, y=80)
    ent3.place(x=120, y=80)

    reg6.place(x=50, y=110)


    myframe.mainloop()
def addstudent():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")


    bgImageb = ImageTk.PhotoImage(file=r"C:\Users\shrey\OneDrive\Documents\New folder\WhatsApp Image 2023-12-21 at 23.57.25_eb594541.jpg")
    canvasb = Canvas(root)
    canvasb.create_image(0, 0, image=bgImageb, anchor=NW)
    canvasb.pack(fill="both", expand=True)

    label = tk.Label(root, text="STUDENT LOGIN", width=50, font=("bold", 20))
    label.place(x=-120, y=20)
    label_0 = tk.Label(root, text="student id no.", width=20, font=("bold", 10))
    label_0.place(x=80, y=80)
    entry_0 = tk.Entry(root)
    entry_0.place(x=240, y=80)

    label_1 = tk.Label(root, text="Full Name", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_9 = tk.Label(root, text="Father Name", width=20, font=("bold", 10))
    label_9.place(x=80, y=130)
    entry_9 = tk.Entry(root)
    entry_9.place(x=240, y=130)

    label_8 = tk.Label(root, text="Mother Name", width=20, font=("bold", 10))
    label_8.place(x=80, y=160)
    entry_8 = tk.Entry(root)
    entry_8.place(x=240, y=160)

    label_2 = tk.Label(root, text="Email", width=20, font=("bold", 10))
    label_2.place(x=68, y=190)

    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=190)

    label_3 = tk.Label(root, text="Gender", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=230)
    label_4 = tk.Label(root, text="Category", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=280)
    label_5 = tk.Label(root, text="course:", width=20, font=("bold", 10))
    label_5.place(x=70, y=320)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=320)
    label_6 = tk.Label(root, text="DOB", width=20, font=("bold", 10))
    label_6.place(x=70, y=350)

    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=350)
    label_7 = tk.Label(root, text="contact_no:", width=20, font=("bold", 10))
    label_7.place(x=70, y=380)

    entry_7 = tk.Entry(root)
    entry_7.place(x=240, y=380)
    label_10 = tk.Label(root, text="attendance", width=20, font=("bold", 10))
    label_10.place(x=70, y=410)

    entry_10 = tk.Entry(root)
    entry_10.place(x=240, y=410)
    label_11 = tk.Label(root, text="fee", width=20, font=("bold", 10))
    label_11.place(x=70, y=440)

    entry_11 = tk.Entry(root)
    entry_11.place(x=240, y=440)
    def submit1():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_0.get()
        nm = entry_1.get()
        fnm = entry_9.get()
        mnm = entry_8.get()
        em = entry_2.get()
        gen = entry_3.get()
        cat = entry_4.get()
        co = entry_5.get()
        do = entry_6.get()
        cn = entry_7.get()
        atd = entry_10.get()
        f = entry_11.get()
        cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (sid,nm,fnm,mnm,em,gen,cat,co,do,cn,atd,f))
        conn.commit()
        conn.close()
        msg.showinfo("success", "data inserted successfully")
    tk.Button(root, text='Submit', width=20, bg='brown', fg='white',command=submit1).place(x=280, y=450)
    root.mainloop()
def addfaculty():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")


    bgImagec = ImageTk.PhotoImage(file=r"C:\Users\DELL\OneDrive\Pictures\Saved Pictures\IMG-20231222-WA0002.jpg")
    canvasc = Canvas(root)
    canvasc.create_image(0, 0, image=bgImagec, anchor=NW)
    canvasc.pack(fill="both", expand=True)

    label_0 = tk.Label(root, text="TEACHER LOGIN", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Faculty_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="Name", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="Email", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="salary", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="course", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)

    label_6 = tk.Label(root, text="contact_no", width=20, font=("bold", 10))
    label_6.place(x=80, y=250)
    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=250)

    label_7 = tk.Label(root, text="DOB", width=20, font=("bold", 10))
    label_7.place(x=70, y=280)

    entry_7 = tk.Entry(root)
    entry_7.place(x=240, y=280)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        fid = entry_1.get()
        nm = entry_2.get()
        em = entry_3.get()
        sal = entry_4.get()
        co = entry_5.get()
        cn = entry_6.get()
        do = entry_7.get()
        cursor.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s)", (fid,nm,em,sal,co,cn,do))
        conn.commit()
        conn.close()
        msg.showinfo("success", "data inserted successfully")
    tk.Button(root, text='Submit', width=20, bg='brown', fg='white',command=submit).place(x=180, y=380)
    root.mainloop()
def showteacherdetail():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from faculty"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Faculty_id')
    entry0 = tk.Entry(frame)

    label1 = tk.Label(frame, text='Name:')
    entry1 = tk.Entry(frame)

    label2 = tk.Label(frame, text='Email')
    entry2 = tk.Entry(frame)
    label3 = tk.Label(frame, text='salary')
    entry3 = tk.Entry(frame)
    label4 = tk.Label(frame, text='course')
    entry4 = tk.Entry(frame)
    label5 = tk.Label(frame, text='contact_no')
    entry5 = tk.Entry(frame)
    label6 = tk.Label(frame, text='DOB')
    entry6 = tk.Entry(frame)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.column(7, anchor='center', width=100)
    trv.heading(1, text='Faculty_id')
    trv.heading(2, text='Name:')
    trv.heading(3, text='Email')
    trv.heading(4, text='salary')
    trv.heading(5, text='course')
    trv.heading(6, text='contact_no')
    trv.heading(7, text='DOB')

    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()
    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)
        entry6.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])
        entry6.insert(0, trv.item(selectedItem)['values'][6])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    label6.grid(row=6, column=0, sticky='e')
    entry6.grid(row=6, column=1)

    window.mainloop()
def showstudentdetail():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from student"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='student_id')
    entry0 = tk.Entry(frame)

    label1 = tk.Label(frame, text='Name:')
    entry1 = tk.Entry(frame)

    label2 = tk.Label(frame, text='father name')
    entry2 = tk.Entry(frame)
    label3 = tk.Label(frame, text='mother name')
    entry3 = tk.Entry(frame)
    label4 = tk.Label(frame, text='email')
    entry4 = tk.Entry(frame)
    label5 = tk.Label(frame, text='gender')
    entry5 = tk.Entry(frame)
    label6 = tk.Label(frame, text='category')
    entry6 = tk.Entry(frame)
    label7 = tk.Label(frame, text='course')
    entry7 = tk.Entry(frame)
    label8 = tk.Label(frame, text='DOB')
    entry8 = tk.Entry(frame)
    label9 = tk.Label(frame, text='contact_no')
    entry9 = tk.Entry(frame)
    label10 = tk.Label(frame, text='attendance')
    entry10 = tk.Entry(frame)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.column(7, anchor='center', width=100)
    trv.column(8, anchor='center', width=100)
    trv.column(9, anchor='center', width=100)
    trv.column(10, anchor='center', width=100)
    trv.column(11, anchor='center', width=100)
    trv.heading(1, text='student_id')
    trv.heading(2, text='Name:')
    trv.heading(3, text='father name')
    trv.heading(4, text='mother name')
    trv.heading(5, text='email')
    trv.heading(6, text='gender')
    trv.heading(7, text='category')
    trv.heading(8, text='course')
    trv.heading(9, text='DOB')
    trv.heading(10, text='contact_no')
    trv.heading(11, text='attendance')
    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)


    displayData()


    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)
        entry6.delete(0, tk.END)
        entry7.delete(0, tk.END)
        entry8.delete(0, tk.END)
        entry9.delete(0, tk.END)
        entry10.delete(0, tk.END)
        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])
        entry6.insert(0, trv.item(selectedItem)['values'][6])
        entry7.insert(0, trv.item(selectedItem)['values'][7])
        entry8.insert(0, trv.item(selectedItem)['values'][8])
        entry9.insert(0, trv.item(selectedItem)['values'][9])
        entry10.insert(0, trv.item(selectedItem)['values'][10])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    label6.grid(row=6, column=0, sticky='e')
    entry6.grid(row=6, column=1)
    label7.grid(row=7, column=0, sticky='e')
    entry7.grid(row=7, column=1)
    label8.grid(row=8, column=0, sticky='e')
    entry8.grid(row=8, column=1)
    label9.grid(row=9, column=0, sticky='e')
    entry9.grid(row=9, column=1)
    label10.grid(row=10, column=0, sticky='e')
    entry10.grid(row=10, column=1)
    window.mainloop()
def myd():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImaged = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasd = Canvas(window)
    canvasd.create_image(0, 0, image=bgImaged, anchor=NW)
    canvasd.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s=[f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from student where student_id=%s",s)
    data = cur.fetchone()
    conn.close()
    v=tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:" ,font="ariel", foreground='black',width=10)
    label1.place(x=5,y=50,width=100,height=25)
    label_1 = tk.Label(window, text= data[0], width=20)
    label_1.place(x=200,y=50,width=100,height=25)
    label2 = tk.Label(window, text="Name:",font="ariel", foreground='black',width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=100, height=25)
    label3 = tk.Label(window, text="Father's name:",font="ariel", foreground='black',width=10)
    label3.place(x=10, y=150, width=150, height=25)
    label_3 = tk.Label(window, text=data[2], width=20)
    label_3.place(x=200, y=150, width=100, height=25)
    label4 = tk.Label(window, text="Mother's name:",font="ariel", foreground='black',width=10)
    label4.place(x=5, y=200, width=150, height=25)
    label_4 = tk.Label(window, text=data[3], width=20)
    label_4.place(x=200, y=200, width=100, height=25)
    label5 = tk.Label(window, text="Email:",font="ariel", foreground='black',width=10)
    label5.place(x=5, y=250, width=100, height=25)
    label_5 = tk.Label(window, text=data[4], width=20)
    label_5.place(x=200, y=250, width=100, height=25)
    label6 = tk.Label(window, text="Gender:",font="ariel", foreground='black',width=10)
    label6.place(x=5, y=300, width=100, height=25)
    label_6 = tk.Label(window, text=data[5], width=20)
    label_6.place(x=200, y=300, width=100, height=25)
    label7 = tk.Label(window, text="Category:",font="ariel", foreground='black',width=10)
    label7.place(x=10, y=350, width=100, height=25)
    label_7 = tk.Label(window, text=data[6], width=20)
    label_7.place(x=200, y=350, width=100, height=25)
    label8 = tk.Label(window, text="Course:",font="ariel", foreground='black',width=10)
    label8.place(x=5, y=400, width=100, height=25)
    label_8 = tk.Label(window, text=data[7], width=20)
    label_8.place(x=200, y=400, width=100, height=25)
    label9 = tk.Label(window, text="DOB:",font="ariel", foreground='black',width=10)
    label9.place(x=5, y=450, width=100, height=25)
    label_9 = tk.Label(window, text=data[8], width=20)
    label_9.place(x=200, y=450, width=100, height=25)
    label10 = tk.Label(window, text="Contact no:",font="ariel", foreground='black',width=10)
    label10.place(x=5, y=500, width=100, height=25)
    label_10 = tk.Label(window, text=data[9], width=20)
    label_10.place(x=200, y=500, width=100, height=25)
    label11 = tk.Label(window, text="Attendance:",font="ariel", foreground='black',width=10)
    label11.place(x=10, y=550, width=130, height=25)
    label_11 = tk.Label(window, text=data[10], width=20)
    label_11.place(x=200, y=550, width=100, height=25)
    v.set(data)
    window.mainloop()
def mytd():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImaged = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasd = Canvas(window)
    canvasd.create_image(0, 0, image=bgImaged, anchor=NW)
    canvasd.pack(fill="both", expand=True)
    file = open("teacherdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s=[f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from faculty where faculty_id=%s",s)
    data = cur.fetchone()
    conn.close()
    v=tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="faculty_id:" ,font="ariel", foreground='black',width=10)
    label1.place(x=5,y=50,width=100,height=25)
    label_1 = tk.Label(window, text= data[0], width=20)
    label_1.place(x=200,y=50,width=100,height=25)
    label2 = tk.Label(window, text="Name:",font="ariel", foreground='black',width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=100, height=25)
    label5 = tk.Label(window, text="Email:",font="ariel", foreground='black',width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=150, height=25)
    label6 = tk.Label(window, text="salary:",font="ariel", foreground='black',width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=100, height=25)
    label7 = tk.Label(window, text="Course:",font="ariel", foreground='black',width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=100, height=25)
    label9 = tk.Label(window, text="contact no::",font="ariel", foreground='black',width=10)
    label9.place(x=5, y=300, width=100, height=25)
    label_9 = tk.Label(window, text=data[5], width=20)
    label_9.place(x=200, y=300, width=100, height=25)
    label10 = tk.Label(window, text="DOB:",font="ariel", foreground='black',width=10)
    label10.place(x=5, y=350, width=100, height=25)
    label_10 = tk.Label(window, text=data[6], width=20)
    label_10.place(x=200, y=350, width=100, height=25)
    v.set(data)
    window.mainloop()
def addschedule():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagef = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasf = Canvas(root)
    canvasf.create_image(0, 0, image=bgImagef, anchor=NW)
    canvasf.pack(fill="both", expand=True)


    label_0 = tk.Label(root, text="add schedule", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Faculty_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="lecture_1", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130,width=350)

    label_3 = tk.Label(root, text="lecture_2", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160,width=350)

    label_4 = tk.Label(root, text="lecture_3", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190,width=350)

    label_5 = tk.Label(root, text="lecture_4", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220,width=350)

    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        fid = entry_1.get()
        l1 = entry_2.get()
        l2 = entry_3.get()
        l3 = entry_4.get()
        l4 = entry_5.get()

        cursor.execute("insert into schedule values(%s,%s,%s,%s,%s)", (fid,l1,l2,l3,l4))
        conn.commit()
        conn.close()
        msg.showinfo("success", "data inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def showschedule():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from schedule"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Faculty_id')
    entry0 = tk.Entry(frame,width=50)

    label1 = tk.Label(frame, text='lecture_1')
    entry1 = tk.Entry(frame,width=50)

    label2 = tk.Label(frame, text='lecture_2')
    entry2 = tk.Entry(frame,width=50)
    label3 = tk.Label(frame, text='lecture_3')
    entry3 = tk.Entry(frame,width=50)
    label4 = tk.Label(frame, text='lecture_4')
    entry4 = tk.Entry(frame,width=50)


    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.heading(1, text='Faculty_id')
    trv.heading(2, text='lecture_1')
    trv.heading(3, text='lecture_2')
    trv.heading(4, text='lecture_3')
    trv.heading(5, text='lecture_4')

    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)


        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)


    window.mainloop()
def mys():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("teacherdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s=[f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from schedule where faculty_id=%s",s)
    data = cur.fetchone()
    conn.close()
    v=tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="faculty_id:" ,font="ariel", foreground='black',width=10)
    label1.place(x=5,y=50,width=100,height=25)
    label_1 = tk.Label(window, text= data[0], width=20)
    label_1.place(x=200,y=50,width=200,height=25)
    label2 = tk.Label(window, text="Lecture 1:",font="ariel", foreground='black',width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="Lecture 2:",font="ariel", foreground='black',width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="Lecture 3:",font="ariel", foreground='black',width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="Lecture 4:",font="ariel", foreground='black',width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    v.set(data)
    window.mainloop()
def showresult():
    main_win =  tk.Toplevel()
    main_win.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(main_win)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    lab1 = tk.Label(main_win, text="result", bg='grey', foreground='white', height=1, width=24)
    lab1.pack(pady=20)

    btn = tk.Button(main_win, text="BCA result", width=15, height=2, bg='pink',command=bca)
    btn.pack(pady=10)
    btn.config(foreground='black')
    btn1 = tk.Button(main_win, text="BBA result", width=15, height=2, bg='pink',command=bba)
    btn1.pack(pady=10)
    btn2 = tk.Button(main_win, text="BA result", width=15, height=2, bg='pink',command=ba)
    btn2.pack(pady=10)
    btn3 = tk.Button(main_win, text="BSc result", width=15, height=2, bg='pink',command=bsc)
    btn3.pack(pady=10)
    btn4 = tk.Button(main_win, text="BCom result", width=15, height=2, bg='pink',command=bcom)
    btn4.pack(pady=10)
    main_win.loop()
def bca():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from bca_result"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Student_id')
    entry0 = tk.Entry(frame, width=50)

    label1 = tk.Label(frame, text='DBMS')
    entry1 = tk.Entry(frame, width=50)

    label2 = tk.Label(frame, text='PYTHON')
    entry2 = tk.Entry(frame, width=50)
    label3 = tk.Label(frame, text='MATH')
    entry3 = tk.Entry(frame, width=50)
    label4 = tk.Label(frame, text='OS')
    entry4 = tk.Entry(frame, width=50)
    label5 = tk.Label(frame, text='HTML')
    entry5 = tk.Entry(frame, width=50)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5,6), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.heading(1, text='Student_id')
    trv.heading(2, text='DBMS')
    trv.heading(3, text='PYTHON')
    trv.heading(4, text='MATH')
    trv.heading(5, text='OS')
    trv.heading(6, text='HTML')
    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    window.mainloop()
def bba():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from bba_result"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Student_id')
    entry0 = tk.Entry(frame, width=50)

    label1 = tk.Label(frame, text='ACCOUNTING')
    entry1 = tk.Entry(frame, width=50)

    label2 = tk.Label(frame, text='STATISTICS')
    entry2 = tk.Entry(frame, width=50)
    label3 = tk.Label(frame, text='COMMERCE')
    entry3 = tk.Entry(frame, width=50)
    label4 = tk.Label(frame, text='FINANCE')
    entry4 = tk.Entry(frame, width=50)
    label5 = tk.Label(frame, text='MANAGEMENT')
    entry5 = tk.Entry(frame, width=50)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5,6), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.heading(1, text='Student_id')
    trv.heading(2, text='ACCOUNTING')
    trv.heading(3, text='STATISTICS')
    trv.heading(4, text='COMMERCE')
    trv.heading(5, text='FINANCE')
    trv.heading(6, text='MANAGEMENT')
    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    window.mainloop()
def bsc():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from bsc_result"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Student_id')
    entry0 = tk.Entry(frame, width=50)

    label1 = tk.Label(frame, text='CHEMISTRY')
    entry1 = tk.Entry(frame, width=50)

    label2 = tk.Label(frame, text='PHYSICS')
    entry2 = tk.Entry(frame, width=50)
    label3 = tk.Label(frame, text='MATH')
    entry3 = tk.Entry(frame, width=50)
    label4 = tk.Label(frame, text='CHEM LAB')
    entry4 = tk.Entry(frame, width=50)
    label5 = tk.Label(frame, text='PHY LAB')
    entry5 = tk.Entry(frame, width=50)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5,6), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.heading(1, text='Student_id')
    trv.heading(2, text='CHEMISTRY')
    trv.heading(3, text='PHYSICS')
    trv.heading(4, text='MATH')
    trv.heading(5, text='CHEM LAB')
    trv.heading(6, text='PY LAB')
    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    window.mainloop()
def ba():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from ba_result"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='Student_id')
    entry0 = tk.Entry(frame, width=50)

    label1 = tk.Label(frame, text='HISTORY')
    entry1 = tk.Entry(frame, width=50)

    label2 = tk.Label(frame, text='ENGLISH')
    entry2 = tk.Entry(frame, width=50)
    label3 = tk.Label(frame, text='GEN HINDI')
    entry3 = tk.Entry(frame, width=50)
    label4 = tk.Label(frame, text='GEOGRAPHY')
    entry4 = tk.Entry(frame, width=50)
    label5 = tk.Label(frame, text='MATH HONS')
    entry5 = tk.Entry(frame, width=50)

    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5,6), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.column(6, anchor='center', width=100)
    trv.heading(1, text='Student_id')
    trv.heading(2, text='HISTORY')
    trv.heading(3, text='ENGLISH')
    trv.heading(4, text='GEN HINDI')
    trv.heading(5, text='GEOGRAPHY')
    trv.heading(6, text='MATH HONS')
    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])
        entry5.insert(0, trv.item(selectedItem)['values'][5])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)
    label5.grid(row=5, column=0, sticky='e')
    entry5.grid(row=5, column=1)
    window.mainloop()
def bcom():
    window = tk.Tk()
    window.geometry('1600x3200')
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from bcom_result"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='student_id')
    entry0 = tk.Entry(frame,width=50)

    label1 = tk.Label(frame, text='COMMERCE')
    entry1 = tk.Entry(frame,width=50)

    label2 = tk.Label(frame, text='OB')
    entry2 = tk.Entry(frame,width=50)
    label3 = tk.Label(frame, text='BUSINESS COMM')
    entry3 = tk.Entry(frame,width=50)
    label4 = tk.Label(frame, text='COST ACC')
    entry4 = tk.Entry(frame,width=50)


    trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5), show='headings')
    trv.column(1, anchor='center', width=100)
    trv.column(2, anchor='center', width=100)
    trv.column(3, anchor='center', width=100)
    trv.column(4, anchor='center', width=100)
    trv.column(5, anchor='center', width=100)
    trv.heading(1, text='STUDENT_ID')
    trv.heading(2, text='COMMERCE')
    trv.heading(3, text='OB')
    trv.heading(4, text='BUSINESS COMM')
    trv.heading(5, text='COST ACC')

    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)


        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])
        entry2.insert(0, trv.item(selectedItem)['values'][2])
        entry3.insert(0, trv.item(selectedItem)['values'][3])
        entry4.insert(0, trv.item(selectedItem)['values'][4])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)

    label2.grid(row=2, column=0, sticky='e')
    entry2.grid(row=2, column=1)
    label3.grid(row=3, column=0, sticky='e')
    entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0, sticky='e')
    entry4.grid(row=4, column=1)

    window.mainloop()
def addresult():
    main_win = tk.Toplevel()
    main_win.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(main_win)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    lab1 = tk.Label(main_win, text="result", bg='grey', foreground='white', height=1, width=24)
    lab1.pack(pady=20)

    btn = tk.Button(main_win, text="BCA result", width=15, height=2, bg='pink', command=addbca)
    btn.pack(pady=10)
    btn.config(foreground='black')
    btn1 = tk.Button(main_win, text="BBA result", width=15, height=2, bg='pink', command=addbba)
    btn1.pack(pady=10)
    btn2 = tk.Button(main_win, text="BA result", width=15, height=2, bg='pink', command=addba)
    btn2.pack(pady=10)
    btn3 = tk.Button(main_win, text="BSc result", width=15, height=2, bg='pink', command=addbsc)
    btn3.pack(pady=10)
    btn4 = tk.Button(main_win, text="BCom result", width=15, height=2, bg='pink', command=addbcom)
    btn4.pack(pady=10)
    main_win.loop()
def addbca():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    root.title("result")

    label_0 = tk.Label(root, text="BCA RESULT", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="DBMS", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="PYTHON", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="MATH", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="OS", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)
    label_6 = tk.Label(root, text="HTML", width=20, font=("bold", 10))
    label_6.place(x=70, y=250)
    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=250)
    login_button = tk.Button(root, text="back", bg='brown', fg='white', command=addresult)
    login_button.place(x=180 ,y=320)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()
        s2 = entry_3.get()
        s3 = entry_4.get()
        s4 = entry_5.get()
        s5 = entry_6.get()

        cursor.execute("insert into bca_result values(%s,%s,%s,%s,%s,%s)", (sid, s1, s2, s3, s4,s5))
        conn.commit()
        conn.close()
        msg.showinfo("success", "result inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def addbba():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    root.title("result")

    label_0 = tk.Label(root, text="BBA RESULT", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="ACCOUNTING", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="STATISTICS", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="COMMERCE", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="FINANCE", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)
    label_6 = tk.Label(root, text="MANAGEMENT", width=20, font=("bold", 10))
    label_6.place(x=70, y=250)
    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=250)
    login_button = tk.Button(root, text="back", bg='brown', fg='white', command=addresult)
    login_button.place(x=180, y=320)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()
        s2 = entry_3.get()
        s3 = entry_4.get()
        s4 = entry_5.get()
        s5 = entry_6.get()

        cursor.execute("insert into bba_result values(%s,%s,%s,%s,%s,%s)", (sid, s1, s2, s3, s4,s5))
        conn.commit()
        conn.close()
        msg.showinfo("success", "result inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def addba():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    root.title("result")

    label_0 = tk.Label(root, text="BA RESULT", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="HISTORY", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="ENGLISH", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="GEN HINDI", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="GEOGRAPHY", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)
    label_6 = tk.Label(root, text="MATH HONS", width=20, font=("bold", 10))
    label_6.place(x=70, y=250)
    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=250)
    login_button = tk.Button(root, text="back", bg='brown', fg='white', command=addresult)
    login_button.place(x=180, y=320)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()
        s2 = entry_3.get()
        s3 = entry_4.get()
        s4 = entry_5.get()
        s5 = entry_6.get()

        cursor.execute("insert into ba_result values(%s,%s,%s,%s,%s,%s)", (sid, s1, s2, s3, s4,s5))
        conn.commit()
        conn.close()
        msg.showinfo("success", "result inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def addbsc():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    label_0 = tk.Label(root, text="BSc RESULT", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="CHEMISTRY", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="PHYSICS", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="MATH", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="CHEM LAB", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)
    label_6 = tk.Label(root, text="PHY LAB", width=20, font=("bold", 10))
    label_6.place(x=70, y=250)
    entry_6 = tk.Entry(root)
    entry_6.place(x=240, y=250)
    login_button = tk.Button(root, text="back", bg='brown', fg='white', command=addresult)
    login_button.place(x=180, y=320)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()
        s2 = entry_3.get()
        s3 = entry_4.get()
        s4 = entry_5.get()
        s5 = entry_6.get()

        cursor.execute("insert into bsc_result values(%s,%s,%s,%s,%s,%s)", (sid, s1, s2, s3, s4,s5))
        conn.commit()
        conn.close()
        msg.showinfo("success", "result inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def addbcom():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    root.title("result")

    label_0 = tk.Label(root, text="BCOM RESULT", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="COMMERCE", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130)

    label_3 = tk.Label(root, text="OB", width=20, font=("bold", 10))
    label_3.place(x=70, y=160)
    entry_3 = tk.Entry(root)
    entry_3.place(x=240, y=160)

    label_4 = tk.Label(root, text="BUSINESS COMM", width=20, font=("bold", 10))
    label_4.place(x=70, y=190)

    entry_4 = tk.Entry(root)
    entry_4.place(x=240, y=190)

    label_5 = tk.Label(root, text="COST ACC", width=20, font=("bold", 10))
    label_5.place(x=70, y=220)
    entry_5 = tk.Entry(root)
    entry_5.place(x=240, y=220)
    login_button = tk.Button(root, text="back", bg='brown', fg='white', command=addresult)
    login_button.place(x=180, y=320)

    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()
        s2 = entry_3.get()
        s3 = entry_4.get()
        s4 = entry_5.get()


        cursor.execute("insert into bcom_result values(%s,%s,%s,%s,%s)", (sid, s1, s2, s3, s4))
        conn.commit()
        conn.close()
        msg.showinfo("success", "result inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=300)
    root.mainloop()
def addfeedback():
    root = tk.Toplevel()
    root.geometry("1530x790+0+0")

    bgImagek = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvask = Canvas(root)
    canvask.create_image(0, 0, image=bgImagek, anchor=NW)
    canvask.pack(fill="both", expand=True)
    root.title("feedback")

    label_0 = tk.Label(root, text="FEEDBACK", width=50, font=("bold", 20))
    label_0.place(x=-120, y=20)

    label_1 = tk.Label(root, text="Student_id", width=20, font=("bold", 10))
    label_1.place(x=80, y=100)
    entry_1 = tk.Entry(root)
    entry_1.place(x=240, y=100)

    label_2 = tk.Label(root, text="FEEDBACK", width=20, font=("bold", 10))
    label_2.place(x=70, y=130)
    entry_2 = tk.Entry(root)
    entry_2.place(x=240, y=130,width=360)
    def submit():
        conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
        cursor = conn.cursor()
        sid = entry_1.get()
        s1 = entry_2.get()

        cursor.execute("insert into feedback values(%s,%s)", (sid, s1))
        conn.commit()
        conn.close()
        msg.showinfo("success", "feedback inserted successfully")

    tk.Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=200)
    root.mainloop()

def showfeedback():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    frame = tk.Frame(window)
    frame_btns = tk.Frame(frame, bg='#3498db')

    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    qry = "select * from feedback"
    cur.execute(qry)
    data = cur.fetchall()
    conn.close()

    label0 = tk.Label(frame, text='student_id')
    entry0 = tk.Entry(frame,width=50)

    label1 = tk.Label(frame, text='FEEDBACK')
    entry1 = tk.Entry(frame,width=50)


    trv = ttk.Treeview(frame, columns=(1, 2), show='headings')
    trv.column(1, anchor='center', width=400)
    trv.column(2, anchor='center', width=400)
    trv.heading(1, text='STUDENT_ID')
    trv.heading(2, text='feedback')

    # create a function to display data in treeview
    def displayData():
        for row in data:
            trv.insert('', 0, values=row)

    displayData()

    # create a function to display the selected row from treeview
    def displaySelectedItem(event):
        # clear entries
        entry0.delete(0, tk.END)
        entry1.delete(0, tk.END)

        selectedItem = trv.selection()

        entry0.insert(0, trv.item(selectedItem)['values'][0])
        entry1.insert(0, trv.item(selectedItem)['values'][1])

    trv.bind("<<TreeviewSelect>>", displaySelectedItem)

    frame.grid(row=0, column=0)

    label0.grid(row=0, column=0, sticky='e')
    entry0.grid(row=0, column=1)

    trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    label1.grid(row=1, column=0, sticky='e')
    entry1.grid(row=1, column=1)
    window.mainloop()
def myf():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from feedback where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", font="ariel", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=100, height=25)
    label2 = tk.Label(window, text="Feedback:", font="ariel", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=400)
    label_2.place(x=200, y=100, width=400, height=25)
    v.set(data)
    window.mainloop()
def mya():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select student_id, attendance from student where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", font="ariel", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=20, height=25)
    label2 = tk.Label(window, text="attendance:", font="ariel", foreground='black', width=20)
    label2.place(x=15, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=20, height=25)
    v.set(data)
    window.mainloop()
def mygf():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from feedback where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", font="ariel", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=100, height=25)
    label2 = tk.Label(window, text="Feedback:", font="ariel", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=400)
    label_2.place(x=200, y=100, width=400, height=25)
    v.set(data)
    window.mainloop()
def showresulttostudent():
    main_win = tk.Toplevel()
    main_win.geometry("1530x790+0+0")
    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(main_win)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    lab1 = tk.Label(main_win, text="result", bg='grey', foreground='white', height=1, width=24)
    lab1.pack(pady=20)

    btn = tk.Button(main_win, text="BCA", width=15, height=2, bg='pink', command=showbca)
    btn.pack(pady=10)
    btn.config(foreground='black')
    btn1 = tk.Button(main_win, text="BBA", width=15, height=2, bg='pink', command=showbba)
    btn1.pack(pady=10)
    btn2 = tk.Button(main_win, text="BA", width=15, height=2, bg='pink',command=showba)
    btn2.pack(pady=10)
    btn3 = tk.Button(main_win, text="BSc", width=15, height=2, bg='pink',command=showbsc)
    btn3.pack(pady=10)
    btn4 = tk.Button(main_win, text="BCom", width=15, height=2, bg='pink',command=showbcom)
    btn4.pack(pady=10)
    main_win.mainloop()
def showbca():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bca_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:",  foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="DBMS:",  foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="PYTHON:",  foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="MATH:",  foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="OS",foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="HTML", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[5], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[6], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttostudent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showbba():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bba_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:",  foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="ACCOUNTING",  foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="STATISTICS:",  foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="COMMERCE", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="FINANCE",  foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="MANAGEMENT", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[5], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS",  foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[6], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttostudent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showba():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from ba_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="HISTORY:", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="ENGLISH:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="GEN HINDI:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="GEOGRAPHY", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="MATH HONS", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[4], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttostudent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showbsc():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bsc_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="CHEMISTRY:",  foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="PHYSICS:",  foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="MATH:",  foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="CHEM LAB", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="PHY LAB", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[4], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttostudent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showbcom():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("details.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bcom_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="COMMERCE:",  foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="ORG BEHAVIOUR:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="BUSINESS COMM:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="COST ACC:", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=300, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=300, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttostudent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showresulttoparent():
    main_win = tk.Toplevel()
    main_win.geometry("1530x790+0+0")
    bgImage12 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas12 = Canvas(main_win)
    canvas12.create_image(0, 0, image=bgImage12, anchor=NW)
    canvas12.pack(fill="both", expand=True)
    lab1 = tk.Label(main_win, text="result", bg='grey', foreground='white', height=1, width=24)
    lab1.pack(pady=20)

    btn = tk.Button(main_win, text="BCA", width=15, height=2, bg='pink', command=showgbca)
    btn.pack(pady=10)
    btn.config(foreground='black')
    btn1 = tk.Button(main_win, text="BBA", width=15, height=2, bg='pink', command=showgbba)
    btn1.pack(pady=10)
    btn2 = tk.Button(main_win, text="BA", width=15, height=2, bg='pink', command=showgba)
    btn2.pack(pady=10)
    btn3 = tk.Button(main_win, text="BSc", width=15, height=2, bg='pink', command=showgbsc)
    btn3.pack(pady=10)
    btn4 = tk.Button(main_win, text="BCom", width=15, height=2, bg='pink', command=showgbcom)
    btn4.pack(pady=10)
    main_win.loop()
def showgbca():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")
    bgImage12 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas12 = Canvas(window)
    canvas12.create_image(0, 0, image=bgImage12, anchor=NW)
    canvas12.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bca_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="DBMS:", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="PYTHON:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="MATH:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="OS", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="HTML", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[5], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[6], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showgbba():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")

    bgImageg = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvasg = Canvas(window)
    canvasg.create_image(0, 0, image=bgImageg, anchor=NW)
    canvasg.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bba_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="ACCOUNTING", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="STATISTICS:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="COMMERCE",foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="FINANCE", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="MANAGEMENT", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[5], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS",  foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[6], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showgba():
    window =tk.Toplevel()
    window.geometry("1530x790+0+0")
    bgImage12 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas12 = Canvas(window)
    canvas12.create_image(0, 0, image=bgImage12 , anchor=NW)
    canvas12.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from ba_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="HISTORY:", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="ENGLISH:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="GEN HINDI:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="GEOGRAPHY", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="MATH HONS", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[4], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showgbsc():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")
    bgImage11 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas11 = Canvas(window)
    canvas11.create_image(0, 0, image=bgImage11, anchor=NW)
    canvas11.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bsc_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="CHEMISTRY:", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="PHYSICS:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="MATH:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="CHEM LAB", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label8 = tk.Label(window, text="PHY LAB", foreground='black', width=10)
    label8.place(x=5, y=300, width=100, height=25)
    label_8 = tk.Label(window, text=data[4], width=20)
    label_8.place(x=200, y=300, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=350, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=350, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    window.mainloop()
def showgbcom():
    window = tk.Toplevel()
    window.geometry("1530x790+0+0")
    bgImage10 = ImageTk.PhotoImage(file=r"C:\Users\shrey\Downloads\Untitled design.jpg")
    canvas10 = Canvas(window)
    canvas10.create_image(0, 0, image=bgImage10, anchor=NW)
    canvas10.pack(fill="both", expand=True)
    file = open("gdetails.txt", "r")
    f = file.read()
    file.close()
    print(f)
    s = [f]
    conn = sql.connect(host="localhost", username="root", password="you8tube5", database="collage_mag")
    cur = conn.cursor()
    cur.execute("select * from bcom_result where student_id=%s", s)
    data = cur.fetchone()
    conn.close()
    v = tk.StringVar()
    print(data)

    label1 = tk.Label(window, text="student_id:", foreground='black', width=10)
    label1.place(x=5, y=50, width=100, height=25)
    label_1 = tk.Label(window, text=data[0], width=20)
    label_1.place(x=200, y=50, width=200, height=25)
    label2 = tk.Label(window, text="COMMERCE:", foreground='black', width=10)
    label2.place(x=5, y=100, width=100, height=25)
    label_2 = tk.Label(window, text=data[1], width=20)
    label_2.place(x=200, y=100, width=250, height=25)
    label5 = tk.Label(window, text="ORG BEHAVIOUR:", foreground='black', width=10)
    label5.place(x=5, y=150, width=100, height=25)
    label_5 = tk.Label(window, text=data[2], width=20)
    label_5.place(x=200, y=150, width=250, height=25)
    label6 = tk.Label(window, text="BUSINESS COMM:", foreground='black', width=10)
    label6.place(x=5, y=200, width=100, height=25)
    label_6 = tk.Label(window, text=data[3], width=20)
    label_6.place(x=200, y=200, width=250, height=25)
    label7 = tk.Label(window, text="COST ACC:", foreground='black', width=10)
    label7.place(x=5, y=250, width=100, height=25)
    label_7 = tk.Label(window, text=data[4], width=20)
    label_7.place(x=200, y=250, width=250, height=25)
    label9 = tk.Label(window, text="STATUS", foreground='black', width=10)
    label9.place(x=5, y=300, width=100, height=25)
    label_9 = tk.Label(window, text=data[4], width=20)
    label_9.place(x=200, y=300, width=250, height=25)
    v.set(data)
    login_button = tk.Button(window, text="back", bg='brown', fg='white', command=showresulttoparent)
    login_button.place(x=200, y=380)
    window.mainloop()

if __name__=="__main__":
 mainWindow()
