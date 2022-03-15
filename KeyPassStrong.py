import tkinter as tk
import os
import time
import subprocess as sp
import random
import sys
from tkinter import ttk
from pathlib import Path
import datetime
import urllib.request




def main_program(): 
    global main
    main=tk.Tk()

    main_width=500
    main_height=150
    screen_width=main.winfo_screenwidth()
    screen_height=main.winfo_screenheight()

    x_cordinates=(screen_width/2)-(main_width/2)
    y_cordinates=(screen_height/2)-(main_height/2)

    main.geometry( "%dx%d+%d+%d" % (main_width,main_height,x_cordinates,y_cordinates))

    dirname = os.path.dirname(__file__)
    ico=os.path.join(dirname,"Files","key.ico")
    main.iconbitmap(ico)

    main.title("Password Generator")
    main.resizable(False, False)
    global site,username
    
    usernamee.delete(0, tk.END)
    passworde.delete(0, tk.END)
    start.withdraw()
    
    site1=tk.Label(main,text="Site:")
    site1.place(x=5,y=5)

    site=tk.Entry(main,width=35)
    site.place(x=5,y=25)

    username1=tk.Label(main,text="Username:")
    username1.place(x=5,y=45)

    username=tk.Entry(main,width=35)
    username.place(x=5,y=65)

    symbols=["@","!","%","#","$","&"]
    up=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    low=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","e","x","y","z"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    def randomcoice():
        temp=[]
        for i in range(4):
            s=random.choice(symbols)
            c=random.choice(low)
            v=random.choice(up)
            b=random.choice(numbers)
            temp.append(s)
            temp.append(c)
            temp.append(v)
            temp.append(b)
        
        l=""
        for i in range(4):
            l+=random.choice(temp)
        return(l)


    def main_destroy_label():
        global save_lbl
        save_lbl.destroy()       


    def save():

        global save_lbl
        global account
        global g 
        currentDT = datetime.datetime.now()

        username3=username.get()
        site3=site.get()

        dirname = os.path.dirname(__file__)
        path=os.path.join(dirname,r"Files\Users_Data")      
        save_txt=os.path.join(dirname,r"Files\Users_Data",account+".txt")
        save_txt_file=account+".txt"
        txt_files=os.listdir(path)
        
        if site3!="":
            if username3!="":
                if password2["state"]=="normal":
                    if save_txt_file in txt_files:
                        file=open(save_txt,"a")
                        file.write("Site:"+site3+"\n")
                        file.write("Username:"+username3+"\n")
                        file.write("Password:"+g+"\n")
                        file.write("Time Added:"+currentDT.strftime("%Y-%m-%d %H:%M")+"\n"+"\n")
                        file.close()

                        password2.delete(0,tk.END)
                        site.delete(0,tk.END)
                        username.delete(0,tk.END)
                        password2["state"]="disabled"

                        save_lbl=tk.Label(main,text="Save Success!",fg="green",font=(20))

                        save_lbl.place(x=320, y=100)
                        main.after(600,main_destroy_label)


                    else:
                        file=open(save_txt,"w")
                        file.write("Site:"+site3+"\n")
                        file.write("Username:"+username3+"\n")
                        file.write("Password:"+g+"\n"+"\n")
                        file.close()

                        password2.delete(0,tk.END)
                        site.delete(0,tk.END)
                        username.delete(0,tk.END)
                        password2["state"]="disabled"
                        save_lbl=tk.Label(main,text="Save Success!",fg="green",font=(20))
                        save_lbl.place(x=320, y=100)
                        main.after(1500,main_destroy_label)
                else:
                    save_lbl=tk.Label(main,text="Generate Password!",fg="red",font=(20))
                    save_lbl.place(x=310, y=100)
                    main.after(600,main_destroy_label)
    
            else:
                save_lbl=tk.Label(main,text="Insert Username!",fg="red",font=(20))
                save_lbl.place(x=320, y=100)
                main.after(600,main_destroy_label)
            
        else:
            save_lbl=tk.Label(main,text="Insert Site Name!",fg="red",font=(20))
            save_lbl.place(x=320, y=100)
            main.after(600,main_destroy_label)
            

    def generate():
        global g
        password2["state"]="normal"
        password2.delete(0,tk.END)
        a=""
        for i in range(3):
            a+=randomcoice()
        password2["state"]="normal"
        password2.insert(0,a)
        g=password2.get()
    

    def close():
        main.destroy()
        start.destroy()


    def open1():
        global account
        dirname = os.path.dirname(__file__)

        path=os.path.join(dirname,r"Files\Users_data")
        txt_file=os.path.join(path,account+".txt")
        import webbrowser
        webbrowser.open(txt_file)
        

    password=tk.Label(main,text="Password:")
    password.place(x=5,y=85)

    password2=tk.Entry(main,text="", state='disabled',width=35)
    password2.place(x=5,y=105)
    
    openf=tk.Button(main,text="OPEN",width=11,command=open1)
    close=tk.Button(main,text="QUIT",width=11,command=close)
    save=tk.Button(main,text="SAVE",command=save,width=11)
    generate=tk.Button(main,text="GENERATE",command=generate,width=11)
    logout=tk.Button(main,text="Log Out",command=loggout_main,width=25)
    
    
    close.place(x=398, y=63)
    generate.place(x=398, y=25)
    save.place(x=298, y=25)
    openf.place(x=298, y=63)
    logout.place(x=298 , y=100)

    main.mainloop()

