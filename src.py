import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import mysql.connector as sqlpj

root=tk.Tk()
def get(entry):
    global a
    a = entry.get()
def change(label):
    global a
    label['text']=a
a=""

root.title("comedy shows")
root.geometry("800x600")
root.configure()
root.resizable(height = False, width = False)

# font style for headings buttons and all
heading = tkfont.Font(family="Arial",size=40)
text = tkfont.Font(family="Arial",size=20)
btntext=tkfont.Font(family="Arial",size=14)

# god frame contains all other frames
god=tk.Frame(master = root)
god.pack(side = "top", fill="both",expand=True)

#first slide
intro1 = tk.Frame(master = god )
intro1.grid(row=0,column=0,sticky="nsew")
c=tk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\white8.png")
l1=tk.Label(root,image=c).pack()
title1 = tk.Label(master=intro1, bg="black", fg="white"
                 , text="Welcome To Event Management System"
                 , width=35,
                 font=text)
title1.place(x=120, y= 200)

proceed_btn=tk.Button(master=intro1,bg="black",
                    fg="white",
                    width=20,
                    text="click to proceed",
                    font=btntext,
                    command= lambda: intro.tkraise())
proceed_btn.place(x=280,y=260)
#view ticket and all
intro = tk.Frame(master = god , bg = "white" )
intro.grid(row=0,column=0,sticky="nsew")

#intro title
title=tk.Label(master=intro,bg="white",fg="black"
               ,text="Stand Up Shows"
               ,width=26,
               font= heading)
title.place(x=0,y=50)

#Book show button
btn_shows=tk.Button(master=intro,bg="black",
                    fg="white",
                    width=20,
                    text="Book Shows",
                    font=btntext,
                    command= lambda: show.tkraise())
btn_shows.place(x=280,y=150)

btn_view=tk.Button(master=intro,bg="black",
                    fg="white",
                    width=20,
                    text="View Ticket Status",
                    font=btntext,
                    command= lambda: view_ticket_status.tkraise())
btn_view.place(x=280,y=200)

btn_exit=tk.Button(master=intro,bg="black",
                    fg="white",
                    width=20,
                    text="Exit",
                    font=btntext,
                    command= lambda: exit())
btn_exit.place(x=280,y=250)

#show frame contains all the show buttons
show=tk.Frame(master= god , bg="white")
show.grid(row=0,column=0,sticky="nsew")

show_date=tk.Label(master=show,bg="white",fg="black"
               ,text="Shows Available"
               ,width=15,
               font= heading)
show_date.place(x=150,y=10)

show_a=tk.Label(master=show,bg="white",fg="black"
               ,text="Select the show of your choice:"
               ,width=26,
               font= btntext)
show_a.place(x=250,y=80)



var = tk.IntVar()
R1 = tk.Radiobutton(master=show,indicator=0, text="6th March,2022-Sunday \n Standup artist: Anubhav Singh \n Time: 5:00 pm-6:30 pm", variable=var, value=1,width=38,
                  command=lambda: clicked(var.get()))
R1.place(x=250,y=120)
R2 = tk.Radiobutton(master=show, indicator=0,text="13th March,2022-Sunday \n Standup artist: Aakash Gupta \n Time: 7:00 pm-8:30 pm", variable=var, value=2,width=38,
                  command=lambda: clicked(var.get()))
R2.place(x=250,y=180)
R3 = tk.Radiobutton(master=show,indicator=0, text="20th March,2022-Sunday \n Standup artist: Yash Rathi \n Time: 6:00pm-7:30 pm", variable=var, value=3,width=38,
                  command=lambda: clicked(var.get()))
R3.place(x=250,y=240)
R4 = tk.Radiobutton(master=show,indicator=0, text="27th March,2022-Sunday \n Standup artist: Atul Sharma \n Time: 4:00 pm-5:30 pm", variable=var, value=4,width=38,
                  command=lambda: [clicked(var.get()),R4.deselect()])
R4.place(x=250,y=300)
label = tk.Label(root)
label.pack()

