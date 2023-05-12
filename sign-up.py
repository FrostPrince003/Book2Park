from tkinter import *
from tkinter import messagebox



root=Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

img = PhotoImage(file='parking1.png')
Label(root,image=img,border=0,bg='white').place(x=-340,y=-280)

frame=Frame(root,width=400,height=350,bg='#fff')
frame.place(x=450,y=80)

heading=Label(frame,text='New User? Sign in!',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',20,))
heading.place(x=120, y=5)

Guest=Button(frame,text='Guest Mode',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',12))
Guest.place(x=300, y=300)

Login=Button(frame,text='Already registered? Login',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',12))
Login.place(x=60, y=300)

signup=Button(frame,text='Sign Up',pady=2,width=18,fg='white',border=1,bg='skyblue',font=('Microsoft Yahei UI Light',14))
signup.place(x=135,y=250)


        
        
user=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
user.place(x=60,y=50)
user.insert(0,'Username:')



Frame(frame,width=350,height=2,bg='black').place(x=60,y=80)
Frame(frame,width=350,height=2,bg='black').place(x=60,y=130)
Frame(frame,width=350,height=2,bg='black').place(x=60,y=180)
Frame(frame,width=350,height=2,bg='black').place(x=60,y=230)

passkey=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
passkey.place(x=60,y=150)
passkey.insert(0,'Password:')



vno=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
vno.place(x=60,y=100)
vno.insert(0,'Vehicle No.:')



confirmpass=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
confirmpass.place(x=60,y=200)
confirmpass.insert(0,'Confirm Password:')

root.mainloop()