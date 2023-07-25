import tkinter
import json

#------------------------------------------------------------

def login():
#----------get Entry text----------
#user=txt_user.get()
#print(user)

#user=txt_user.get()
#pas=txt_pass.get()
#if user=="admin" and pas=="f123":
#   lbl_msg.configure(text="welcome to your account!",fg="green")
#else:
#   lbl_msg.configure(text="wrong username or password!",fg="red")

    user=txt_user.get()
    pas=txt_pass.get()
    with open("info.json") as f:
        dct=json.load(f)
    if (user in dct) and (dct[user]==pas):
        lbl_msg.configure(text="welcome to your account!",fg="green")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
    else:
        lbl_msg.configure(text="wrong username or password!",fg="red")


def submit():
    user=txt_user.get()
    pas=txt_pass.get()
    cpas=txt_cpass.get()
    
    if pas!=cpas:
        lbl_msg.configure(text="password and confirmation mismatch",fg="red")
        return
    if (len(pas)) < 8:
        lbl_msg.configure(text="password length should be at least 8 chars",fg="red")
        return
    
    with open("info.json") as f:
        dct=json.load(f)
    
    if user in dct:
        lbl_msg.configure(text="username already exist!",fg="red")
        return
    
    dct[user]=pas
    with open("info.json",'w') as f:
        json.dump(dct,f)
    lbl_msg.configure(text="submit done!",fg="green")
    
    txt_user.delete(0,"end")
    txt_pass.delete(0,"end")
    txt_cpass.delete(0,"end")


def edit():
    user=txt_user.get()
    pas=txt_pass.get()
    
    with open("info.json") as f:
        dct=json.load(f)
    if (user in dct) and (dct[user]==pas):
        lbl_msg.configure(text="please enter new password and confirmation : ",fg="green")
        
        npas=txt_npass.get()
        cnpas=txt_cnpass.get()
        
        if npas!=cnpas:
            lbl_msg.configure(text="password and confirmation mismatch",fg="red")
        if (len(npas)) < 8:
            lbl_msg.configure(text="password length should be at least 8 chars",fg="red")
            return
        
        with open("info.json") as f:
            dct=json.load(f)
        
        dct[user]=npas

        with open("info.json",'w') as f:
            json.dump(dct,f)
        lbl_msg.configure(text="edit done!",fg="green")

        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        txt_npass.delete(0,"end")
        txt_cnpass.delete(0,"end")
    else:
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return

def users_list():
    win2=tkinter.Toplevel()
    win2.geometry("250x250")
    win2.title("users list")
    
    listbx=tkinter.Listbox(win2)
    listbx.pack()
    
    with open("info.json") as f:
        dct=json.load(f)
    
    for user,pas in dct.items():
        listbx.insert("end",user)
    
    win2.mainloop()

#------------------------------------------------------------

#new window
win=tkinter.Tk()

#window size
win.geometry("400x400")

#window title
win.title("first project")

#new label widget
lbl_user=tkinter.Label(win,text="username : ")
lbl_user.pack()

#new text widget
txt_user=tkinter.Entry(win)
txt_user.pack()

#new label widget
lbl_pass=tkinter.Label(win,text="password : ")
lbl_pass.pack()

#new text widget
txt_pass=tkinter.Entry(win)
txt_pass.pack()

#new label widget
lbl_cpass=tkinter.Label(win,text="password confirmation : ")
lbl_cpass.pack()

#new text widget
txt_cpass=tkinter.Entry(win)
txt_cpass.pack()

#new label widget
lbl_npass=tkinter.Label(win,text="new password : ")
lbl_npass.pack()

#new text widget
txt_npass=tkinter.Entry(win)
txt_npass.pack()

#new label widget
lbl_cnpass=tkinter.Label(win,text="new password confirmation : ")
lbl_cnpass.pack()

#new text widget
txt_cnpass=tkinter.Entry(win)
txt_cnpass.pack()

#label for messages
lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

#new button widget
btn=tkinter.Button(win,text="login",command=login)
btn.pack()

#new button widget
btn_submit=tkinter.Button(win,text="submit",command=submit)
btn_submit.pack()

#new button widget
btn_edit=tkinter.Button(win,text="edit",command=edit)
btn_edit.pack()

#new button widget
btn_users=tkinter.Button(win,text="users list",command=users_list)
btn_users.pack()

win.mainloop()