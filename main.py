from tkinter import *
from tkinter import messagebox, LabelFrame
from tkinter.ttk import Combobox,Treeview
from Database_Connection import connection
import tkcalendar
from tkinter import ttk
import random
from PIL import ImageTk,Image


# New-medicine Functions
    
def AddMedicine():
    code=codeEntry.get()
    name=nameEntry.get()
    disease=disease_combo.get()
    price=priceEntry.get()

    mycursor,mysqldb=connection()

    mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Medicine (
                code VARCHAR(50) PRIMARY KEY,
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

 
def UpdateMedicine():
    code=codeEntry.get()
    name=nameEntry.get()
    disease=disease_combo.get()
    price=priceEntry.get()

    mycursor,mysqldb=connection()

    updateQuery="""
           UPDATE Medicine
           SET name = %s,disease=%s,price=%s
           WHERE code =%s
        """
    val=(name,disease,price,code)

    mycursor.execute(updateQuery,val)
    mysqldb.commit()
    messagebox.showinfo("information", "Record Updated successfully...") 
    
    codeEntry.delete(0, END)
    nameEntry.delete(0, END)
    disease_combo.set('')
    priceEntry.delete(0, END)

def RemoveMedicine():
    code=codeEntry.get()
    mycursor,mysqldb=connection()

    deleteQuery="Delete from Medicine where code=%s"
    val=(code,)

    mycursor.execute(deleteQuery,val)
    mysqldb.commit()
    messagebox.showinfo("information", "Record Deleted successfully...") 

    codeEntry.delete(0, END)
    nameEntry.delete(0, END)
    disease_combo.set('')
    priceEntry.delete(0, END)
    codeEntry.focus_set()

def ClearMedicine():
    codeEntry.delete(0, END)
    nameEntry.delete(0, END)
    disease_combo.set('Select a Disease')
    priceEntry.delete(0, END)



def new_medicine():
    global codeEntry,nameEntry,priceEntry,disease_combo
    medicine=Toplevel()
    iconImg=PhotoImage(file="D:\\MCA_MIni_Final_project\\Final Year project\\Pharmacy Mangement System code\\assets\\icon.png")
    medicine.iconphoto(False,iconImg)
    medicine.geometry('900x600')
    medicine.config(bg=Background)
    medicine.title('New Medicine')
    medicine_font=(fontname, 45, 'bold')

    
    Label(medicine,text='New Medicine',font=medicine_font,fg=foreground,bg=Background).place(x=290, y=50)

    mf=LabelFrame(medicine,highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground,bd=0,width=600,fg=foreground, height=320, bg=Background)
    mf.place(x=170, y=150)

    Label(mf, text="Medicine code", font=(fontname,19,'bold'),bg=Background, fg=foreground).place(x=40,y=30)
    Label(mf, text="Medicine Name", font=(fontname,19,'bold'),bg=Background, fg=foreground).place(x=40,y=100)
    Label(mf, text="Disease", font=(fontname,19,'bold'),bg=Background, fg=foreground).place(x=40,y=170)
    Label(mf, text="Price", font=(fontname,19,'bold'),bg=Background, fg=foreground).place(x=40,y=240)

    codeEntry = Entry(mf,font=10,highlightthickness=2,highlightcolor=Background, width=20, bd=2)
    nameEntry = Entry(mf,  width=20,bd=2,font=10,highlightthickness=2,highlightcolor=Background)
    priceEntry = Entry(mf, width=20,bd=2,font=10,highlightthickness=2,highlightcolor=Background)

    codeEntry.place(x=260,y=30)
    nameEntry.place(x=260,y=100)
    priceEntry.place(x=260,y=240)
    
    disease_combo = Combobox(mf, values=['Allergy','Asthma','Cholesterol','Cough and Cold','Diabetes','Fever','Gastrointestinal Disorders','Hypertension','Other General Diseases','Pain'], font="Consolas 15", state='r', width=19)
    disease_combo.place(x=260,y=170)
    disease_combo.set('Select a Disease')


    buttonEnter = Button(
        medicine, text="Add", height=1, width=6,
        bd=3, font=(fontname, 18), bg=buttBack,fg=Background,command=AddMedicine)
    buttonEnter.place(x=250,y=480)

    buttonEnter = Button(
        medicine, text="Update",height=1, width=6,
        bd=3, font=(fontname, 18), bg=buttBack,fg=Background,command=UpdateMedicine)
    buttonEnter.place(x=365,y=480)

    buttonEnter = Button(
        medicine, text="Remove", height=1, width=6,
        bd=3, font=(fontname, 18), bg=buttBack,fg=Background,command=RemoveMedicine)
    buttonEnter.place(x=480,y=480)

    buttonEnter = Button(
        medicine, text="Clear", height=1, width=6,
        bd=3, font=(fontname, 18), bg=buttBack,fg=Background,command=ClearMedicine)
    buttonEnter.place(x=595,y=480)

# --Main Page function--

def AddTablet():
    
    cust=CustEntry.get() 
    name=c1.get() 
    age=ageEntry.get() 
    date=d1.get() 
    number=p1.get()
    city=cityEntry.get() 
    gender=gender_combo.get() 

    code=CodeEntry.get() 
    tablet=TabletEntry.get() 
    quan=QuanEntry.get()
    price=PriceEntry.get()
    total=int(quan)*float(price)

    mycursor,mysqldb=connection()

    mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Customer (
                Cust_id INT PRIMARY KEY,
                Bill_Number INT,
                Name VARCHAR(255),
                Age INT,
                date DATE,
                PhoneNumber VARCHAR(10),
                City VARCHAR(255),
                Gender VARCHAR(20)
            )
        """)
       
    mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Tablet_Data(
                Tablet_code VARCHAR(50),
                Tablet_Name VARCHAR(255),
                Quantity INT,
                Price DECIMAL(10, 2),
                Total DECIMAL(10, 2),
                Cust_id INT,
                FOREIGN KEY (Cust_id) REFERENCES Customer(Cust_id)
            )
        """)

    mycursor.execute("SELECT * FROM Customer WHERE Cust_id=%s",(cust,))
    exist_cust=mycursor.fetchone()

    if cust!='' and name!='' and age!='' and date!='' and city!='' and gender!='' and code!='' and tablet!='' and quan!='' and price!='':
            if not exist_cust:
                custSql="INSERT INTO Customer (Cust_id,Bill_Number,Name,Age,Date,PhoneNumber,City,Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                customer_data=(cust,billNum,name,age,date,number,city,gender)
                mycursor.execute(custSql,customer_data)
            
            tableSql="INSERT INTO Tablet_Data (Tablet_code, Tablet_Name, Quantity, Price, Total, Cust_id) VALUES (%s, %s, %s, %s,%s, %s)"
            tablet_data = (code, tablet, quan, price, total,cust)
            mycursor.execute(tableSql, tablet_data)
            
            mysqldb.commit()
            mysqldb.close()

            CodeEntry.delete(0, END)
            TabletEntry.delete(0, END)
            QuanEntry.delete(0, END)
            PriceEntry.delete(0, END)
            showValue()
            ll.destroy()
            ll.delete(0,END)
        
    else:
           messagebox.showinfo("Warning", "Enter the Details")

