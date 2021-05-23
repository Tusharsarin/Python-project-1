from tkinter import *
import math
import random,os
from tkinter import messagebox




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x820+0+0")
        self.root.title("Daily Needs Store's Invioce Creator ")
        bg_color="maroon"   #maroon color
        title=Label(self.root,text="Daily Needs Store's Invoice Creator",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #---------------------Variable-----------------------------------------
        
        #------------------Cosmetics Variable-----------------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.powder=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        
        #----------------------------------Grocery Variable---------------------------------
        self.rice=IntVar()
        self.wheat=IntVar()
        self.wheat_flour=IntVar()
        self.daal=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #--------------------------Drinks Variables-----------------------
        self.maaza=IntVar()
        self.frooti=IntVar()
        self.coca_cola=IntVar()
        self.thumps_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #-----------------------Total Products Variable---------------------------------------------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.drinks_price=StringVar()

        #-----------------Tax Variables----------------------------
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.drinks_tax=StringVar()      
       
        #------------------Total Prices Variable---------------------------------------
        self.total_product_price=StringVar()
        self.total_tax=StringVar()
        self.total_bill_price=IntVar()
       
        #---------------------------------------Customer Variable-------------------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()       
       
       
       
        #-------------------Customer Details Frame---------------

        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color) 
        F1.place(x=0,y=80,relwidth=1)


        cname_label=Label(F1,text="Customer Name :",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10)
        cname_text=Entry(F1,width=18,textvariable=self.c_name,bd=7,relief=SUNKEN,font=("ariel",15)).grid(row=0,column=1,padx=5,pady=10)

        cphone_label=Label(F1,text="Phone No. :",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=10,pady=10)
        cphone_text=Entry(F1,width=18,textvariable=self.c_phone,bd=7,relief=SUNKEN,font=("ariel",15)).grid(row=0,column=3,padx=5,pady=10)

        cbill_label=Label(F1,text=" Search Bill Number :",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=10,pady=10)
        cbill_text=Entry(F1,width=18,textvariable=self.search_bill,bd=7,relief=SUNKEN,font=("ariel",15)).grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=15,bd=7,font=("ariel",12,"bold")).grid(row=0,column=6,padx=10,pady=10)

        #--------------------Cosmetics Frame---------------------------------
        F2=LabelFrame(self.root,text="Cosmetics Products",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color) 
        F2.place(x=5,y=180,width=350,height=380)


        bath_lbl=Label(F2,text="Bath Soap :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Face Wash :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_c_lbl=Label(F2,text="Face Cream :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_c_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="Hair Gel :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Lotion :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        powder_lbl=Label(F2,text="Telcom Powder :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        powder_txt=Entry(F2,width=10,textvariable=self.powder,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #-----------------------Grocery Frame--------------------------
        F3=LabelFrame(self.root,text="Grocery Products",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color) 
        F3.place(x=360,y=180,width=335,height=380)

        g1_lbl=Label(F3,text="Rice :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        g2_lbl=Label(F3,text="Wheat :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        g3_lbl=Label(F3,text="Wheat Flour :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.wheat_flour,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)

        g4_lbl=Label(F3,text="Daal :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=2,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=3,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=2,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=3,padx=10,pady=10)




        #-----------------------------Drinks Frame-----------------------------
        F4=LabelFrame(self.root,text="Drinks Products",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color) 
        F4.place(x=700,y=180,width=335,height=380)

        d1_lbl=Label(F4,text="Maaza :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=4,padx=10,pady=10,sticky="w")
        d1_txt=Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=10)

        d2_lbl=Label(F4,text="Frooti :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=4,padx=10,pady=10,sticky="w")
        d2_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=5,padx=10,pady=10)

        d3_lbl=Label(F4,text="Coca-cola :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=4,padx=10,pady=10,sticky="w")
        d3_txt=Entry(F4,width=10,textvariable=self.coca_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=5,padx=10,pady=10)

        d4_lbl=Label(F4,text="Thumbs Up :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=4,padx=10,pady=10,sticky="w")
        d4_txt=Entry(F4,width=10,textvariable=self.thumps_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=5,padx=10,pady=10)

        d5_lbl=Label(F4,text="Limca :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=4,padx=10,pady=10,sticky="w")
        d5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=5,padx=10,pady=10)

        d6_lbl=Label(F4,text="Sprite :",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=4,padx=10,pady=10,sticky="w")
        d6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=5,padx=10,pady=10)


        #--------------------------------bill display----------------------------
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1050,y=180,width=455,height=380)
        bill_title=Label(F5,text="Bill Display",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #-------------------Button Frame----------------------------------------
        F6=LabelFrame(self.root,text="Bill Calculation Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color) 
        F6.place(x=0,y=560,relwidth=1,height=260)
        
        m1=Label(F6,text="Total Cosmatic Price :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2=Label(F6,text="Total Grocery Price :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3=Label(F6,text="Total Drinks Price :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        m5=Label(F6,text="Total Product Price :",bg=bg_color,fg="white",font=("times new roman",22,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        m5_txt=Entry(F6,width=18,textvariable=self.total_product_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        m6=Label(F6,text="Total Taxes :",bg=bg_color,fg="white",font=("times new roman",24,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w")
        m6_txt=Entry(F6,width=18,textvariable=self.total_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)

        
        c1=Label(F6,text="Cosmatic Tax :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        c2=Label(F6,text="Grocery Tax :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        c3=Label(F6,text="Drinks Tax :",bg=bg_color,fg="white",font=("times new roman",20,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)


        btn_f=Frame(F6,bd=10,relief=GROOVE)
        btn_f.place(x=875,y=75,width=580,height=100)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=12,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        g_bill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=12,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=12,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,width=12,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()


    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fw_p=self.face_wash.get()*100
        self.c_fc_p=self.face_cream.get()*80
        self.c_g_p=self.gel.get()*60
        self.c_l_p=self.lotion.get()*200
        self.c_p_p=self.powder.get()*90

        self.total_cosmetic_price=float(
                                    (self.c_s_p)+
                                    (self.c_fw_p)+
                                    (self.c_fc_p)+
                                    (self.c_g_p)+
                                    (self.c_l_p)+
                                    (self.c_p_p)
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*50
        self.g_w_p=self.wheat.get()*30
        self.g_wf_p=self.wheat_flour.get()*40
        self.g_d_p=self.daal.get()*100
        self.g_s_p=self.sugar.get()*50
        self.g_t_p=self.tea.get()*350

        self.total_grocery_price=float(
                                    (self.g_r_p)+
                                    (self.g_w_p)+
                                    (self.g_wf_p)+
                                    (self.g_d_p)+
                                    (self.g_s_p)+
                                    (self.g_t_p)
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.18),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maaza.get()*100
        self.d_f_p=self.frooti.get()*120
        self.d_c_p=self.coca_cola.get()*90
        self.d_t_p=self.thumps_up.get()*95
        self.d_l_p=self.limca.get()*85
        self.d_s_p=self.sprite.get()*105

        self.total_drinks_price=float(
                                    (self.d_m_p)+
                                    (self.d_f_p)+
                                    (self.d_c_p)+
                                    (self.d_t_p)+
                                    (self.d_l_p)+
                                    (self.d_s_p)
                                    )
        self.drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.18),2)
        self.drinks_tax.set("Rs. "+str(self.d_tax))


        self.product_price=float(
                                (self.total_cosmetic_price)+
                                (self.total_grocery_price)+
                                (self.total_drinks_price)
                                )
        self.total_product_price.set("Rs. "+str(self.product_price))
        self.total_tax.set("Rs. "+str(round((self.product_price*0.18),2)))

       

        self.total_bill_price=float(
                                        self.total_cosmetic_price+
                                        self.total_grocery_price+
                                        self.total_drinks_price+
                                        self.c_tax+
                                        self.g_tax+
                                        self.d_tax
                                        
                                    )

        self.total_bill_price=round((self.total_bill_price),2)


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t  Welcome Daily Needs Retail Store ")
        self.txtarea.insert(END,f"\n\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()} ")
        self.txtarea.insert(END,f"\n***************************************************")
        self.txtarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n***************************************************")




    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product are Purchased")

        else:

            self.welcome_bill()

            #-----------------Print Cosmetic Products in Bill--------------------------

            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t\t{self.gel.get()}\t\t{self.c_g_p}")

            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t\t{self.lotion.get()}\t\t{self.c_l_p}")

            if self.powder.get()!=0:
                self.txtarea.insert(END,f"\n Telcome Powder\t\t\t{self.powder.get()}\t\t{self.c_p_p}")

            #-----------------Print Grocery Products in Bill--------------------------

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.wheat_flour.get()!=0:
                self.txtarea.insert(END,f"\n Wheat Flour\t\t\t{self.wheat_flour.get()}\t\t{self.g_wf_p}")

            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t{self.g_t_p}")
        
            #-----------------Print Drinks Products in Bill--------------------------

            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t\t{self.maaza.get()}\t\t{self.d_m_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.coca_cola.get()!=0:
                self.txtarea.insert(END,f"\n Coca Cola\t\t\t{self.coca_cola.get()}\t\t{self.d_c_p}")

            if self.thumps_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t\t{self.thumps_up.get()}\t\t{self.d_t_p}")

            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END,f"\n---------------------------------------------------")
            
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Costmetic Tax :\t\t\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax :\t\t\t\t\t{self.grocery_tax.get()}")
    
            if self.drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Drinks Tax :\t\t\t\t\t{self.drinks_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill Price :\t\t\t\t\tRs.{self.total_bill_price}")


            self.txtarea.insert(END,f"\n---------------------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved successfully")

        else:
            return

    def find_bill(self):
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
        if self.search_bill.get()=="" :
            messagebox.showerror("Error","Enter Bill No.")


    def clear_data(self):

        op=messagebox.askyesno("Clear","Do you Really want to Clear all Details?")
        if op>0:
            #------------------Cosmetics Variable-----------------------
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.powder.set(0)
            self.gel.set(0)
            self.lotion.set(0)
            
            #----------------------------------Grocery Variable---------------------------------
            self.rice.set(0)
            self.wheat.set(0)
            self.wheat_flour.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #--------------------------Drinks Variables-----------------------
            self.maaza.set(0)
            self.frooti.set(0)
            self.coca_cola.set(0)
            self.thumps_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #-----------------------Total Products Variable---------------------------------------------
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            #-----------------Tax Variables----------------------------
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")      
        
            #------------------Total Prices Variable---------------------------------------
            self.total_product_price.set("")
            self.total_tax.set("")
                
            #---------------------------------------Customer Variable-------------------------
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill=StringVar("")  
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you Really want to exit?")
        if op>0:
            self.root.destroy()   

root=Tk()
obj = Bill_App(root)
root.mainloop()
