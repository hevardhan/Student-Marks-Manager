
import tkinter as t
from tkinter import END
import pandas as pd
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog as fd
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


firebaseConfig = {
  "apiKey": "AIzaSyD0Nct_JKDGGk-Q2WTxjchNZkiYnJ514NQ",
  "authDomain": "sis-database-f90db.firebaseapp.com",
  "databaseURL": "https://sis-database-f90db-default-rtdb.firebaseio.com",
  "projectId": "sis-database-f90db",
  "storageBucket": "sis-database-f90db.appspot.com",
  "messagingSenderId": "221559006372",
  "appId": "1:221559006372:web:81f674f34f743b72843231",
}

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
authent = firebase.auth()

db = firebase.database()

data={}



     
#------------------------------------------------------------------#
class Main:
    def __init__(self,username):
        self.username=username
    def student(self):
        t.messagebox.showerror("","You are a student !")
    #FUNCTIONS
    def view(self):
        usnm = self.username
        win = t.Tk()
        win.title("Data Manager")
        win.state("zoomed")
        win.resizable(0,0)
        
        #title :
        top_frame = t.Frame(win,bg="#a2d5c6",width=1280,height=150)
        
        #Image
        symbi_image = Image.open("icon.png")
        symbi_img=symbi_image.resize((800,120))
        symbi_pic = ImageTk.PhotoImage(symbi_img)
        symbi_img_label=t.Label(top_frame,image=symbi_pic,bg="#a2d5c6")
        symbi_img_label.image = symbi_pic
        info = db.child("User-Data Base").child("Students").child(usnm).get()
        info_dict = info.val()
        fname_info = info_dict['First Name']
        lname_info = info_dict['Last Name']
        mail_info = info_dict['Mail id']
        batch_info = info_dict['Batch']
        branch_info = info_dict['Branch']
        prn_info = info_dict['PRN']
        #Profile
        def show_profile():
            msg_prof = f"User id : {usnm}\nFirst Name : {fname_info}\nLast Name : {lname_info}\nMail id : {mail_info}\nBatch : {batch_info}\nBranch : {branch_info}\nP.R.N : {prn_info}"
            t.messagebox.showinfo("",msg_prof) 
        prof_btn = t.Button(top_frame,text="View Profile",command=show_profile)
        log_out_btn = t.Button(top_frame,text="Log Out",command=win.destroy)
        

        #Main Frame:
        main_frame = t.PanedWindow(win,width=700,height=500,bg="#332b3a")
        title_main = t.Label(main_frame,text="Student Data Manager",font=("Poppins Light",22),bg="#332b3a",fg="white")
        mid_frame = t.PanedWindow(main_frame,width=650,height=400,bg="#83b1cf")
        chose_sub_label = t.Label(mid_frame,text="Choose the Subject : ",font=("Century Gothic",15),bg="#83b1cf")
        rand_val = db.child("student_database").child(batch_info).child(branch_info).child(prn_info).get()
        dictionary_1 = rand_val.val()
        dictionary_1.pop("Data")
        options = list(dictionary_1.keys())
        clicked = t.StringVar()
        clicked.set("Select")
        chose_sub_drop   = t.OptionMenu(mid_frame,clicked,*options)       
        
        
        def display_marks():
            sub = clicked.get()
            xyz = db.child("student_database").child(batch_info).child(branch_info).child(prn_info).get()
            xyz_dic = xyz.val()
            diction_1 = xyz_dic[sub]
            
            cmp_1 = diction_1["Comp 1"]
            cmp_2 = diction_1['Comp 2']
            cmp_3 = diction_1['Comp 3']
            tot   = diction_1['Total']
            
            cmp1_label = t.Label(mid_frame,text="Component 1 : ",font=("Century Gothic",15),bg="#83b1cf")
            cmp2_label = t.Label(mid_frame,text="Component 2 : ",font=("Century Gothic",15),bg="#83b1cf")
            cmp3_label = t.Label(mid_frame,text="Component 3 : ",font=("Century Gothic",15),bg="#83b1cf")
            tot_label  = t.Label(mid_frame,text="Total Marks : ",font=("Century Gothic",15),bg="#83b1cf")
                
            cmp1_show = t.Label(mid_frame,text=cmp_1,font=("Century Gothic",15),bg="#83b1cf",width=10)
            cmp2_show = t.Label(mid_frame,text=cmp_2,font=("Century Gothic",15),bg="#83b1cf",width=10)
            cmp3_show = t.Label(mid_frame,text=cmp_3,font=("Century Gothic",15),bg="#83b1cf",width=10)
            tot_show  = t.Label(mid_frame,text=tot,font=("Century Gothic",15),bg="#83b1cf",width=10)

            
            cmp1_label.place(x=10,y=80)  
            cmp2_label.place(x=10,y=140)
            cmp3_label.place(x=10,y=200)
            tot_label.place(x=10,y=260)
            
            cmp1_show.place(x=200,y=80)
            cmp2_show.place(x=200,y=140)
            cmp3_show.place(x=200,y=200)
            tot_show.place(x=200,y=260)
            
        get_btn = t.Button(mid_frame,text="Get Marks",font=("Ebrima",12),command=display_marks)    
        
        #BG Image
        bg_image = Image.open("new.png")
        bg_img=bg_image.resize((400,400))
        bg_pic = ImageTk.PhotoImage(bg_img)
        bg_img_label=t.Label(win,image=bg_pic)
        bg_img_label.image = bg_pic


        #Placing

        #--top_frame:
        
        prof_btn.place(x=1190,y=10)
        log_out_btn.place(x=1190,y=50)
        symbi_img_label.place(x=10,y=10)
        
        #--main_frame:
        title_main.place(x=180,y=10)
       
        chose_sub_label.place(x=10,y=20)
        chose_sub_drop.place(x=250,y=20)
        get_btn.place(x=10,y=350)

      
        
        
        #--frames and Canvas
        top_frame.place(x=0,y=0)
        main_frame.place(x=20,y=175)
        mid_frame.place(x=20,y=80)
        bg_img_label.place(x=800,y=225)
        win.mainloop()
    def ops(self):
        win = t.Tk()
        usnm = self.username
        win.title("Data Manager")
        win.state("zoomed")
        win.resizable(0,0)
        
        #title :
        top_frame = t.Frame(win,bg="#a2d5c6",width=1280,height=150)
        
        #Image
        symbi_image = Image.open("icon.png")
        symbi_img=symbi_image.resize((800,120))
        symbi_pic = ImageTk.PhotoImage(symbi_img)
        symbi_img_label=t.Label(top_frame,image=symbi_pic,bg="#a2d5c6")
        symbi_img_label.image = symbi_pic
        
        info = db.child("User-Data Base").child("Teachers").child(usnm).get()
        info_dict = info.val()
        fname_info = info_dict['First Name']
        lname_info = info_dict['Last Name']
        mail_info = info_dict['Mail id']
        sub_info = info_dict['Subject']
        #Profile
        def show_profile():
            msg_prof = f"User id : {usnm}\nFirst Name : {fname_info}\nLast Name : {lname_info}\nMail id : {mail_info}"
            t.messagebox.showinfo("",msg_prof)
        prof_btn = t.Button(top_frame,text="View Profile",command=show_profile)
        log_out_btn = t.Button(top_frame,text="Log Out",command=win.destroy)
        
        #Panned Window for entry
        entry_canvas = t.PanedWindow(win, width=700,heigh=530,bg="#077b8a")
        #DB Info
        from_db = db.child("student_database").get()
        batch_dict = from_db.val()
        batch_options = batch_dict.keys()
        
        #Widgets on Entry window:
        title_label = t.Label(entry_canvas,text="ADD / EDIT DATA :",font=("Poppins Light",20),bg="#077b8a",fg="white")
        chose_label = t.Frame(entry_canvas, width = 640, height=400,bg="#e0fbfc")
        dropdown_label = t.Label(chose_label,text="Choose the Class :",font=("Century Gothic",15),bg="#e0fbfc")
        drop2_label    = t.Label(chose_label,text="Choose the Batch :",font=("Century Gothic",15),bg="#e0fbfc")
        
        
        options = ["AIML","CS"]
        clicked_batch = t.StringVar()
        clicked_batch.set("Select")
        clicked_branch = t.StringVar()
        clicked_branch.set("Select")        

        branch_options = ["AIML A","AIML B","Cs A","Cs B","Cs C","Civil","EnTC B","Mech","Robotics"]
        dropdown = t.OptionMenu(chose_label, clicked_branch, *branch_options)
        drop2    = t.OptionMenu(chose_label,clicked_batch,*batch_options)        
        
        
        prn_entr_label = t.Label(chose_label,text="Enter the P.R.N of the Student     : ",font=("Century Gothic",15),bg="#e0fbfc")
        prn_entr_entry = t.Entry(chose_label,font=("Century Gothic",15))

        def next_show():
            name_dis_label = t.Label(chose_label,text="Name of the Student            : ",font=("Century Gothic",15),bg="#e0fbfc")
            comp_1_label =   t.Label(chose_label,text="Enter the Marks of Component 1 : ",font=("Century Gothic",15),bg="#e0fbfc")
            comp_2_label =   t.Label(chose_label,text="Enter the Marks of Component 2 : ",font=("Century Gothic",15),bg="#e0fbfc")
            comp_3_label =   t.Label(chose_label,text="Enter the Marks of Component 3 : ",font=("Century Gothic",15),bg="#e0fbfc")
            
            
            prn = prn_entr_entry.get()
            branch = clicked_branch.get()
            batch = clicked_batch.get()
            #getting info
            abc = db.child("student_database").child(batch).child(branch).get()
            all_data=abc.val()
            student_data = all_data[prn]
            name = student_data["Data"]   
            name_dis_entry = t.Label(chose_label,text=name["Name"],font=("Century Gothic",15),width=50,anchor="w")
            comp_1_entry   = t.Entry(chose_label,font=("Century Gothic",15))
            comp_2_entry   = t.Entry(chose_label,font=("Century Gothic",15))
            comp_3_entry   = t.Entry(chose_label,font=("Century Gothic",15))
            
            add_comp_label = t.Label(chose_label,text="To add more Components --> ",font=("Verdana 11"),bg="#e0fbfc")
            add_comp = t.Button(chose_label,text="Click Here",activebackground="white",background="#e0fbfc",bd=0,font=("Verdana 11 underline"),cursor="hand2")
            button_hide_Label = t.Label(chose_label,bg="#e0fbfc",height=50,width=70)
            sub_dictionary = student_data[sub_info]
            try :
                if sub_dictionary["Comp 1"] != 0:
                    comp_1_entry.insert(0,sub_dictionary["Comp 1"])
                if sub_dictionary["Comp 2"] != 0:
                    comp_2_entry.insert(0,sub_dictionary["Comp 2"])
                if sub_dictionary["Comp 3"] != 0:
                    comp_3_entry.insert(0,sub_dictionary["Comp 3"])
            except :
                pass
            name_dis_label.place(x=10,y=110)
            comp_1_label.place(x=10,y=160)
            comp_2_label.place(x=10,y=210)
            comp_3_label.place(x=10,y=260)
            
            
            name_dis_entry.place(x=320,y=113)
            comp_1_entry.place(x=355,y=163)
            comp_2_entry.place(x=355,y=213)
            comp_3_entry.place(x=355,y=263)  
            # add_comp_label.place(x=10,y=360)
            # add_comp.place(x=250,y=360) 
            button_hide_Label.place(x=580,y=360)
            
            
            
            
            def add_to_db():
                c1_val = comp_1_entry.get()
                c2_val = comp_2_entry.get()
                c3_val = comp_3_entry.get()
                if c1_val == "":
                    c1_val = "0"
                if c2_val == "":
                    c2_val = "0"
                if c3_val == "":
                    c3_val = "0"
                
                total = int(c1_val)+int(c2_val)+int(c3_val)
                
                student_data[sub_info]={"Comp 1" : c1_val,"Comp 2": c2_val,"Comp 3":c3_val,"Total":total}
                
                db.child("student_database").child(batch).child(branch).child(prn).set(student_data)
                
                name_dis_entry.destroy()
                name_dis_label.destroy()
                comp_1_entry.destroy()
                comp_1_label.destroy()
                comp_2_entry.destroy()
                comp_2_label.destroy()
                comp_3_entry.destroy()
                comp_3_label.destroy()
                add_comp.destroy()
                button_hide_Label.destroy()
                add_comp_label.destroy()
                prn_entr_entry.delete(0,END)
                t.messagebox.showinfo("","Added To Database")
            
            done_btn = t.Button(entry_canvas,text="Add to Database",command=add_to_db)    
            done_btn.place(x=20,y=480)
        next_btn = t.Button(chose_label,text="Next",command=next_show)
        
        # xl function

        def gen_xl():
            xl_file = fd.asksaveasfilename(initialfile="Untitled.xlsx",defaultextension=".xlsx",filetypes = [('excel files', '*.xlsx'),('All files', '*.*')]) 
            batch_get = clicked_batch.get()
            branch_get=clicked_branch.get()
            data_ = db.child("student_database").child(batch_get).child(branch_get).get()
            data_dict = data_.val()
            list_keys = data_dict.keys()
            name_list = []
            value_list = {}
            comp1_list = []
            comp2_list = []
            comp3_list = []
            total_list = []
            for x in list_keys:
                in_data = data_dict[x]
                name_da = in_data["Data"]
                name_list.append(name_da["Name"])
                
                
                comp_da = in_data[sub_info]
                comp1_list.append(comp_da["Comp 1"])
                comp2_list.append(comp_da["Comp 2"])
                comp3_list.append(comp_da["Comp 3"])
                
                if "Total" in comp_da.keys():
                    total_list.append(comp_da["Total"])
                else :
                    total_list.append("0")

            key_list = []
            for x in list_keys:
                key_list.append(x)
            
            value_list["P.R.N"] = key_list
            value_list["Component 1"] = comp1_list
            value_list["Component 2"] = comp2_list
            value_list["Component 3"] = comp3_list
            value_list["Total"] = total_list
            table = pd.DataFrame(value_list,index=name_list)
            table.to_excel(xl_file,sheet_name="1")
        
        def upl_xl():
            filetypes = (('excel files', '*.xlsx'),('All files', '*.*'))
            
            filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
            df = pd.read_excel(filename,sheet_name="1")
            upload_dict = df.to_dict()
            up_name_dict = upload_dict['Unnamed: 0']
            # up_cmp1_dict = upload_dict['']
            up_prn_dict = upload_dict['P.R.N']
            print(upload_dict)
            #
            batch_get = clicked_batch.get()
            branch_get= clicked_branch.get()
            for x in up_prn_dict:
                cmp1_ = upload_dict["Component 1"]
                cmp2_ = upload_dict["Component 2"]
                cmp3_ = upload_dict["Component 3"]
                totl_ = upload_dict["Total"]
                diction = {"Data":{"Name":up_name_dict[x]},sub_info:{"Comp 1":cmp1_[x],"Comp 2":cmp2_[x],"Comp 3":cmp3_[x],"Total":totl_[x]}}
                db.child("student_database").child(batch_get).child(branch_get).child(up_prn_dict[x]).set(diction)

            t.messagebox.showinfo("","Upload Successful !")
        genx_btn = t.Button(entry_canvas,text="Generate Excel Sheet",command=gen_xl)
        uplx_btn = t.Button(entry_canvas,text="Upload Data from Excel",command=upl_xl)

        
        #Panned window for display
        display_canvas = t.PanedWindow(win,width=542, height=530,bg="#8ecae6")
        title_2_label = t.Label(display_canvas,text = "View Data",font=("Poppins Light",20),bg="#8ecae6")
        list_window = t.PanedWindow(display_canvas,width=300,height=410)
        list = t.Listbox(list_window,width=50,height=25)
        clicked = t.StringVar()
        clicked.set("Select")
        batch_label = t.Label(display_canvas,text="Select the Batch :",font=("Arial",12),bg="#8ecae6")
        batch_drop = t.OptionMenu(display_canvas,clicked_batch,*batch_options)
        
        class_label= t.Label(display_canvas,text="Select the Branch",font=("Arial",12),bg="#8ecae6")
        class_drop = t.OptionMenu(display_canvas,clicked_branch,*branch_options)
        def display_stuff():
            get_branch = clicked_branch.get()
            get_batch  = clicked_batch.get()
            list.delete(0,END)
            main_dic  = db.child("student_database").child(get_batch).child(get_branch).get()
            comp_dic  = main_dic.val()
            for x in comp_dic.keys():
                name_doc = comp_dic[x]
                name_dictt =name_doc["Data"]
                list.insert(END,name_dictt["Name"])
        def data_from_list(event):
            get_branch = clicked_branch.get()
            get_batch  = clicked_batch.get()
            main_dic  = db.child("student_database").child(get_batch).child(get_branch).get()
            comp_dic  = main_dic.val()
            prn_entr_entry.delete(0,END)
            
            l1 = []
            for x in comp_dic.keys():
                l1.append(x)
            cs = list.curselection()
            prn_list = l1[int(cs[0])]
            prn_entr_entry.insert(0,prn_list)
            next_show()
            # t.messagebox.showinfo(sub_info,text_in_box)
        list.bind('<Double-1>',data_from_list)
        
        show_btn = t.Button(display_canvas,text="Show Data",command=display_stuff)
        
        #Placing:
        
        #--entry canvas:
        title_label.place(x=20,y=5)
        chose_label.place(x=20,y=60)
        
        #--in place:
        dropdown_label.place(x=10,y=10)
        drop2_label.place(x=330,y=10)
        drop2.place(x=525,y=10)
        dropdown.place(x=200,y=10)
        prn_entr_label.place(x=10,y=60)
        next_btn.place(x=580,y=360)
        
        prn_entr_entry.place(x=350,y=63)
        
        genx_btn.place(x=530,y=480)
        uplx_btn.place(x=250,y=480)
        
        #--view data:
        title_2_label.place(x=20,y=5)
        list_window.place(x=20,y=60)
        list.pack()
        
        batch_label.place(x=390,y=70)
        batch_drop.place(x=390,y=100)
        
        class_label.place(x=390,y=150)
        class_drop.place(x=390,y=180)
        
        show_btn.place(x=390,y=250)
        
        #--top_frame:
        
        prof_btn.place(x=1190,y=10)
        log_out_btn.place(x=1190,y=50)
        symbi_img_label.place(x=10,y=10)
        
        #--frames and Canvas
        top_frame.place(x=0,y=0)
        entry_canvas.place(x=10,y=160)
        display_canvas.place(x=725,y=160)
        
        win.mainloop()