def ClearTablet():
    CodeEntry.delete(0, END)
    TabletEntry.delete(0, END)
    QuanEntry.delete(0, END)
    PriceEntry.delete(0, END)

def UpdateTablet():
    code=CodeEntry.get() 
    tablet=TabletEntry.get() 
    quan=QuanEntry.get()
    price=PriceEntry.get()
    total=int(quan)*float(price)

    mycursor,mysqldb=connection()

    updateSql="""
           UPDATE Tablet_Data
           SET Tablet_Name=%s,Quantity = %s,Price=%s,Total=%s
           WHERE Tablet_Code =%s
        """
    updateData=(tablet,quan,price,total,code)
    mycursor.execute(updateSql,updateData)
    
    mysqldb.commit()
    mysqldb.close()

    CodeEntry.delete(0, END)
    TabletEntry.delete(0, END)
    QuanEntry.delete(0, END)
    PriceEntry.delete(0, END)
    showValue()

def RemoveTablet():
    Code=CodeEntry.get()
    mycursor,mysqldb=connection()

    deletequery="Delete from Tablet_Data where Tablet_code=%s"
    val=(Code,)

    mycursor.execute(deletequery,val)
    mysqldb.commit()
    mysqldb.close()

    for item in tree.get_children():
        if tree.item(item, "values")[0] == Code: 
            tree.delete(item)
            break 
    messagebox.showinfo("information", "Record Deleted successfully...") 

    CodeEntry.delete(0, END)
    TabletEntry.delete(0, END)
    QuanEntry.delete(0, END)
    PriceEntry.delete(0, END)

