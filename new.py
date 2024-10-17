import tkinter as t
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'student_data'
}

# Establishing the connection
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None
def sign_up():
    s = t.Toplevel()
    s.geometry("350x500")
    s.title("Sign up portal") 
    label_1 = t.Label(s, text="Sign up Portal", font=("Impact", 15))
    label_2 = t.Label(s, text="Enter your Username   : ")
    label_3 = t.Label(s, text="Enter your First name  : ")
    label_4 = t.Label(s, text="Enter your Last name   : ")
    label_5 = t.Label(s, text="Enter your Email ID    : ")
    label_6 = t.Label(s, text="Enter your Password    : ")
    label_7 = t.Label(s, text="Sign up as               : ")

    user_id = t.Entry(s)
    f_name = t.Entry(s)
    l_name = t.Entry(s)
    mail_id = t.Entry(s)
    pswd = t.Entry(s)

    label_1.place(x=120, y=10)
    label_2.place(x=10, y=50)
    user_id.place(x=170, y=53)
    label_3.place(x=10, y=90)
    f_name.place(x=170, y=92)
    label_4.place(x=10, y=130)
    l_name.place(x=170, y=132)
    label_5.place(x=10, y=170)
    mail_id.place(x=170, y=172)
    label_6.place(x=10, y=210)
    pswd.place(x=170, y=212)
    label_7.place(x=10, y=250)

    radio = t.StringVar()
    radio.set(None)
    r_btn1 = t.Radiobutton(s, text="Teacher", variable=radio, value="Teacher")
    r_btn2 = t.Radiobutton(s, text="Student", variable=radio, value="Student")
    r_btn1.place(x=170, y=250)
    r_btn2.place(x=260, y=250)

    def student_info_window(uid, email, password, fname, lname):
        # Create a new window for student details
        student_win = t.Toplevel()
        student_win.geometry("350x300")
        student_win.title("Student Information")

        label_batch = t.Label(student_win, text="Enter your Batch:")
        label_branch = t.Label(student_win, text="Enter your Branch:")
        label_prn = t.Label(student_win, text="Enter your PRN:")

        batch_entry = t.Entry(student_win)
        branch_entry = t.Entry(student_win)
        prn_entry = t.Entry(student_win)

        label_batch.pack(pady=10)
        batch_entry.pack(pady=5)
        label_branch.pack(pady=10)
        branch_entry.pack(pady=5)
        label_prn.pack(pady=10)
        prn_entry.pack(pady=5)

        def finish_student_info():   
            batch = batch_entry.get()
            branch = branch_entry.get()
            prn = prn_entry.get()

            # Validate input fields
            if not all([batch, branch, prn]):
                messagebox.showerror("", "Please fill in all fields")
                return

            # Insert into the students table
            try:
                conn = connect_to_db()
                if conn is None:
                    return

                cursor = conn.cursor()
                # Insert the student information
                cursor.execute("INSERT INTO students (username, first_name, last_name, mail_id, batch, branch, prn) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                               (uid, fname, lname, email, batch, branch, prn))
                conn.commit()

                messagebox.showinfo("", "Student information saved successfully!")

                # After successfully saving the student information, now insert into the users table
                try:
                    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (uid, password, "Student"))
                    conn.commit()
                    messagebox.showinfo("", "Sign Up Successful!")
                    student_win.destroy()
                    s.destroy()  # Close the sign-up window after successful sign-up
                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", f"Error adding to users table: {e}")
                    conn.rollback()  # Rollback the transaction if user insertion fails

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                s.destroy()
            finally:
                cursor.close()
                conn.close()

        finish_btn = t.Button(student_win, text="Finish", command=finish_student_info)
        finish_btn.pack(pady=20)

    def done():
        uid = user_id.get()
        email = mail_id.get()
        password = pswd.get()
        fname = f_name.get()
        lname = l_name.get()
        role = radio.get()

        # Validate input fields
        if not all([uid, email, password, fname, lname, role]):
            messagebox.showerror("", "Please fill in all fields")
            s.destroy()
            return

        # Check password length
        if len(password) < 6:
            messagebox.showerror("", "Password must be at least 6 characters")
            s.destroy()
            
            return

        # Check for existing username or email in the database
        conn = connect_to_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", (uid,))
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showerror("", "Username already exists.")
                s.destroy()
                return
              
            cursor.execute("SELECT * FROM students WHERE mail_id = %s", (email,))
            existing_email = cursor.fetchone()
            if existing_email:
                messagebox.showerror("", "Email already exists.")
                s.destroy()
                return
            
            # If role is Student, open the student info window
            if role == "Student":
                student_info_window(uid, email, password, fname, lname)
            else:
                # For Teacher, insert directly into users table
                cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (uid, password, role))
                conn.commit()
                messagebox.showinfo("", "Sign Up Successful!")
                s.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            s.destroy()
            
        finally:
            cursor.close()
            conn.close()

    btn_01 = t.Button(s, text="Sign Up", command=done)
    btn_01.place(x=110, y=330)
    s.mainloop()


    def done():
        uid = user_id.get()
        email = mail_id.get()
        password = pswd.get()
        fname = f_name.get()
        lname = l_name.get()
        role = radio.get()

        if not all([uid, email, password, fname, lname, role]):
            messagebox.showerror("", "Please fill in all fields")
            return

        # Check password length
        if len(password) < 6:
            messagebox.showerror("", "Password must be at least 6 characters")
            return

        conn = connect_to_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()
            # Insert into users table
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (uid, password, role))
            conn.commit()
            
            if role == "Student":
                # Open the student info window
                student_info_window(uid,email,password,fname,lname)
            else:
                messagebox.showinfo("", "Sign Up Successful!")
                s.destroy()
                
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    btn_01 = t.Button(s, text="Sign Up", command=done)
    btn_01.place(x=110, y=330)
    s.mainloop()

        
