from tkinter import *
from tkinter import messagebox



root=Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

img = PhotoImage(file='parking1.png')
Label(root,image=img,border=0,bg='white').place(x=-350,y=-280)

frame=Frame(root,width=400,height=390,bg='#fff')
frame.place(x=450,y=80)

heading=Label(frame,text='New User? Sign in!',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',20,))
heading.place(x=120, y=5)

Guest=Button(frame,text='Guest Mode',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',10))
Guest.place(x=300, y=350)

Login=Button(frame,text='Already registered? Login',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',10))
Login.place(x=100, y=350)

signup=Button(frame,text='Sign Up',pady=1,width=25,fg='White',border=0,bg='#57a1f8',font=('Microsoft Yahei UI Light',14))
signup.place(x=115,y=260)



def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
        
        
user=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
user.place(x=110,y=67)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=110,y=90)

def on_enter(e):
    passkey.delete(0,'end')
def on_leave(e):
    if passkey.get()=='':
        passkey.insert(0,'Password')

passkey=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
passkey.place(x=110,y=134)
passkey.insert(0,'Password')
passkey.bind("<FocusIn>",on_enter)
passkey.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=110,y=160)

def on_enter(e):
    confirmpass.delete(0,'end')
def on_leave(e):
    if confirmpass.get()=='':
        confirmpass.insert(0,'Confirm Password')


confirmpass=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
confirmpass.place(x=110,y=214)
confirmpass.insert(0,'Confirm Password')
confirmpass.bind("<FocusIn>",on_enter)
confirmpass.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=110,y=240)
root.mainloop()