def show_entry_fields():
    #Getting Values
    user_name = n3.get()
    #ps_word = n4.get()
    password = n4.get()
    app = Main(user_name)
    try :
        user_details = auth.get_user(user_name)
    except firebase_admin._auth_utils.UserNotFoundError:
        t.messagebox.showerror("","Invalid Username")
    mail_get = user_details.email
    try :
        authent.sign_in_with_email_and_password(email=mail_get,password=password) 
        t.messagebox.showinfo("","Log in Successfull")
    except :
        t.messagebox.showerror("","Invalid Password")
        pass
    else :
        m.destroy()
        premium = auth.get_user(user_name)
        check_admin = premium.custom_claims.get("admin")
        if check_admin == True:
            app.ops()
        else :
            app.view()
    return user_name    

# In[1]
def sign_up():
    s = t.Toplevel()
    s.geometry("350x500")
    s.title("Sign up portal") 
    label_1 =t.Label(s, text="Sign up Portal",font=("Impact",15))
    label_2 =t.Label(s, text="Enter your Username   : ")
    label_3 =t.Label(s, text="Enter your First name  : ")
    label_4 =t.Label(s, text="Enter your Last name   : ")
    label_5 =t.Label(s, text="Enter your Email ID    : ")
    label_6 =t.Label(s, text="Enter your Password    : ")
    label_7 = t.Label(s, text="Sign up as               : ")

    user_id = t.Entry(s)
    f_name  = t.Entry(s)
    l_name  = t.Entry(s)
    mail_id = t.Entry(s)
    pswd    = t.Entry(s)



    label_1.place(x=120,y=10)
    label_2.place(x=10,y=50)
    user_id.place(x=170,y=53)

    label_3.place(x=10,y=90)
    f_name.place(x=170,y=92)

    label_4.place(x=10,y=130)
    l_name.place(x=170,y=132)

    label_5.place(x=10,y=170)
    mail_id.place(x=170,y=172)

    label_6.place(x=10,y=210)
    pswd.place(x=170,y=212)

    label_7.place(x=10,y=250)
    radio = t.StringVar()
    radio.set(None)
    r_btn1 = t.Radiobutton(s, text="Teacher",variable=radio,value="Teacher")
    r_btn2 = t.Radiobutton(s, text="Student",variable=radio,value="Student")
    r_btn1.place(x=170,y=250)
    r_btn2.place(x=260,y=250)
    def done():      
        uid = user_id.get()
        email = mail_id.get()
        password = pswd.get()
        fname = f_name.get()
        lname = l_name.get()
        
        data = {"First Name" : fname,"Last Name" : lname,"Mail id":email}
        try:
            auth.create_user(uid=uid,email=email,password=password)   
        except firebase_admin._auth_utils.UidAlreadyExistsError:
            t.messagebox.showerror("","Username Already exists")
        except ValueError as e:
            if str(e) == f'Malformed email address string: "{email}".':
                t.messagebox.showerror("","Invalid Email ID")
            elif str(e) == 'Invalid password string. Password must be a string at least 6 characters long.':
                t.messagebox.showerror("","Password must be at least 6 characters")
        else :
            
            if radio.get() == "Teacher":
                auth.set_custom_user_claims(uid,{"admin":True})
                smth = t.Toplevel()
                t.Label(smth,text="Enter the Subject : ").grid(row=0,column=0)
                sn = t.Entry(smth)
                
                def finish():
                    data["Subject"]=sn.get()
                    db.child("User-Data Base").child("Teachers").child(uid).set(data)
                    abc = db.child("student_database").get()
                    all_data = abc.val()


                    for x in all_data.keys():
                        dic1 = all_data[x]
                        for y in dic1:
                            dic2 = dic1[y]
                            for z in dic2:
                                dic3 = dic2[z]
                                dic3[sn.get()]={"Comp 1":"0","Comp 2":"0","Comp 3":"0"}
                                db.child("student_database").child(x).child(y).child(z).set(dic3)
                    t.messagebox.showinfo("","Sign Up Successfull !!")
                    s.destroy()
                    smth.destroy()
                t.Button(smth,text="Done",command=finish).grid(row=2)
                sn.grid(row=0,column=1)
                
            elif radio.get() == "Student":
                auth.set_custom_user_claims(uid,{"admin":False})
                top_lvl = t.Toplevel()
                chose_batch_label = t.Label(top_lvl,text="Select your Batch : ",font=("Century Gothic",15),bg="#83b1cf")
                chose_branch_label= t.Label(top_lvl,text="Select your Branch :",font=("Century Gothic",15),bg="#83b1cf")
                prn_enter_label = t.Label(top_lvl,text="Enter your P.R.N : ",font=("Century Gothic",15),bg="#83b1cf")
                #name_label      = t.Label(mid_frame,text="Name : ",font=("Century Gothic",15),bg="#83b1cf")
                chose_sub_label = t.Label(top_lvl,text="Choose the Subject : ",font=("Century Gothic",15),bg="#83b1cf")
                
                clicked_batch = t.StringVar()
                clicked_batch.set("Select")
                from_db = db.child("student_database").get()
                batch_dict = from_db.val()
                options_batch = batch_dict.keys()
                
                clicked_branch = t.StringVar()
                clicked_branch.set("Select")
                options_branch = ["AIML A","AIML B","Cs A","Cs B","Cs C"]
                chose_batch_drop = t.OptionMenu(top_lvl,clicked_batch,*options_batch)
                chose_branch_drop= t.OptionMenu(top_lvl,clicked_branch,*options_branch)
                prn_enter_entry  = t.Entry(top_lvl,font=("Century Gothic",15))
                
                def finish():
                    batch = clicked_batch.get()
                    branch = clicked_branch.get()
                    prn = prn_enter_entry.get()
                    
                    data["Batch"] = batch
                    data["Branch"] = branch
                    data["PRN"] = prn
                    
                    t.messagebox.showinfo("","Sign Up Successfull !!")
                    s.destroy()
                    top_lvl.destroy()
                    db.child("User-Data Base").child("Students").child(uid).set(data)
                done_btn = t.Button(top_lvl,text="Done",command=finish)
                chose_batch_label.grid(row=0,column=0)
                chose_batch_drop.grid(row=0,column=1)
                chose_branch_label.grid(row=1,column=0)
                chose_branch_drop.grid(row=1,column=1)
                prn_enter_label.grid(row=2,column=0)
                prn_enter_entry.grid(row=2,column=1)
                done_btn.grid(row=4,column=0)


    btn_01=t.Button(s, text="Sign Up", command=done)

    btn_01.place(x=110,y=330)
    #btn_02.place(x=100,y=350
    s.mainloop()