def GetValue(event=None):
    CodeEntry.delete(0, END)
    TabletEntry.delete(0, END)
    QuanEntry.delete(0, END)
    PriceEntry.delete(0, END)

    codeId = tree.selection()[0]
    select = tree.set(codeId)

    CodeEntry.insert(0, select['Code'])
    TabletEntry.insert(0, select['Tablet Name'])
    QuanEntry.insert(0, select['Quantity'])
    PriceEntry.insert(0, select['Price'])

def showValue():
    cust = CustEntry.get() 
    mycursor, mysqldb = connection()
    mycursor.execute("SELECT Tablet_code, Tablet_Name, Quantity, Price, Total from Tablet_Data WHERE Cust_id=%s", (cust,))
    data = mycursor.fetchall()
        
    if len(data) != 0:
        tree.delete(*tree.get_children())
        for row in data:
            new_row=list(row)
            new_row[3]=float(new_row[3])
            new_row[4]=float(new_row[4])
            
            found=False
            for i,exist_row in enumerate(tree_list):
                 if exist_row[:2]==new_row[:2]:
                      tree_list[i]=new_row
                      found=True
                      break
            if not found:
                 tree_list.append(new_row)
            tree.insert("", END, values=row)
    mysqldb.close()


def updateList():
    global my_list
    mycursor,mysqldb=connection()
    listsql="Select name from Medicine"
    mycursor.execute(listsql)
    result=mycursor.fetchall()
    
    my_list=[row for row in result]
    
def getData(event=None):
    tablet=TabletEntry.get()
    ll.delete(0,END)
    for element in my_list:
         if tablet.lower() in element[0].lower():
              ll.insert(END,element[0])

def fillData(s):
    mycursor,mysqldb=connection()
    sql="Select code,price from Medicine where name=%s"
    val=(s,)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()

    CodeEntry.delete(0,END)
    PriceEntry.delete(0,END)

    CodeEntry.insert(0,result[0])
    PriceEntry.insert(0,result[1])
    mysqldb.close()

def selectList(event=None):
    TabletEntry.delete(0,END)
    select=ll.get(ACTIVE)
    fillData(select)
    TabletEntry.insert(0,ll.get(ACTIVE)) 

def listbox(event=None):
    global ll
    ll=Listbox(rf,height=4,width='34',relief='flat',bg='white')
    ll.place(x=1225,y=190)
    ll.bind('<Down>',my_down)
    ll.bind('<<ListboxSelect>>',selectList)


def my_down(even=None):
     ll.focus()
     ll.select_set(0)


# Invoice Section
    
def Invoice(event=None):
    success.destroy()
    bill = Tk()
    iconImg=PhotoImage(file="D:\\MCA_MIni_Final_project\\Final Year project\\Pharmacy Mangement System code\\assets\\icon.png")
    bill.iconphoto(False,iconImg)
    app_width = bill.winfo_screenwidth()
    app_height = bill.winfo_screenheight()
    bill.geometry("%dx%d+0+0" % (app_width, app_height))
    bill.config(bg=Background)
    bill.title('Cyber Pharmacy Invoice')
    
    custName=c1.get()
    custPhone=p1.get()
    
    CusDate=d1.get()
    total=0

    bill_icon = PhotoImage(file="assets/icon.png").subsample(4, 4)

    icon_label = Label(bill,bg=Background, image=bill_icon)
    icon_label.place(x=200,y=40)


    textarea=Text(bill,padx=8,pady=8,bg=Background,highlightbackground=foreground,highlightcolor=foreground,highlightthickness=3,font='Consolas 15',width=65,height=28)
    textarea.place(x=400,y=60)

    textarea.insert(END,"\t \t \t CYBER PHARMACY")
    textarea.insert(END,"\n \t \t142, Four roads, Salem-636004")
    textarea.insert(END,"\n \t \t \tPh.no: 9765786501")

    textarea.insert(END, f"\n \n \n Bill Number: {billNum} \t \t \t \t \t  Date: {CusDate}")
    textarea.insert(END, f"\n Customer Name: {custName} \t \t \t \t \t  Ph.no: {custPhone}")

    textarea.insert(END,"\n \n ===============================================================")
    textarea.insert(END,"\n Tablet Name \t\t\t Quantity \t\t Price \t\t Total")
    textarea.insert(END,"\n ===============================================================")
    for item in tree_list:
         total+=item[4]
         textarea.insert(END,f"\n {item[1]} \t\t\t {item[2]} \t\t {item[3]} \t\t {item[4]}")
    textarea.insert(END,"\n ===============================================================")

    textarea.insert(END,"\n \n ---------------------------------------------------------------")
    textarea.insert(END,f"\n Total: \t\t\t\t\t\t\t {total}")
    textarea.insert(END,"\n ---------------------------------------------------------------")

    bill.mainloop()
