from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #Variables
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        #Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

        #SubCatClothing
        self.SubCatClothing=["Jeans","T-Shirt","Shirt"]
        self.jeans=["Levis","Louis Philippe","U.S Polo","Mufti"]
        self.price_levis=4999
        self.price_louisphilippe=5999
        self.price_polo=4499
        self.price_mufti=3999

        self.T_shirt=["Polo","Puma","Jack&Jones"]
        self.price_polo=999
        self.price_puma=1199
        self.price_Jack=799

        self.Shirt=["Puma","Louis Phillipe","Park Avenue"]
        self.price_Puma=1999
        self.price_Louis=1299
        self.price_Park=1799

        #SubCatLifeStyle
        self.SubCatLifeStyle=['Bath Soap','Face Cream','Hair Oil']
        self.Bath_Soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_life=20
        self.price_lux=20
        self.price_santoor=17
        self.price_pearl=25

        self.Face_cream=["Fair&Lovely","Ponds","Dove","Garnier"]
        self.price_fair=30
        self.price_ponds=25
        self.price_dove=20
        self.price_garnier=50

        self.Hair_Oil=["Dabur Amla","Jasmine","Bajaj"]
        self.price_amla=28
        self.price_jasmine=33
        self.price_bajaj=25

        #SubCatMobiles
        self.SubCatMobiles=['Iphone','Samsung','Oppo','Vivo','RealMe']
        self.Iphone=["Iphone_x","Iphone_11","Iphone_12"]
        self.price_ix=45000
        self.price_i11=75000
        self.price_i12=80000

        self.Samsung=["Samsung M16","Galaxy A20","Samsung M21"]
        self.price_sm16=16000
        self.price_sm20=22000
        self.price_sm21=20000

        self.Oppo=["Oppo A74","Oppo K3","Oppo F21"]
        self.price_o74=12999
        self.price_o3=8999
        self.price_o21=1999

        self.Vivo=["Vivo Y33s","Vivo Y22","Vivo Y75"]
        self.price_v33=15349
        self.price_v22=16499
        self.price_v75=19990

        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_rm12=25000
        self.price_rm13=28000
        self.price_rmpro=33000


        #Image1
        img=Image.open("image/pic2.jpeg")
        img=img.resize((350,130), Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=350, height=130)

        #Image2
        img_1 = Image.open("image/pic1.jpeg")
        img_1 = img_1.resize((350, 130), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=350, y=0, width=350, height=130)

        #Image3
        img_2 = Image.open("image/pic4.jpeg")
        img_2 = img_2.resize((350, 130), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=1050, y=0, width=350, height=130)

        #Image4
        img_3 = Image.open("image/good.jpg")
        img_3 = img_3.resize((350, 130), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        lbl_img_3 = Label(self.root, image=self.photoimg_3)
        lbl_img_3.place(x=700, y=0, width=350, height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("Times New Roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=("times new roman",16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=40)
        time()

        #Main Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("Times New Roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=150)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("aerial",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("aerial",12,"bold"),width=19)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=("aerial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("aerial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=("aerial",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("aerial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("Times New Roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=5, width=550, height=150)

        # Category
        self.lblCategory = Label(Product_Frame, font=("aerial", 12, "bold"), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame, value=self.Category, font=("aerial", 10, "bold"),width=18,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # Sub Category
        self.lblSubCategory = Label(Product_Frame, font=("aerial", 12, "bold"), bg="white", text="Sub Category", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("aerial", 10, "bold"), width=18, state="readonly")
        self.ComboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product
        self.lblProduct = Label(Product_Frame, font=("aerial", 12, "bold"), bg="white", text="Product Name", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly", font=("aerial", 10, "bold"), width=18)
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice = Label(Product_Frame, font=("aerial", 12, "bold"), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame,textvariable=self.prices, state="readonly",font=("aerial", 10, "bold"), width=18)
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Quantity
        self.lblQty = Label(Product_Frame, font=("aerial", 12, "bold"), bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame,textvariable=self.qty, font=("aerial", 10, "bold"), width=20)
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=160,width=910,height=220)

        # Image2
        img_12 = Image.open("image/good.jpg")
        img_12 = img_12.resize((450, 335), Image.ANTIALIAS)
        self.photoimg_12 = ImageTk.PhotoImage(img_12)

        lbl_img_12 = Label(MiddleFrame, image=self.photoimg_12)
        lbl_img_12.place(x=0, y=0, width=450, height=335)

        # Image2
        img_13 = Image.open("image/pic3.jpeg")
        img_13 = img_13.resize((450, 210), Image.ANTIALIAS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(MiddleFrame, image=self.photoimg_13)
        lbl_img_13.place(x=450, y=0, width=450, height=210)


        #Search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1020, y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=("aerial",12,"bold"),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("aerial",10,"bold"),width=15)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("aerial",12,"bold"),bg="red",fg="white",width=13,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        # Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=930,y=35,width=420,height=350)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame, yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("Times New Roman", 12, "bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0, y=400, width=1520, height=300)

        self.lblSubTotal=Label(Bottom_Frame,font=("aerial", 12, "bold"),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("aerial", 10, "bold"),width=20)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=("aerial",12,"bold"),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("aerial",10,"bold"),width=20)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=("aerial",12,"bold"),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("aerial",10,"bold"),width=20)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("aerial",10,"bold"),bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill = Button(Btn_Frame,command=self.gen_bill, height=2, text="Generate Bill", font=("aerial", 10, "bold"), bg="orange",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_Frame,command=self.save_bill, height=2, text="Save Bill", font=("aerial", 10, "bold"), bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame,command=self.iprint, height=2, text="Print", font=("aerial", 10, "bold"), bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame,command=self.clear, height=2, text="Clear", font=("aerial", 10, "bold"), bg="orange", fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame,command=self.root.destroy, height=2, text="Exit", font=("aerial", 10, "bold"), bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.welcome()

        self.l=[]
    #==========================Function Declaration========================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No.{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="No"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for j in f1:
                    self.textarea.insert(END,j)
                f1.close()
                found="Yes"
        if found=="No":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to Pacific Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n===========================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n===========================================\n")


    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Jeans":
            self.ComboProduct.config(value=self.jeans)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)


        #LifeStyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)

        #Mobile
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Oppo":
            self.ComboProduct.config(value=self.Oppo)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Vivo":
            self.ComboProduct.config(value=self.Vivo)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

    def price(self,event=""):

        #Jeans
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Philippe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="U.S Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T-Shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_Puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_Jack)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt
        if self.ComboProduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_louisphilippe)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #lifeStyle
        #Bath Soap
        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face cream
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dove":
            self.ComboPrice.config(value=self.price_dove)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #HairOil
        if self.ComboProduct.get()=="Dabur Amla":
            self.ComboPrice.config(value=self.price_amla)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jasmine":
            self.ComboPrice.config(value=self.price_jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Mobiles
        #Iphones
        if self.ComboProduct.get()=="Iphone_x":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Samsung
        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy A20":
            self.ComboPrice.config(value=self.price_sm20)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Oppo
        if self.ComboProduct.get()=="Oppo A74":
            self.ComboPrice.config(value=self.price_o74)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oppo K3":
            self.ComboPrice.config(value=self.price_o3)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oppo F21":
            self.ComboPrice.config(value=self.price_o21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Vivo
        if self.ComboProduct.get()=="Vivo Y33s":
            self.ComboPrice.config(value=self.price_v33)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vivo Y22":
            self.ComboPrice.config(value=self.price_v22)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vivo Y75":
            self.ComboPrice.config(value=self.price_v75)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #RealMe
        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rm13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_rmpro)
            self.ComboPrice.current(0)
            self.qty.set(1)





if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