def clicked(value):
    if value== 3 :
        return(show_3.tkraise())
    else:
        return(details.tkraise())

#show_3
show_3=tk.Frame(master= god , bg="white")
show_3.grid(row=0,column=0,sticky="nsew")

show_3_label= tk.Label(master=show_3, bg="black", fg="white"
                 , text="This show is full!!"
                 , width=26,
                 font=text)
show_3_label.place(x=200, y=150)


back_show_3=tk.Button(master=show_3,bg="black",
                    fg="white",
                    width=20,
                    text="back",
                    font=btntext,
                    command= lambda: show.tkraise())
back_show_3.place(x=250,y=250)


#fix this button
back_show=tk.Button(master=show,bg="black",
                    fg="white",
                    width=15,
                    text="back",
                    font=btntext,
                    command= lambda: intro.tkraise())
back_show.place(x=50,y=350)
#personal details frame for booking the ticket
details=tk.Frame(master= god , bg="white")
details.grid(row=0,column=0,sticky="nsew")

fill_label=tk.Label(master=details,bg="black",fg="white",
               text="Fill Your Details"
               ,width=26,
               font= text)
fill_label.grid(row = 0, columnspan = 2, sticky = "ew")

label_book_heading=tk.Label(master=details,bg="white",fg="black"
               ,text="Book Your Ticket"
               ,width=26,
               font= heading)
label_book_heading.grid(row = 0, column = 0,columnspan=2, sticky = "ew")

label_book_name=tk.Label(master=details,bg="white",fg="black"
               ,text="Name"
               ,width=15,
               font=text)
label_book_name.grid(row = 1, column = 0,padx=(0,30), sticky = "e")
entry_book_name=tk.Entry(master=details,bg="black",fg="white",
                         width=20,
                         highlightbackground="white",
                         highlightcolor="white",

                         insertbackground="white",
                         font=text)
entry_book_name.grid(row=1, column=1,sticky="w")

label_book_email=tk.Label(master=details,bg="white",fg="black"
               ,text="Email"
               ,width=15,
               font=text)
label_book_email.grid(row = 2, column = 0,padx=(0,30), sticky = "e")
entry_book_email=tk.Entry(master=details,bg="black",fg="white",
                         width=20,
                         highlightbackground="white",
                         highlightcolor="white",

                         insertbackground="white",
                         font=text)
entry_book_email.grid(row=2, column=1,sticky="w")

label_book_num=tk.Label(master=details,bg="white",fg="black"
               ,text="Phone Number"
               ,width=15,
               font=text)
label_book_num.grid(row = 3, column = 0,padx=(0,30) , sticky = "e")
entry_book_num=tk.Entry(master=details,bg="black",fg="white",
                         width=20,
                         highlightbackground="white",
                         highlightcolor="white",

                         insertbackground="white",
                         font=text)
entry_book_num.grid(row=3, column=1,sticky="w")
def error(x):
    if x=="":
        return False
    else:
        return True 
label_book_invalid=tk.Label(master=details,bg="white",fg="black"
               ,text=""
               ,width=10,
               font=text)
label_book_invalid.place(x=300, y=330)           
def invalid():
    c=1
    for i in [error(entry_book_num.get()),error(entry_book_email.get()),error(entry_book_name.get())]:
        if i==False:
            c=0
    if c==0:        
        label_book_invalid["text"]="Invalid"
    else:
        for i in entry_book_num.get():
            if i.isdigit():
                c=1
            else:
                c=0
        if c==1:
            price.tkraise()
            R1_.select()
        else:
            label_book_invalid["text"]="Invalid"    

        

proceed_details=tk.Button(master=details,bg="black",
                    fg="white",
                    width=20,
                    text="click to proceed",
                    font=btntext,
                    command= invalid)
proceed_details.place(x=500,y=330)

back_details=tk.Button(master=details,bg="black",
                    fg="white",
                    width=20,
                    text="back",
                    font=btntext,
                    command= lambda: show.tkraise())
back_details.place(x=55,y=330)


