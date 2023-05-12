from tkinter import *

root=Tk()
root.title("Guest mode")
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False,False)


img = PhotoImage(file='parking1.png')
Label(root,image=img,border=0,bg='white').place(x=-340,y=-280)



frame=Frame(root,width=400,height=350,bg='#fff')
frame.place(x=450,y=80)
heading=Label(frame,text='Login using Guest Mode!',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',20,))
heading.place(x=40, y=5)

#main buttons
signup=Button(frame,text='Click here to Enter',pady=2,width=18,fg='white',border=1,bg='skyblue',font=('Microsoft Yahei UI Light',14))
signup.place(x=80,y=200)

Login=Button(frame,text='Already registered? Login',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',12))
Login.place(x=20, y=300)

Login=Button(frame,text='Sign Up',border=0,fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',12))
Login.place(x=300, y=300)


#input 

Frame(frame,width=250,height=2,bg='black').place(x=60,y=100)
Frame(frame,width=250,height=2,bg='black').place(x=60,y=150)

user=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
user.place(x=60,y=70)
user.insert(0,'Username: ')


vno=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
vno.place(x=60,y=120)
vno.insert(0,'Vehicle No.: ')


root.mainloop()