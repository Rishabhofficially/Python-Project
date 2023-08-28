from tkinter import*
from tkinter import messagebox
screen=Tk()
screen.title("Regstration Form.")
screen.geometry("500x400")

def Register():
    
     Name=Name_info.get()
     Age=age_info.get()
     Phone=phone_info.get()
     Email=email_info.get()
     
     if Name=="":
         messagebox.showerror("Error","please enter your Name." )
     elif Age=="":
         messagebox.showerror("Error","please enter your Age." )
     elif Phone=="":
         messagebox.showerror("Error","please enter your phone no." )
     elif Email=="":
         messagebox.showerror("Error","please enter your Email." )
     else:
         Label(screen,text="Register sucessfully",font="20",fg="green").place(x=185,y=310)
         
         
     with open(Name+".txt","w")as f:
         f.write("Name: "+Name+"\n")
         f.write("Age: "+Age+"\n")
         f.write("Phone no.: "+Phone+"\n")
         f.write("Email ID: "+Email+"\n")
def Clear():
    Name_Entry.delete(0,END)
    Age_Entry.delete(0,END)
    Phone_Entry.delete(0,END)
    Email_Entry.delete(0,END)
# lable
Label(screen,text="Rergstration form",font="arial 20 bold",bg="green",fg="gold").pack(fill="both")

Label(screen,text="Name",font="20").place(x=30,y=60)
Label(screen,text="Age",font="20").place(x=30,y=110)
Label(screen,text="phone",font="20").place(x=30,y=160)
Label(screen,text="Email",font="20").place(x=30,y=210)

#Entry
Name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()

Name_Entry=Entry(screen,font="10",textvariable=Name_info)
Name_Entry.place(x=150,y=60)

Age_Entry=Entry(screen,font="10",textvariable=age_info)
Age_Entry.place(x=150,y=110)

Phone_Entry=Entry(screen,font="10",textvariable=phone_info)
Phone_Entry.place(x=150,y=160)

Email_Entry=Entry(screen,font="10",textvariable=email_info)
Email_Entry.place(x=150,y=210)

#Button
Button(screen,text="Register", font="20",command=Register).place(x=185,y=255)
Button(screen,text="Clear", font="20",command=Clear).place(x=300,y=255)
mailloop()