# End of Invoice Section

def main_page():
    app.destroy()
    global success,tree,rf,c1,p1,d1,CustEntry,nameEntry,ageEntry,DateEntry,NumberEntry,cityEntry,gender_combo,CodeEntry,TabletEntry,QuanEntry,PriceEntry,Tablet_str
    success = Tk()
    app_width = success.winfo_screenwidth()
    app_height = success.winfo_screenheight()
    iconImg=PhotoImage(file="D:\\MCA_MIni_Final_project\\Final Year project\\Pharmacy Mangement System code\\assets\\icon.png")
    success.iconphoto(False,iconImg)
    success.geometry("%dx%d+0+0" % (app_width, app_height))
    success.config(bg=Background)
    success.title('Cyber Pharmacy')
    
    # logo
    
    icon = PhotoImage(file="assets/icon.png").subsample(6, 6)

    icon_label = Label(success,bg=Background, image=icon)
    icon_label.place(x=35,y=2)

    # --Head section--
    Label(success, text="Cyber Pharmacy", font=(fontname, 50, 'bold'), fg=foreground, bg=Background).place(x=130, y=2)
    Label(success, text="Add New Medicine", font=(fontname, 17, 'bold'), fg=foreground, bg=Background).place(x=1200, y=80)

    image = PhotoImage(file="assets/plus.png").subsample(5, 5)

    image_label = Label(success,bg=Background, image=image)
    image_label.place(x=1250,y=2)

    image_label.bind("<Button-1>", lambda event: new_medicine())

    # --End Head section--
    
    # --Customer_detail Frame--
    
    lf=LabelFrame(success,highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground,bd=0,width=600,fg=foreground, height=650, bg=Background,font="10").place(x=20, y=120)

    # Label
    Label(lf, text="Customer Data", font=(fontname, 22, 'bold'),highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground, bg=Background, fg=foreground).place(x=60, y=100)
    Label(lf, text="Customer Id", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=190)
    Label(lf, text="Name", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=265)
    Label(lf, text="Age", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=350)
    Label(lf, text="Date", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=430)
    Label(lf, text="Gender", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=510)
    Label(lf, text="Phone Number", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=590)
    Label(lf, text="City", font=(fontname, 19, 'bold'), bg=Background, fg=foreground).place(x=80, y=670)
    
    c1=StringVar()
    p1=StringVar()
    d1=StringVar()

    CustEntry=Entry(lf,width=20,bd=2,font=10,highlightthickness=2,highlightcolor=Background)
    nameEntry = Entry(lf, width=20, bd=2, font=10,textvariable=c1,highlightthickness=2,highlightcolor=Background)
    ageEntry = Entry(lf, width=20, bd=2, font=10,highlightthickness=2,highlightcolor=Background)
    DateEntry = tkcalendar.DateEntry(lf, width=19, bd=2, font=10, date_pattern='yyyy-mm-dd',textvariable=d1,highlightthickness=2,highlightcolor=Background)
    NumberEntry=Entry(lf,width=20,bd=2,font=10,textvariable=p1,highlightthickness=2,highlightcolor=Background)
    cityEntry = Entry(lf, width=20, bd=2, font=10,highlightthickness=2,highlightcolor=Background)

    # Gender
    gender_combo = Combobox(lf, values=['Male', "Female", "Others"], font="Helvetica 15", state='r', width=19)
    gender_combo.place(x=280, y=510)
    gender_combo.set('Select a Gender')
    
    CustEntry.place(x=280,y=190)
    nameEntry.place(x=280, y=265)
    ageEntry.place(x=280, y=350)
    DateEntry.place(x=280, y=430)
    NumberEntry.place(x=280,y=590)
    cityEntry.place(x=280, y=670)
    
    # --End Customer_detail Frame--

    # --Medicine Frame--

    rf=LabelFrame(success,width=850,highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground,bd=0, fg=foreground,height=210, bg=Background,font="10").place(x=640, y=120)

    # Label
    Label(rf, text="Medicine Details", font=(fontname, 20, 'bold'), bg=Background,highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground, fg=foreground).place(x=680, y=100)
    Label(rf, text="Tablet Code", font=(fontname, 18, 'bold'), bg=Background, fg=foreground).place(x=665, y=160)
    Label(rf, text="Tablet Name", font=(fontname, 18, 'bold'), bg=Background, fg=foreground).place(x=1060, y=160)
    Label(rf, text="Quantity", font=(fontname, 18, 'bold'), bg=Background, fg=foreground).place(x=665, y=260)
    Label(rf, text="Price", font=(fontname, 18, 'bold'), bg=Background, fg=foreground).place(x=1060, y=260)

    Button(rf,text="Add",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=8,height=1,command=AddTablet).place(x=810,y=340)
    Button(rf,text="Update",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=8,height=1,command=UpdateTablet).place(x=940,y=340)
    Button(rf,text="Remove",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=8,height=1,command=RemoveTablet).place(x=1080,y=340)
    Button(rf,text="Clear",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=8,height=1,command=ClearTablet).place(x=1210,y=340)
    
    updateList()
    
    CodeEntry = Entry(rf, width=18, bd=2, font=10,highlightthickness=2,highlightcolor=Background)
    TabletEntry = Entry(rf, width=18, bd=2, font=10,highlightthickness=2,highlightcolor=Background)
    QuanEntry = Entry(rf, width=18, bd=2, font=10,highlightthickness=2,highlightcolor=Background)
    PriceEntry = Entry(rf,width=18, bd=2, font=10,highlightthickness=2,highlightcolor=Background)

    CodeEntry.place(x=830, y=160)
    TabletEntry.place(x=1225, y=160)
    QuanEntry.place(x=830, y=260)
    PriceEntry.place(x=1225, y=260)
    
    TabletEntry.bind("<FocusIn>", listbox)
    TabletEntry.bind('<KeyRelease>',getData)
    # --En₫ Medicine Frame--
    
    # --Treeview Frame--
    tf = LabelFrame(success,fg=foreground, width=650, height=340,font='10', highlightbackground=foreground,highlightthickness=5,highlightcolor=foreground,bd=0,bg=Background)
    tf.place(x=640, y=410)
    

    cols = ('Code', 'Tablet Name','Quantity','Price','Total')
    tree = Treeview(tf, columns=cols, show='headings', height=11)
    for col in cols:
         tree.heading(col, text=col)

    col_width = int(798 / len(cols))  
    for col in cols:
         tree.column(col, width=col_width)
    

    vsb = Scrollbar(tf, orient="vertical", command=tree.yview)
    vsb.pack(side="right", fill="y")
    tree.configure(yscrollcommand=vsb.set)


    tree.pack(fill='both', expand=True, padx=15, pady=15)

    tree.bind('<<TreeviewSelect>>', GetValue)
     
    # --End Treeview Frame--

    # --Invoice Button--
    Button(success,text="Print Invoice",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=16,height=1,command=Invoice).place(x=960,y=710)
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
foreground="#46688B"
Background="#F4F7FB"
buttBack="#38706B"
fontname="Consolas"
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (app_width, app_height))
app.config(bg=Background)
iconImg=PhotoImage(file="D:\\MCA_MIni_Final_project\\Final Year project\\Pharmacy Mangement System code\\assets\\icon.png")
app.iconphoto(False,iconImg)
app.title('Cyber Pharmacy')