def loggout_main():
    main.destroy()
    start.deiconify()
   
def clear_admin():    
    admin_label_done["text"]=""
    admin_label_wrong["text"]=""
    admin_label_wrong2["text"]=""

def name_new():
    global newname_admin
    global usernamead
    global values1
    global cmbox

    dirname = os.path.dirname(__file__)
    path=os.path.join(dirname,r"Files\Users")
    data_path=os.path.join(dirname,r"Files\Users_Data")


    my_admin_files3=os.listdir(path)
    ExistName=cmbox.get()
    existname_path=os.path.join(path,ExistName)
    existname_data_path=os.path.join(data_path,ExistName+".txt")
    NewName=newname_admin.get()
    NewName_path=os.path.join(path,NewName)
    NewName_data_path=os.path.join(data_path,NewName+".txt")
    
    if ExistName in my_admin_files3:
        if NewName!="":
            file3=open(existname_data_path,"r")
            b=file3.read()
            file3.close()
            os.remove(existname_data_path)

            file=open(existname_path,"r")
            a=file.readline()
            file.close()
            os.remove(existname_path)
            
            file2=open(NewName_path,"w")
            file2.write(a)
            file2.close()        
            
            file4=open(NewName_data_path,"w")
            file4.write(b)
            file4.close()
            
            newname_admin.delete(0, tk.END)
            admin_label_done["text"]="Username changed!"
            admin.after(1500,clear_admin)

            my_admin_files3=os.listdir(path)
            values2=[]
            for i in my_admin_files3:
                values2.append(i)

            cmbox.destroy()

            cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values2)
            cmbox.set("Select User")
            cmbox.place(x=5,y=25)


        else:
            admin_label_wrong["text"]="Insert new username!"
            admin.after(1500,clear_admin)
            
    else:
        
        admin_label_wrong["text"]="User not found!"
        newname_admin.delete(0, tk.END)
        admin.after(1500,clear_admin)

def pass_new():
    global users
    global usernamead
    global newpass_admin
    username_info_admin=cmbox.get()
    password_info_admin=newpass_admin.get()
    dirname = os.path.dirname(__file__)
    path=os.path.join(dirname,r"Files\Users")
        
    my_admin_files=os.listdir(path)
    
    save_file=os.path.join(path,username_info_admin)
    if username_info_admin in my_admin_files:
        if password_info_admin!="Select User":
            newpass_admin.delete(0, tk.END)
            file=open(save_file,"w")
            file.write(password_info_admin)
            file.close()
            admin_label_done["text"]="Password changed!"
            admin.after(1500,clear_admin)
        else:
            admin_label_wrong2["text"]="Please enter new password!"
            admin.after(1500,clear_admin)
        
    else:
        newpass_admin.delete(0, tk.END)
        admin_label_wrong["text"]="Select User!"
        admin.after(1500,clear_admin)

def show_file():
    global cmbox,admin
    global users

    username_info_admin=cmbox.get()
    lines=[]

    dirname = os.path.dirname(__file__)
    path=os.path.join(dirname,r"Files\Users")
    save_path_user_txt=os.path.join(dirname,r"Files\Users_Data",username_info_admin+".txt")
    file=open(save_path_user_txt,"r")
    a=file.read()
    file.close()

    if username_info_admin!="Select User":             
        import webbrowser
        webbrowser.open(save_path_user_txt)

        values21=[]
        users1=os.listdir(path)
        for file in users1:
            values21.append(file)
        cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values21)
        cmbox.set("Select User")
        cmbox.place(x=5,y=25)

    else:
        admin_label_wrong["text"]="Select User"
        admin.after(1500,clear_admin)

        values21=[]    
        users1=os.listdir(path)
        for file in users1:
            values21.append(file)
        cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values21)
        cmbox.set("Select User")
        cmbox.place(x=5,y=25)
    