#ticket details frame starts here
price=tk.Frame(master= god , bg="white")
price.grid(row=0,column=0,sticky="nsew")

ticket_detail_label=tk.Label(master=price,bg="white",fg="black"
               ,text="Ticket Details"
               ,width=10,
               font= heading)
ticket_detail_label.place(x=250,y=5)


duration_label=tk.Label(master=price,bg="white",fg="black"
               ,text="Duration:90 minutes"
               ,width=20,
               font= text)
duration_label.place(x=250,y=90)

price_label=tk.Label(master=price,fg="black",bg="white"
               ,text="Prices:"
               ,width=10,
               font= text)
price_label.place(x=250,y=130)

price_label=tk.Label(master=price,bg="white",fg="black"
               ,text="how many tickets do you want to buy?"
               ,width=30,
               font= btntext)
price_label.place(x=75,y=280)

def set():
   label.config(text = "selection")

var1 = tk.IntVar()
R1_ = tk.Radiobutton(master=price, text="1.Regular-Rs.500", variable=var1, value=1,width=20,
                  command=set)
R1_.place(x=300,y=170)
R2_ = tk.Radiobutton(master=price, text="2.Gold-Rs.800", variable=var1, value=2,width=20,
                  command=set)
R2_.place(x=300,y=205)
R3_ = tk.Radiobutton(master=price, text="3.Premium-Rs.1000", variable=var1, value=3,width=20,
                  command=set)
R3_.place(x=300,y=240)
label =tk.Label(root)
label.pack()
numbers_ticket=tk.Entry(master=price,bg="white",fg="black",
                         width=8,
                         highlightbackground="black",
                         highlightcolor="black",

                         insertbackground="black",
                         font=text)
numbers_ticket.place(x=400,y=278)

def books(var):
    conn = sqlpj.connect(host = "localhost", user = "root", passwd = "mysql", database = "ticket")
    c = conn.cursor()
    name=entry_book_name.get()
    email=entry_book_email.get()
    num=entry_book_num.get()
    if var1.get() == 1:
        type = "Regular"
    elif var1.get() == 2:
        type = "Gold"
    elif var1.get() == 3:
        type = "Premium"
    qty = numbers_ticket.get()
    print(name,email,int(num),type, int(qty))
    if var==1:
        
        c.execute("INSERT INTO 6thmarch VALUES('{}','{}','{}','{}','{}')".format(name,email,num,type, int(qty)))
        conn.commit()
    elif var==2:
        c.execute("INSERT INTO 13thmarch VALUES ('{}','{}','{}','{}','{}')".format(name, email, num, type, int(qty)))
        conn.commit()
    elif var==4:
        c.execute("INSERT INTO 27thmarch VALUES ('{}','{}','{}','{}','{}')".format(name, email, num, type, int(qty)))
        conn.commit()
    else:
        intro.tkraise()
    last_show.tkraise()
    if var1.get() == 1:
        price_1 = 500*int(qty)
    elif var1.get() == 2:
        price_1 = 800*int(qty)
    elif var1.get() == 3:
        price_1 =1000*int(qty)
    paid_label1=tk.Label(master=last_show,bg="black",fg="white"
               ,text=price_1
               ,width=7,
               font= text)
    paid_label1.place(x=450,y=60)    
    entry_book_name.delete(0,"end")
    entry_book_email.delete(0,"end")
    entry_book_num.delete(0,"end")
    numbers_ticket.delete(0,"end")
proceed_price=tk.Button(master=price,bg="black",
                    fg="white",
                    width=20,
                    text="click to proceed",
                    font=btntext,
                    command= lambda: books(var.get()))
proceed_price.place(x=500,y=340)

back_price=tk.Button(master=price,bg="black",
                    fg="white",
                    width=15,
                    text="back",
                    font=btntext,
                    command= lambda: details.tkraise())
back_price.place(x=80,y=340)
#last frame of show starts here
last_show=tk.Frame(master= god , bg="white")
last_show.grid(row=0,column=0,sticky="nsew")

