import tkinter as tk

def Submit():
    name=entry1.get()
    print("Name : ",name)
    radio1=var.get()
    if radio1==1:
        print("Gender : Male")
    elif radio1==2:
        print("Gender : Female")
    else:   
        print("Gender : Not Selected")

    radio2=subject.get()
    if radio2==1:
        print("Best Subject : Python")  
    elif radio2==2:
        print("Best Subject : Java")
    else:
        print("Best Subject : Not Selected")

    mobile=entry2.get()
    print("Mobile number: ",mobile)

    address=entry3.get()
    print("Address: ",address)

root=tk.Tk()
root.title("My Gui")
root.geometry("800x600")

label1=tk.Label(root,text="IT Preneur",font=("Arial",20))
label1.grid(row=0,column=1)

label2=tk.Label(root,text="Name : ",font=("Arial",16))
label2.grid(row=1,column=0)

entry1=tk.Entry(root,font=("Arial",16))
entry1.grid(row=1,column=1)

lebal3=tk.Label(root,text="Gender: ",font=("Arial",16))
lebal3.grid(row=3,column=0)

var=tk.IntVar()

radio1=tk.Radiobutton(root,text="Male: ",value=1,variable=var)
radio1.grid(row=3,column=2)

radio2=tk.Radiobutton(root,text="Female",value=2,variable=var)
radio2.grid(row=4,column=2)

subject=tk.IntVar()

label4=tk.Label(root,text="Best Subject ",font=("Arial",16))
label4.grid(row=5,column=0)

radio3=tk.Radiobutton(root,text="Python",value=1,variable=subject)
radio3.grid(row=5,column=2)

radio4=tk.Radiobutton(root,text="Java",value=2,variable=subject)
radio4.grid(row=6,column=2)


mobile=tk.Label(root,text="Mobile no : ",font=("Arial",16))
mobile.grid(row=7,column=0)

entry2=tk.Entry(root,font=("Arial",16))
entry2.grid(row=7,column=1)

address=tk.Label(root,text="Address : ",font=("Arial",16))
address.grid(row=8,column=0)

entry3=tk.Entry(root,font=("Arial",16))
entry3.grid(row=8,column=1)

button1=tk.Button(root,text="Submit",command=Submit,font=("Arial",16))
button1.grid(row=9,column=1)

root.mainloop()