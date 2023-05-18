from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("ParkiN")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def book():
    vehicleno = user.get()
    phoneno = Phone.get()
    gmailac = gmail.get()
    

    if vehicleno == 'M' and phoneno == 'M' and gmailac == 'M' :
        
        building=Toplevel(root)
        building.title('Parkin!')
        building.geometry('925x500+300+200')
        building.configure(bg='#fff')
        building.resizable(False,False)
    
        Label(building,text='Please select Your Parking Space',fg='#57a1f8',bg='white',font =('Microsoft Yahei UI Light',20)).place(x=285,y=5)
                
        Parking_A = Button(building,text='Parking A',pady=1,width=10,fg='black',border=0,bg='#FFFFEB',font=('Microsoft Yahei UI Light',14,))
        Parking_A.place(x=140,y=220)
        
        op = PhotoImage(file='parkinga.png')
        op_label = Label(building,image=op,width = 300,height=180,border=0,bg='black').place(x=60,y=40)
        op_label.image = op
        
        Parking_B = Button(building,text='Parking B',pady=1,width=10,fg='black',border=0,bg='#FFFFEB',font=('Microsoft Yahei UI Light',14,))
        Parking_B.place(x=650,y=220)
        
        Parking_C = Button(building,text='Parking C',pady=1,width=10,fg='black',border=0,bg='#FFFFEB',font=('Microsoft Yahei UI Light',14,))
        Parking_C.place(x=140,y=420)
        
        Parking_D = Button(building,text='Parking D',pady=1,width=10,fg='black',border=0,bg='#FFFFEB',font=('Microsoft Yahei UI Light',14,))
        Parking_D.place(x=650,y=420)

    
    elif vehicleno!= 'MH34BK2578' and phoneno!= '7028067585' and gmailac!= 'sanjay.22210866@viit.ac.in' :
        messagebox.showerror("Invalid"," Invalid Vehicle No")

img = PhotoImage(file='parking1.png')
Label(root,image=img,border=0,bg='white').place(x=-350,y=-265)

frame=Frame(root,width=400,height=390,bg='#fff')
frame.place(x=450,y=80)

heading=Label(frame,text='Welcome to Parkin!',fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',20,))
heading.place(x=120, y=5)

ok=Button(frame,text='Book',pady=1,width=25,fg='white',border=0,bg='#57a1f8',font=('Microsoft Yahei UI Light',14,),command=book)
ok.place(x=115,y=250)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Vehicle Number ')


user=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
user.place(x=110,y=67)

# This input will be given by the parking coordinator

user.insert(0,'Vehicle Number')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=110,y=90)

def on_enter(e):
    Phone.delete(0,'end')
def on_leave(e):
    if Phone.get()=='':
        Phone.insert(0,'Phone No.')

Phone=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
Phone.place(x=110,y=134)
Phone.insert(0,'Phone No.')
Phone.bind("<FocusIn>",on_enter)
Phone.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=110,y=160)

def on_enter(e):
    gmail.delete(0,'end')
def on_leave(e):
    if gmail.get()=='':
        gmail.insert(0,'Enter your Gmail')

gmail=Entry(frame,width=25,fg="black",border=0,bg='white',font=('Microsoft Yahei UI Light',13))
gmail.place(x=110,y=200)
gmail.insert(0,'Enter your Gmail ')
gmail.bind("<FocusIn>",on_enter)
gmail.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=110,y=230)

root.mainloop()