paid_label=tk.Label(master=last_show,bg="white",fg="black"
               ,text="Amount to be paid:"
               ,width=26,
               font= text)
paid_label.place(x=40,y=60)

code_label=tk.Label(master=last_show,bg="white",fg="black"
               ,text="Ticket Code:"
               ,width=20,
               font= text)
code_label.place(x=80,y=100)

thanks_label=tk.Label(master=last_show,bg="white",fg="black"
               ,text="All info and SMS regarding the show you have booked \n will be sent to this contact no. :"
               ,width=60,
               font= btntext)
thanks_label.place(x=80,y=250)

finish=tk.Button(master=last_show,bg="black",
                    fg="white",
                    width=28,
                    text="Finish",
                    font=btntext,
                    command= lambda: intro1.tkraise())
finish.place(x=240,y=310)

#view ticket status frame starts here

def view(var):
    if var == 1:
        table = '6thmarch'
        x="6th March"
        y="5:00 pm - 6:30 pm"

    elif var == 2:
        table = '13thmarch'
        x="13th March" 
        y="7:00 pm - 8:30 pm"
    elif var == 4:
        table = '27thmarch'
        x="27th March" 
        y="4:00 pm - 5:30 pm"
    name = entry_book_name1.get()
    number = entry_book_num1.get()
    conn = sqlpj.connect(host = "localhost", user = "root", passwd = "mysql", database = "ticket")
    c = conn.cursor()
    c.execute("SELECT * FROM {} WHERE name = '{}' AND phone_number = '{}'".format(table, name, number))
    l = c.fetchall()
    if len(l)==0:
        entry_book_name1.delete(0,"end")
        entry_book_num1.delete(0,"end")
        case2.tkraise()
    else:
        print_l=""
        for i in l[0]:
            print_l += str(i) + "\n"
        ticket_info_labe2=tk.Label(master=case1  ,bg="white",fg="black"
                ,text= print_l
                ,width=15,
                
                font=text)
        ticket_info_labe2.grid(row=1,column=1,sticky='e',columnspan=1,padx=(0,0),pady=(13,0))
        ticket_info_labe3=tk.Label(master=case1  ,bg="white",fg="black"
                ,text= x + "\n" + y
                ,width=15,
                
                font=text)
        ticket_info_labe3.grid(row=2,column=1,sticky='e',columnspan=1,padx=(0,0),)
        entry_book_name1.delete(0,"end")
        entry_book_num1.delete(0,"end")
        case1.tkraise()   

view_ticket_status=tk.Frame(master= god , bg="white")
view_ticket_status.grid(row=0,column=0,sticky="nsew")

view_label=tk.Label(master=view_ticket_status,bg="white",fg="black"
               ,text="Please enter the following details to view your ticket:"
               ,width=40,
               font= btntext)
view_label.grid(row=1, column=0, columnspan = 4, pady = 50, sticky = 'ew')


label_book_name1=tk.Label(master=view_ticket_status,bg="white",fg="black"
               ,text="Name:"
               ,width=15,
               font=text)
label_book_name1.grid(row  = 2, column = 0, columnspan = 2, padx = (0,10), pady = (0, 25), sticky = "e")
entry_book_name1=tk.Entry(master=view_ticket_status,bg="black",fg="white",
                         width=20,
                         highlightbackground="white",
                         highlightcolor="white",

                         insertbackground="white",
                         font=text)
entry_book_name1.grid(row  = 2, column = 2, columnspan = 2, padx = (10,0), pady = (0, 25), sticky = "w")

label_book_num1=tk.Label(master=view_ticket_status,bg="white",fg="black"
               ,text="Phone Number:"
               ,width=15,
               font=text)
label_book_num1.grid(row  = 3, column = 0, columnspan = 2, padx = (0,10), pady = (25, 25), sticky = "e")
entry_book_num1=tk.Entry(master=view_ticket_status,bg="black",fg="white",
                         width=20,
                         highlightbackground="white",
                         highlightcolor="white",
                         insertbackground="white",
                         font=text)