def show_password():
    if var1.get()==1:
        n4.config(show="")
    if var1.get()==0:
        n4.config(show="*")

def forgot_pass():
    win = t.Toplevel()
    win.title("Forgor Password")
    win_label = t.Label(win,text="Enter Your Email Id : ").grid(row=1,column=1)
    win_entry = t.Entry(win)
    win_entry.grid(row=1,column=2)
    
    
    def get_p():
        get_name = win_entry.get()
        t.messagebox.showinfo("","Password Sent to Email")
                    
    win_button = t.Button(win,text="Get ",command=get_p).grid(row=2,column=2)
    win.mainloop()
    

def login():
    user_name = n3.get()
    password = n4.get()

    if not user_name or not password:
        messagebox.showerror("", "Please fill in both fields")
        return

    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user_name, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("", "Log in Successful")
            # Proceed to the next screen or functionality
        else:
            messagebox.showerror("", "Invalid Username or Password")
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

       
m = t.Tk()
m.geometry("750x250")
m.state("zoomed")
m.resizable(0,0)
m.title("Mark Entry Portal")   


#title image
symbi = Image.open("Logo1.png")
symbi_image = ImageTk.PhotoImage(symbi)
l3 = t.Label(m,image=symbi_image,bg="#D2D2D2")

#frame and placing
f1 = t.Frame(m,width = 400,height=500,bg="#333333")
f2 = t.Frame(m,width = 400,height=500,bg="#444444")
f1.place(x=750,y=200)
f2.place(x=350,y=200)


#frame 1 components
n1=t.Label(f1, text="Username :",font=("Bahnschrift SemiLight",10),bg="#333333",fg="#D2D2D2")
n2=t.Label(f1, text="Password :",font=("Bahnschrift SemiLight",10),bg="#333333",fg="#D2D2D2")
n3=t.Entry(f1, highlightthickness=0, font=("Lucida Sans",10), relief="flat", width=30,bg="#333333",fg="white")
n4=t.Entry(f1, highlightthickness=0, font=("Lucida Sans",10), relief="flat", width=30,bg="#333333",fg="white", show="*")

n6 = t.Button(f1, text="Sign Up", relief="flat",font=("Lucida Sans",10,"underline"),bd=0,bg="#333333",activebackground="#333333",fg="white",cursor="hand2",command=sign_up)

#group icon
gr = Image.open("group.png")
gr_pic = gr.resize((50,50))
gr_img = ImageTk.PhotoImage(gr_pic)
l2 = t.Label(f1,image=gr_img, bg="#333333")

#user icon
u_icon = Image.open("user1.png")
u_img = ImageTk.PhotoImage(u_icon)
u_label = t.Label(f1,image=u_img, bg="#333333")

#key
k_icon = Image.open("key1.png")
k_img = ImageTk.PhotoImage(k_icon)
k_label = t.Label(f1,image=k_img, bg="#333333")

#Login Label
L_l = t.Label(f1, text="LOGIN", font=("Lucida Sans",25),bg="#333333",fg="white")
L_2 = t.Label(f1, text="Don't have an Account ?",font=("Arial",10),bg="#333333",fg="white")

#Login button
login_btn = Image.open("btn12.png")
login_pic= ImageTk.PhotoImage(login_btn)
login_label=t.Label(f1,image=login_pic,bg="#333333")
n5 = t.Button(login_label, text='LOGIN',font=("yu gothic ui",9,"bold"),bd=0,width=25,bg="#3047ff",cursor="hand2", activebackground="#3047ff",fg="white",relief="flat",command=login)
n5.place(x=14,y=8)

#forgot Password
frgt_psswd = t.Button(f1,text="Forgot Password ?",font=("yu gothic ui",9,"underline"),bd=0,bg="#333333",activebackground="#333333",cursor="hand2",fg="white")


#frame 2 image
image  = Image.open("Vector.png")
pic = image.resize((400,400))
img = ImageTk.PhotoImage(pic)
l1 = t.Label(f2, image=img, bg="#444444",fg="white")
l1.pack(pady=48)

#line
line1 = t.Canvas(f1, width=300, height=2.5, bg="black", highlightthickness=0)
line2 = t.Canvas(f1, width=300, height=2.5, bg="black", highlightthickness=0)

#Check 
var1 = t.IntVar()
Check_Box = t.Checkbutton(f1, text="Show Password", variable=var1,onvalue=1,offvalue=0,bg="#333333",bd=0,activebackground="#333333")


#placing Elements in Frame 1
L_l.place(x=150, y = 80)
l2.place(x=175,y=150)
n1.place(x=75,y=250)
n3.place(x=100,y=275)
u_label.place(x=75,y=275)
line1.place(x=75,y=300)
n2.place(x=75, y=300)
n4.place(x=100,y=325)
k_label.place(x=75,y=325)
line2.place(x=75,y=350)
login_label.place(x=100,y=385)
L_2.place(x=100,y=450)
n6.place(x=250,y=450)
l3.pack(side="top")
Check_Box.place(x=75,y=355)
frgt_psswd.place(x=270,y=355)

m.configure(bg="#D2D2D2")
m.mainloop()
# time.sleep(3)