def destroyLabel():
    global admin_label_wrong12
    admin_label_wrong12.destroy()

def remove_no():
    global cmbox
    error.destroy()
    username_info_admin=cmbox.get()
    dirname = os.path.dirname(__file__)

    path=os.path.join(dirname,r"Files\Users")  
    path2=os.path.join(dirname,r"Files\Users_Data")
    path_final=os.path.join(path,username_info_admin)
    path_final2=os.path.join(path2,username_info_admin+".txt")
    os.remove(path_final)
    os.remove(path_final2)

    values21=[]
    
    users=os.listdir(path)
    for file in users:
        values21.append(file)
    cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values21)
    cmbox.set("Select User")
    cmbox.place(x=5,y=25)

def remove_yes():
    global cmbox
    error.destroy()



    username_info_admin=cmbox.get()
    cmbox.destroy()

    dirname = os.path.dirname(__file__)
    path01=os.path.join(dirname,r"Files\Removed_Users_Data")

    path1=os.listdir(path01)

    path2=os.path.join(dirname,r"Files\Removed_Users_Data")

    removed_users=os.path.join(path2,username_info_admin+".txt")

    path3=os.path.join(dirname,r"Files\Users_data")

    exist_user_data=os.path.join(path3,username_info_admin+".txt")

    path4=os.path.join(dirname,r"Files\Users")

    exist_user=os.path.join(path4,username_info_admin)

   


    if username_info_admin+".txt" in path1:
        file=open(removed_users,"a")
        file2=open(exist_user_data,"r")
        a=file2.read()
        for line in file2:
            file.write(line)
        file.close()
        file2.close()
        os.remove(exist_user_data)
        os.remove(exist_user)


    else:
        file=open(removed_users,"w")
        file2=open(exist_user_data,"r")
        for line in file2:
            file.write(line)
        file.close()
        file2.close()
        os.remove(exist_user_data)
        os.remove(exist_user)
    values21=[]
    
    users=os.listdir(path4)
    for file in users:
        values21.append(file)
    cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values21)
    cmbox.set("Select User")
    cmbox.place(x=5,y=25)

def remove_user():
    global admin_label_wrong12 
    global error
    global admin_height,admin_width
    username_info_admin=cmbox.get()
    dirname = os.path.dirname(__file__)
    path=os.path.join(dirname,r"Files\Users")
    my_admin_files=os.listdir(path)
    if username_info_admin!="Select User":
        if username_info_admin in my_admin_files:
            error=tk.Toplevel(admin)
            
            error_width=260
            error_height=85
            screen_width=error.winfo_screenwidth()
            screen_height=error.winfo_screenheight()
            x_cordinates=(screen_width/2)-(error_width/2)
            y_cordinates=(screen_height/2)-(error_height/2)
            error.geometry( "%dx%d+%d+%d" % (error_width,error_height,x_cordinates,y_cordinates))


            error.resizable(False, False)

            error.title("Files:")
            sure=tk.Label(error,text="Do you want to keep user's files?",font=(8))
            sure.place(x=10,y=5)

            okbtn=tk.Button(error,text="YES",width=7,command=remove_yes)
            okbtn.place(x=60,y=40)

            nobtn=tk.Button(error,text="NO",width=7,command=remove_no)
            nobtn.place(x=130,y=40)
            error.mainloop()
    else:
        admin_label_wrong12=tk.Label(admin,text="Please select a user!",fg="red", font=(20))
        admin_label_wrong12.place(x=255,y=107)
        admin.after(1500,destroyLabel)

def loggout_admin():    
    start.deiconify()
    admin.destroy()