tree_list=[]
billNum=random.randint(1,300)

# ----Login form----

loginFrame=Frame(app,width=500,height=360,bg=foreground).place(x=500,y=180)

Label(app,text="Cyber Pharmacy",font=(fontname, 50,'bold'),fg=foreground,bg= Background).place(x=480,y=60)


Label(loginFrame,text="Log In",font=(fontname, 40,'bold'),fg=Background,bg=foreground).place(x=670,y=220)
Label(loginFrame,text="UserName",font=(fontname, 26,'bold'),fg=Background,bg=foreground).place(x=530,y=320)
Label(loginFrame,text="Password",font=(fontname, 26,'bold'),fg=Background,bg=foreground).place(x=530,y=425)

# Entry
userValue=StringVar()
passValue=StringVar()

userEntry=Entry(loginFrame,textvariable=userValue,width=20,bd=1,font=12,highlightthickness=3,highlightcolor=Background).place(x=730,y=325)
passEntry=Entry(loginFrame,textvariable=passValue,width=20,bd=1,font=12,highlightthickness=3,show='*',highlightcolor=Background).place(x=730, y=430)

Button(app,text="Login",font=(fontname, 18,'bold'),bg=buttBack,fg=Background,width=10,height=1,command=login).place(x=600,y=570)
Button(app,text="Clear",font=(fontname,18,'bold'),bg=buttBack,fg=Background,width=10,height=1,command=clear).place(x=770,y=570)
# ---- End Login Form ----

app.mainloop()
