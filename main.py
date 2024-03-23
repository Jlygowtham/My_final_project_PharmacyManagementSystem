from tkinter import *
from tkinter import messagebox, LabelFrame
from tkinter.ttk import Combobox,Treeview
import mysql.connector
import tkcalendar
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def AddMedicine():
    code=codeEntry.get()
    name=nameEntry.get()
    disease=disease_combo.get()
    price=priceEntry.get()
    
    
    try:
       mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="pharamacy")
       mycursor=mysqldb.cursor()
    
        # Create the Medicine table if it doesn't exist and insert data
       mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Medicine (
                id INT AUTO_INCREMENT PRIMARY KEY,
                code INT,
                name VARCHAR(255),
                disease VARCHAR(255),
                price DECIMAL(10, 2)
            )
        """)
       if code!='' and name!='' and disease!='' and price!='':
            sql = "INSERT INTO  Medicine (code,name,disease,price) VALUES (%s, %s, %s, %s)"
            val = (code,name,disease,price)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("information", "Medicine inserted successfully...")

            codeEntry.delete(0, END)
            nameEntry.delete(0, END)
            disease_combo.set('')
            priceEntry.delete(0, END)
        
       else:
           messagebox.showinfo("Warning", "Enter the Details")


    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


# Function 
def new_medicine():
    global codeEntry,nameEntry,priceEntry,disease_combo
    medicine=Toplevel()
    medicine.geometry('900x600')
    medicine.config(bg='#2d283e')
    medicine_font=('Helvetica', 35, 'bold')
    fore='#d1d7e0'
    back="#2d283e"
    
    Label(medicine,text='New Medicine',font=medicine_font,fg=fore,bg=back).place(x=250, y=20)

    mf=Frame(medicine, bg="#564f6f")
    mf.place(x=220, y=150)

    medicine_code = Label(mf, text="Medicine code", font=('Arial bold', 15))
    Medicine_Name = Label(mf, text="Medicine Name", font=('Arial bold', 15))
    disease_label=Label(mf, text="Disease", font=('Arial bold', 15))
    price_label = Label(mf, text="Price", font=('Arial bold', 15))

    medicine_code.grid(row=1, column=0, padx=10, pady=10)
    Medicine_Name.grid(row=2, column=0, padx=10, pady=10)
    disease_label.grid(row=3,column=0,padx=10, pady=10)
    price_label.grid(row=4, column=0, padx=10, pady=10)

    codeEntry = Entry(mf, width=25, bd=5, font=('Arial bold', 15))
    nameEntry = Entry(mf, width=25, bd=5, font=('Arial bold', 15))
    priceEntry = Entry(mf, width=25, bd=5, font=('Arial bold', 15))

    codeEntry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
    nameEntry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
    priceEntry.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
    
    disease_combo = Combobox(mf, values=['Heart', "Cold", "Fever"], font="Helvetica 12", state='r', width=14)
    disease_combo.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
    disease_combo.set('Select a Disease')


    buttonEnter = Button(
        mf, text="Add", padx=5, pady=5, width=5,
        bd=3, font=('Arial', 15), bg=back,fg=fore,command=AddMedicine)
    buttonEnter.grid(row=5, column=1, columnspan=1)

    buttonEnter = Button(
        mf, text="Update", padx=5, pady=5, width=5,
        bd=3, font=('Arial', 15), bg=back,fg=fore)
    buttonEnter.grid(row=5, column=2, columnspan=1)

    buttonEnter = Button(
        mf, text="Clear", padx=5, pady=5, width=5,
        bd=3, font=('Arial', 15), bg=back,fg=fore)
    buttonEnter.grid(row=5, column=3, columnspan=1)

def main_page():
    app.destroy()
    success = Tk()
    app_width = success.winfo_screenwidth()
    app_height = success.winfo_screenheight()
    success.geometry("%dx%d+0+0" % (app_width, app_height))
    success.config(bg='#2d283e')

    # --Head section--
    Label(success, text="Pharmacy Management System", font=('Helvetica', 45, 'bold'), fg='#d1d7e0', bg="#2d283e").place(x=120, y=20)
    Label(success, text="Add New Medicine", font=('Arial', 15, 'bold'), fg='#d1d7e0', bg="#2d283e").place(x=1200, y=80)

    image = PhotoImage(file="assets/plus.png").subsample(6, 6)

    image_label = Label(success,bg="#2d283e", image=image)
    image_label.place(x=1250,y=10)

    image_label.bind("<Button-1>", lambda event: new_medicine())

    # --End Head section--
    

    # Body section

    # --Customer_detail Frame--
    
    lf=LabelFrame(success,text="Customer Data",width=600, height=650, bg="#564f6f",font="10").place(x=20, y=120)


    # Label
    Label(lf, text="Name", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=40, y=180)
    Label(lf, text="Age", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=40, y=240)
    Label(lf, text="Gender", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=40, y=360)
    Label(lf, text="Date", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=40, y=480)
    Label(lf, text="City", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=40, y=600)

    # Entry
    nameValue = StringVar()
    ageValue = StringVar()
    DateValue = StringVar()
    cityValue = StringVar()

    nameEntry = Entry(lf, textvariable=nameValue, width=20, bd=2, font=10)
    ageEntry = Entry(lf, textvariable=ageValue, width=20, bd=2, font=10)
    DateEntry = tkcalendar.DateEntry(lf, textvariable=DateValue, width=10, bd=2, font=8, date_pattern='dd-mm-yyyy')
    cityEntry = Entry(lf, textvariable=cityValue, width=10, bd=2, font=10)

    # Gender
    gender_combo = Combobox(lf, values=['Male', "Female", "Others"], font="Helvetica 12", state='r', width=14)
    gender_combo.place(x=120, y=360)
    gender_combo.set('Male')

    nameEntry.place(x=120, y=180)
    ageEntry.place(x=120, y=240)
    DateEntry.place(x=120, y=480)
    cityEntry.place(x=120, y=600)
    
    # --End Customer_detail Frame--

    # --Medicine Frame--

    rf=LabelFrame(success,text="Medicine Details",width=850, height=300, bg="#564f6f",font="10").place(x=640, y=120)
    

    # Label
    Label(rf, text="Tablet Code", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=690, y=150)
    Label(rf, text="Tablet Name", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=1055, y=150)
    Label(rf, text="Quantity", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=690, y=240)
    Label(rf, text="Price", font=('Helvetica', 12, 'bold'), bg='#092635', fg="#9EC8B9").place(x=1055, y=240)
    Button(rf,text="Add",font=('Helvetica',15,'bold'),bg='#2d283e',fg="#d1d7e0",width=12,height=2).place(x=750,y=350)
    Button(rf,text="Update",font=('Helvetica',15,'bold'),bg='#2d283e',fg="#d1d7e0",width=12,height=2).place(x=950,y=350)
    Button(rf,text="Clear",font=('Helvetica',15,'bold'),bg='#2d283e',fg="#d1d7e0",width=12,height=2).place(x=1150,y=350)

    # Entry
    CodeValue = StringVar()
    TabletValue = StringVar()
    QuanValue = StringVar()
    priceValue = StringVar()

    CodeEntry = Entry(rf, textvariable=CodeValue, width=20, bd=2, font=10)
    TabletEntry = Entry(rf, textvariable=TabletValue, width=20, bd=2, font=10)
    QuanEntry = Entry(rf, textvariable=QuanValue, width=20, bd=2, font=10)
    priceEntry = Entry(rf, textvariable=priceValue, width=20, bd=2, font=10)

    CodeEntry.place(x=820, y=150)
    TabletEntry.place(x=1180, y=150)
    QuanEntry.place(x=820, y=240)
    priceEntry.place(x=1180, y=240)
    
    
    # --En₫ Medicine Frame--

    # --Treeview Frame--
    tf = LabelFrame(success,text="Tablet Details", width=850, height=340, bg="#564f6f")
    tf.place(x=640, y=430)

    cols = ('Code', 'Tablet Name', 'Total')
    tree = Treeview(tf, columns=cols, show='headings',height=13)
    for col in cols:
        tree.heading(col, text=col)
    tree.pack(fill='both', expand=True, padx=15, pady=15)

    # --End Treeview Frame--
    
    success.mainloop()


def login():
    user_creditals=["Gowtham","12345"]
    if userValue.get()==user_creditals[0] and passValue.get()==user_creditals[1]:
        main_page()
    else:
        if userValue.get()=='' and passValue.get()=='':
            messagebox.showinfo("Warning","Enter Username and Password")
        else:
            messagebox.showinfo("Wrong Credential","Invalid Username and Password")

def clear():
    userValue.set("")
    passValue.set("")

app = Tk()
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (app_width, app_height))
app.config(bg='#2d283e')
app.title('Pharmacy Management system')

# ----Login form----

loginFrame=Frame(app,width=1200,height=600,bg="#564f6f").place(x=200,y=100)

Label(loginFrame,text="Pharmacy Management System",font=('Helvetica', 45,'bold'),fg='#d1d7e0',bg= "#564f6f").place(x=380,y=120)


Label(loginFrame,text="Log In",font=('Helvetica', 32,'bold'),fg='#d1d7e0',bg="#564f6f").place(x=730,y=245)
Label(loginFrame,text="UserName",font=('Helvetica', 22,'bold'),fg='#d1d7e0',bg="#564f6f").place(x=530,y=340)
Label(loginFrame,text="Password",font=('Helvetica', 22,'bold'),fg='#d1d7e0',bg="#564f6f").place(x=530,y=445)

# Entry
userValue=StringVar()
passValue=StringVar()

userEntry=Entry(loginFrame,textvariable=userValue,width=20,bd=1,font=10,highlightthickness=3,highlightcolor='blue').place(x=730,y=345)
passEntry=Entry(loginFrame,textvariable=passValue,width=20,bd=1,font=10,highlightthickness=3,highlightcolor='blue').place(x=730, y=450)

Button(loginFrame,text="Login",font=('Helvetica', 15,'bold'),bg='#2d283e',fg="#d1d7e0",width=12,height=2,command=login).place(x=560,y=550)
Button(loginFrame,text="Clear",font=('Helvetica',15,'bold'),bg='#2d283e',fg="#d1d7e0",width=12,height=2,command=clear).place(x=760,y=550)
Button(loginFrame,text='main_page',command=main_page).place(x=960,y=550)
# ---- End Login Form ----

app.mainloop()