def admin1():    
    global admin   
    global usernamead
    global newpass_admin
    global admin_label_done,admin_label_wrong,admin_label_wrong2
    global newname_admin    
    global cmbox
    global values1
    global users
    global admin_height , admin_width
    usernamee.delete(0, tk.END)
    passworde.delete(0, tk.END)
    start.withdraw()
    
    admin=tk.Tk()
    admin.title("Admin Panel")
    dirname = os.path.dirname(__file__)
    ico=os.path.join(dirname,"Files","key.ico")
    admin.iconbitmap(ico)

    admin_width=500
    admin_height=420
    screen_width=admin.winfo_screenwidth()
    screen_height=admin.winfo_screenheight()
    
    x_cordinates=(screen_width/2)-(admin_width/2)
    y_cordinates=(screen_height/2)-(admin_height/2)
    admin.geometry( "%dx%d+%d+%d" % (admin_width,admin_height,x_cordinates,y_cordinates))
    
    admin.resizable(False, False)
    
    users=ttk.Notebook(admin,width=493, height=500)
    users.place(x=2,y=150)

    values1=[]
    dirname = os.path.dirname(__file__)
    path=os.path.join(dirname,r"Files\Users")
    my_admin_files=os.listdir(path)

    for x in my_admin_files:
        values1.append(x)

    cmbox=ttk.Combobox(admin,state="readonly",width=27,values=values1)
    cmbox.set("Select User")
    cmbox.place(x=5,y=25)

    admin_label_done=tk.Label(admin,text="",fg="green",font=(20))
    admin_label_done.place(x=277,y=107)

    admin_label_wrong=tk.Label(admin,text="",fg="red",font=(20))
    admin_label_wrong.place(x=273,y=107)

    admin_label_wrong2=tk.Label(admin,text="",fg="red",font=(20))
    admin_label_wrong2.place(x=235,y=107)

    username_input=tk.Label(admin,text="User:")
    username_input.place(x=5,y=2)

    newname_admin_label=tk.Label(admin,text="New Username:")
    newname_admin_label.place(x=5, y=50)

    newname_admin=tk.Entry(admin,width=30)
    newname_admin.place(x=5, y=71)

    newpass_admin_label=tk.Label(admin,text="New Password:")
    newpass_admin_label.place(x=5,y=95)

    newpass_admin=tk.Entry(admin,width=30,show="*")
    newpass_admin.place(x=5,y=116)

    remove=tk.Button(admin,text="Remove User",width=15,command=remove_user)       
    change_pass=tk.Button(admin,text="Change Password",command=pass_new,width=15)
    show=tk.Button(admin,text="Show File",width=15,command=show_file)
    change_name=tk.Button(admin,text="Change Username",width=15,command=name_new)    
    logout=tk.Button(admin,text="Log Out",command=loggout_admin,width=32)
    
    show.place(x=350, y=61)
    change_name.place(x=230, y=61)
    change_pass.place(x=230, y=21)
    remove.place(x=350, y=21)
    logout.place(x=230, y=110)

def clear_label_start_green():
    global done_label 
    done_label.destroy()

def clear_label_start_red():
   global done_label1 
   done_label1.destroy()   

def clear_label():
    global done_label3,done_label2,done_label4
    done_label3.destroy()
    done_label2.destroy()
    done_label4.destroy()

def login(): 
    global enable,enable1
    global save_path_user
    global account
    global done_label1,done_label
    global usernamee,passworde
    global username_info   
    global admin
    account=usernamee.get()
    username_info=usernamee.get()
    password_info=passworde.get()
    dirname = os.path.dirname(__file__)
    save_path_user=os.path.join(dirname,r"Files\Users",username_info)
    save_path_user_txt=os.path.join(dirname,r"Files\Users_Data",username_info+".txt")
    path_files= os.path.dirname(__file__)
    pathfiles=os.path.join(path_files,r"Files\Users")
 
    if username_info=="admin":
        if password_info=="admin":
            admin1()
        else:
            done_label3["text"]="Wrong Password!"     
            start.after(1500,clear_label) 
    
    else:
        list_of_files2=os.listdir(pathfiles)    
        if username_info in list_of_files2:
            file=open(save_path_user,"r")
            verify=file.read().splitlines()
            if password_info in verify:      
                done_label=tk.Label(start,text="Login success",fg="green",font=("calibri"),width=30)
                done_label.place(x=30, y=165)   
                start.after(450,clear_label_start_green)   
                start.after(600,main_program)
            else:
                done_label1=tk.Label(start,text="Wrong password!",fg="red",font=("calibri"))
                done_label1.place(x=90, y=165)   
                enable="red"                
                start.after(600,clear_label_start_red)                                 
        else:
            done_label1=tk.Label(start,text="Username not found!",fg="red",font=("calibri"))
            done_label1.place(x=85, y=165)
            enable="red"
            start.after(600,clear_label_start_red)
    