entry_book_num1.grid(row  = 3, column = 2, columnspan = 2, padx = (10,0), pady = (25, 25), sticky = "w")

var3 = tk.IntVar()
R1 = tk.Radiobutton(master=view_ticket_status, text="6th March,2022-Sunday", variable=var3, value=1,width=20)
R1.grid(row  = 4, column = 0, padx = (50, 5), pady = (25, 25))
R2 = tk.Radiobutton(master=view_ticket_status, text="13th March,2022-Sunday", variable=var3, value=2,width=20)
R2.grid(row  = 4, column = 1, padx = (5), pady = (25, 25))
R3 = tk.Radiobutton(master=view_ticket_status, text="20th March,2022-Sunday", variable=var3, value=3,width=20)
R3.grid(row  = 4, column = 2, padx = (5), pady = (25, 25))
R4 = tk.Radiobutton(master=view_ticket_status, text="27th March,2022-Sunday", variable=var3, value=4,width=20)
R4.grid(row  = 4, column = 3, padx = (5, 0), pady = (25, 25))


next=tk.Button(master=view_ticket_status,bg="black",
                    fg="white",
                    width=20,
                    text="click to proceed",
                    font=btntext,
                    command = lambda: [view(var3.get())])
next.grid(row  = 5, column = 3, columnspan = 2, padx = (0,10), sticky = "e")

back_view_status=tk.Button(master=view_ticket_status,bg="black",
                    fg="white",
                    width=20,
                    text="back",
                    font=btntext,
                    command= lambda: intro.tkraise())
back_view_status.grid(row  = 5, column = 0, columnspan = 2, padx = (10,0), sticky = "w")

#case1 frame starts here
case1=tk.Frame(master= god , bg="white")
case1.grid(row=0,column=0,sticky="nsew")

ticket_info_label1=tk.Label(master=case1  ,bg="white",fg="black"
             ,text="TICKET INFO"
             
             ,width=20,
             font=text)
ticket_info_label1.grid(row=0,columnspan=2,sticky='Ew', pady=(10))

ticket_info_label2=tk.Label(master=case1  ,bg="white",fg="black"
             ,text="Name: \n Email ID: \n Phone Number: \n Ticket Type: \n Number of tickets:  "
             
             ,width=15,
             font=text)
ticket_info_label2.grid(row=1,column=0,columnspan=1,sticky='w',padx=(0,0))

ticket_info_label3=tk.Label(master=case1  ,bg="white",fg="black"
             ,text="Date: \n Time: "
             
             ,width=15,
             font=text)
ticket_info_label3.grid(row=2,column=0,columnspan=1,sticky='w',padx=(0,5))

ticket_info_label4=tk.Label(master=case1  ,bg="white",fg="black"
             ,text="Duration:"
             
             ,width=15,
             font=text)
ticket_info_label4.grid(row=3,column=0,columnspan=1,sticky='w',padx=(0,5))

ticket_info_labe4=tk.Label(master=case1  ,bg="white",fg="black"
             ,text="90 Minutes"
             
             ,width=15,
             font=text)
ticket_info_labe4.grid(row=3,column=1,columnspan=1)

back_case1=tk.Button(master=case1,bg="black",
                    fg="white",
                    width=20,
                    text="back",
                    font=btntext,
                    command= lambda: view_ticket_status.tkraise())
back_case1.grid(row=4,column=0,pady=(20))

#case2
case2=tk.Frame(master= god , bg="white")
case2.grid(row=0,column=0,sticky="nsew")

invalid_label=tk.Label(master=case2  ,bg="white",fg="black"
             ,text="Invalid phone number entered \n Please book tickets! "
             ,width=20,
             font=text)
invalid_label.grid(row=1,column=1,sticky='n')

back_case2=tk.Button(master=case2,bg="black",
                    fg="white",
                    width=20,
                    text="back",
                    font=btntext,
                    command= lambda:view_ticket_status.tkraise())
back_case2.grid(row=5,column=0,pady=(20))





intro1.tkraise()

root.mainloop()