# In[2]
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
        authent.send_password_reset_email(get_name)
        t.messagebox.showinfo("","Password Sent to Email")
                    
    win_button = t.Button(win,text="Get ",command=get_p).grid(row=2,column=2)
    win.mainloop()

#--------------------------------------------------------------------------#
    
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
f1.place(x=650,y=100)
f2.place(x=250,y=100)


#frame 1 components
n1=t.Label(f1, text="Username :",font=("Bahnschrift SemiLight",10),bg="#333333",fg="#D2D2D2")
n2=t.Label(f1, text="Password :",font=("Bahnschrift SemiLight",10),bg="#333333",fg="#D2D2D2")
n3=t.Entry(f1, highlightthickness=0, font=("Lucida Sans",10), relief="flat", width=30,bg="#333333",fg="white")
n4=t.Entry(f1, highlightthickness=0, font=("Lucida Sans",10), relief="flat", width=30,bg="#333333",fg="white", show="*")

n6 = t.Button(f1, text="Sign Up", relief="flat",command=sign_up,font=("Lucida Sans",10,"underline"),bd=0,bg="#333333",activebackground="#333333",fg="white",cursor="hand2")

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
n5 = t.Button(login_label, text='LOGIN',font=("yu gothic ui",9,"bold"),bd=0,width=25,command=show_entry_fields,bg="#3047ff",cursor="hand2", activebackground="#3047ff",fg="white",relief="flat")
n5.place(x=14,y=8)

#forgot Password
frgt_psswd = t.Button(f1,text="Forgot Password ?",font=("yu gothic ui",9,"underline"),bd=0,bg="#333333",activebackground="#333333",cursor="hand2",fg="white",command=forgot_pass)



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
Check_Box = t.Checkbutton(f1, text="Show Password", variable=var1,onvalue=1,offvalue=0,bg="#333333",bd=0,activebackground="#333333",command=show_password)

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