def register():
    global list_of_files
    global done_label1 , done_label
    global enable1,enable2
    username_info=usernamee.get()
    password_info=passworde.get() 

    dirname = os.path.dirname(__file__) 
    save_path_user=os.path.join(dirname,r"Files\Users",username_info)
    save_path_user_txt=os.path.join(dirname,r"Files\Users_Data",username_info+".txt")  
    path1=os.path.join(dirname,r"Files\Users")
    
    if username_info!="":     
        if password_info!="":
            list_of_files2=os.listdir(path1)

            if username_info in list_of_files2:
                done_label1=tk.Label(start,text="Username already exist",fg="red",font=("calibri"))
                enable1=True
                done_label1.place(x=78, y=165)
                start.after(600,clear_label_start_red)

            else:        
                file=open(save_path_user,"w")
                file.write(password_info)
                file.close()

                second=open(save_path_user_txt,"w")
                second.close()

                usernamee.delete(0, tk.END)
                passworde.delete(0, tk.END)
                done_label=tk.Label(start,text="Registration success",fg="green",font=("calibri"),width=30)
                enable2=True
                done_label.place(x=30, y=165)
                start.after(600,clear_label_start_green)
        else:
            done_label1=tk.Label(start,text="Enter password!",fg="red",font=("calibri"))
            enable1=True
            done_label1.place(x=95, y=165)
            start.after(600,clear_label_start_red)

    else:
        done_label1=tk.Label(start,text="Enter username!",fg="red",font=("calibri"))
        enable1=True
        done_label1.place(x=95, y=165)
        start.after(600,clear_label_start_red)

def start():    
    global save_path_user  
    global usernamee
    global passworde
    global register,login
    global start
    global done_label3, done_label2, done_label4

    dirname = os.path.dirname(__file__)
    p_path=os.path.join(dirname,"Files")
    p2_path=os.path.join(p_path,"Users")
    p3_path=os.path.join(p_path,"Users_Data")
    p4_path=os.path.join(p_path,"Removed_Users_Data")
    
    p = Path(p_path)
    p2 = Path(p2_path)
    p3=Path(p3_path)
    p4=Path(p4_path)
    p.mkdir(exist_ok=True)
    p4.mkdir(exist_ok=True)    
    p2.mkdir(exist_ok=True)
    p3.mkdir(exist_ok=True)

    url = 'http://www.iconarchive.com/download/i95222/dtafalonso/modern-xp/ModernXP-07-Keys.ico'
    path_ico=os.path.join(p_path,"key.ico")
    urllib.request.urlretrieve(url,path_ico)

    start=tk.Tk()
    start_width=300
    start_height=215
    screen_width=start.winfo_screenwidth()
    screen_height=start.winfo_screenheight()
    
    x_cordinates=(screen_width/2)-(start_width/2)
    y_cordinates=(screen_height/2)-(start_height/2)
    start.geometry( "%dx%d+%d+%d" % (start_width,start_height,x_cordinates,y_cordinates))
    
    start.title("KeyPassStrong")
    
    ico=os.path.join(dirname,"Files","key.ico")
    start.iconbitmap(ico)
    
    start.resizable(False, False)

    done_label2=tk.Label(start,text="",fg="green",font=("calibri"))
    done_label2.place(x=97, y=165)

    done_label3=tk.Label(start,text="",fg="red",font=("calibri"))
    done_label3.place(x=105, y=165)

    done_label4=tk.Label(start,text="",fg="red",font=("calibri"))
    done_label4.place(x=79, y=165)

    Label1=tk.Label(start,text="Welcome"+"\n",font=("bold"))
    Label1.pack()

    username=tk.Label(start,text="Username")
    username.pack()
    
    usernamee=tk.Entry(start)
    usernamee.pack()
    
    password=tk.Label(start,text="Password")
    password.pack()

    passworde=tk.Entry(start, show="*")
    passworde.pack()

    copyright_label=tk.Label(start,text="©", font=(15))
    copyright_label.place(x=32,y=188)

    copyright_label=tk.Label(start,text="2020 Alex Stamatiadis All Rights Reserved")
    copyright_label.place(x=48,y=190)

    login=tk.Button(start,text="Login",width=10,command=login)
    login.place(x=68, y=135)
    
    register=tk.Button(start,text="Register",width=10,command=register)
    register.place(x=160, y=135)

    start.mainloop()
  
start()