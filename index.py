import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root=Tk()
    app= windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master= master
        self.master.title("Hospdash[META]__wormflash")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame , text='   Meta Hosp Dash   ',font=("arial",40,"bold"),bd=10, relief="sunken")

        self.LabelTitle.grid(row=0 , column = 0, columnspan = 2, pady=20)
        self.Loginframe1=Frame(self.frame,width=1000,height=300,bd=10 , relief="groove")
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=10 , relief="groove")
        self.Loginframe2.grid(row=2,column=0,pady=15)
        self.Loginframe3=Frame(self.frame,width=1000,height=100,bd=10 , relief="groove")
        self.Loginframe3.grid(row=6,column=0,)

        
        self.button_reg = Button(self.Loginframe3,text="Patient Registration Window",font=("arial",15,"bold"),state=DISABLED,
            command=self.reg_window)
        
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)
        
        
        self.button_hosp = Button(self.Loginframe3,text="Hospital management",font=("arial",15,"bold"),state=DISABLED,
            command=self.hosp_window)       
        self.button_hosp.grid(row=1,column=0,padx=10,pady=10)
        
        
        self.button_dr = Button(self.Loginframe3,text="Doctor appointment",font=("arial",15,"bold"),state=DISABLED,
            command=self.dr_window)
        
        self.button_dr.grid(row=0,column=1,padx=10,pady=10)
        
        
        self.button_ph = Button(self.Loginframe3,text="Pharmacy Records",font=("arial",15,"bold"),state=DISABLED,
            command=self.ph_window)
        
        self.button_ph.grid(row=1,column=1,padx=10,pady=10)

        #username and password frame

        self.LableUsername = Label(self.Loginframe1, text ="USER NAME", font=("arial",20,"bold"),bd=3)
        self.LableUsername.grid(row =0 , column=0)
      
        self.textUsername = Entry(self.Loginframe1, font=("arial",20,"bold"),bd=3,textvariable=self.Username)
        self.textUsername.grid(row=0,column=1)
        
        self.LablePassword = Label(self.Loginframe1, text ="PASSWORD", font=("arial",20,"bold"),bd=3)
        self.LablePassword.grid(row =1 , column=0)

        self.textPassword = Entry(self.Loginframe1, font=("arial",20,"bold"),show = '*',bd=3,textvariable=self.Password)
        self.textPassword.grid(row=1,column=1)

        self.button_login = Button(self.Loginframe2, text ="Login", width=20, font=("arial",18,"bold"),command=self.login)
        self.button_login.grid(row=0,column=0, padx =10 ,pady=10)
        

        self.button_reset = Button(self.Loginframe2, text ="Reset", width=20, font=("arial",18,"bold"),
            command=self.reset_btn)
        self.button_reset.grid(row=0,column=1, padx =10 ,pady=10)

        self.button_exit = Button(self.Loginframe2, text ="Exit", width=20, font=("arial",18,"bold"),
            command=self.exit_btn)
        self.button_exit.grid(row=0,column=2, padx =10 ,pady=10)

    def login(self):
        user=self.Username.get()
        password=self.Password.get()

        if (user==str("admin") and (password==str("admin"))):
            self.button_reg.config(state=NORMAL)
            self.button_hosp.config(state=NORMAL)
            self.button_dr.config(state=NORMAL)
            self.button_ph.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("META HOSP DASH","You enterd a inviald name and password , please check user name and password again and retry , thanks ")  
            self.button_reg.config(state=DISABLED)
            self.button_hosp.config(state=DISABLED)
            self.button_dr.config(state=DISABLED)
            self.button_ph.config(state=DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_hosp.config(state=DISABLED)
        self.button_dr.config(state=DISABLED)
        self.button_ph.config(state=DISABLED)
        
        
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Meta Hosp Dash","Do You Want to exit ?")
        if self.exit_btn >0:
            self.master.destroy()
            return


        

    def reg_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def hosp_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def dr_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)


    def ph_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)





class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")


        date_of_reg = StringVar()
        date_of_reg.set(time.strftime("%d/%m/%y"))

        ref=StringVar()
        mobile_no=StringVar()
        pincode=StringVar()
        firstname=StringVar()
        lastname=StringVar()
        address=StringVar()
        gender=StringVar()

        var1=StringVar()
        var2=StringVar() 
        var3=StringVar()
        var4=StringVar() 
        var5=IntVar()

        membership= StringVar()
        membership.set("0")


        def exitbt():
                extbt=tkinter.messagebox.askyesno("Patient Registration System","Are you sure you want to exit?") 
                if exitbt > 0:
                    root.destroy()
                    return
                else:
                    self.newWindow =Toplevel(self.master)
                    self.app = Registration(self.newWindow)

        def receiptbt():
                receiptbt=tkinter.messagebox.askokcancel("Patient Registration System","You want to add as a new record")
                if receiptbt> 0:
                    resetbt()

                elif receiptbt <=0:
                        resetbt()
                        detail_labeltxt.delete("1.0",END)
                        return




        def resetbt():
       
                firstname.set("")
                lastname.set("")
                ref.set("")
                mobile_no.set("")
                pincode.set("")
                address.set("")
                var1.set("")
                var2.set("") 
                var3.set("")
                var4.set("") 
                var5.set("")
                membership.set("0")
                member_gendercmb.current(0)
                member_id_proofcmb.current(0)
                member_typecmb.current(0)
                member_paycmb.current(0)
                member_membershiptxt(state=DISABLED)

        def refernce_number():
                ranumber = random.randint(10000,999999)
                randomnumber=str(ranumber)
                ref.set(randomnumber)


        def membership_fees():
                if(var5.get()== 1):
                        member_membershiptxt.configure(state=NORMAL)
                        item= float(15000)
                        membership.set(str(item)+"rs")

                elif(var5.get()==0):
                        member_membershiptxt.configure(state=DISABLED)
                        membership.set(0)

        def repeiptbtn():
                refernce_number()
                detail_labeltxt.insert(END ,"\t"+date_of_reg.get()+"\t"+ref.get()+" \t "+" \t "+firstname.get()+" \t "+" \t "+lastname.get()+" \t "+" \t "+mobile_no.get()+" \t "+" \t "+
                address.get()+" \t"+pincode.get()+"\t"+member_gendercmb.get()+"\t"+membership.get()+"\n")


        title=Label(self.root, text="Member Registration Form", font=("monotype cprsiva",30,"bold"),bd=5,relief=GROOVE,
            bg= 'yellow', fg="black")
        title.pack(side=TOP,fill= X)


        manage_frame=Frame(self.root, bd=4,relief=RIDGE,bg="Dark blue")
        manage_frame.place(x=20,y=100,width=450,height=590)

    
      

        cus_title=Label(manage_frame,text="Custmor Details",font=("arial",20,"bold"),bg="dark blue",fg="white")
        cus_title.grid(row=0,columnspan=2,pady=5)

        member_datelbl=Label(manage_frame,text="Date",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_datelbl.grid(row=1,column=0, padx=10,pady=5,sticky="w")

        member_datetxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=date_of_reg)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10, sticky='w')

        member_reflbl=Label(manage_frame,text="Reference ID",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_reflbl.grid(row=2,column=0, padx=10,pady=5,sticky="w")
       
        member_reftxt=Entry(manage_frame,font=("arial",15,"bold"),state=DISABLED,text=ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10, sticky='w')


        member_fnamelbl=Label(manage_frame,text="First Name",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_fnamelbl.grid(row=3,column=0, padx=10,pady=5,sticky="w")

        member_fnametxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=firstname)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10, sticky='w')
     

        member_lnamelbl=Label(manage_frame,text="Last Name",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_lnamelbl.grid(row=4,column=0, padx=10,pady=5,sticky="w")

        member_lnametxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=lastname)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10, sticky='w')


        
        member_mobilelbl=Label(manage_frame,text="Mobile No.",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_mobilelbl.grid(row=5,column=0, padx=10,pady=5,sticky="w")

        member_mobiletxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=mobile_no)
        member_mobiletxt.grid(row=5,column=1,pady=5,padx=10, sticky='w')

        
        member_adresslbl=Label(manage_frame,text="Address",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_adresslbl.grid(row=6,column=0, padx=10,pady=5,sticky="w")

        member_adresstxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=address)
        member_adresstxt.grid(row=6,column=1,pady=5,padx=10, sticky='w')

        
        member_pincodelbl=Label(manage_frame,text="Pincode",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_pincodelbl.grid(row=7,column=0, padx=10,pady=5,sticky="w")

        member_pincodetxt=Entry(manage_frame,font=("arial",15,"bold"),textvariable=pincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10, sticky='w')

        member_genderlbl=Label(manage_frame,text="Gender",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_genderlbl.grid(row=8,column=0, padx=10,pady=5,sticky="w")

        member_gendercmb=ttk.Combobox(manage_frame,text=var4,state="readonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['value']=("","Male","Female","other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8,column=1,pady=5,padx=10,sticky="w")
        
       

        member_id_prooflbl=Label(manage_frame,text="ID Proof",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_id_prooflbl.grid(row=9,column=0, padx=10,pady=5,sticky="w")

        member_id_proofcmb=ttk.Combobox(manage_frame,text=var3,state="readonly",font=("arial",15,"bold"),width=19)
        member_id_proofcmb['value']=("","Adhar Card","Passport","Driving Licesnse")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9,column=1,pady=5,padx=10,sticky="w")


        member_typelbl=Label(manage_frame,text="Member type",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_typelbl.grid(row=10,column=0, padx=10,pady=5,sticky="w")

        member_typecmb=ttk.Combobox(manage_frame,text=var2,state="readonly",font=("arial",15,"bold"),width=19)
        member_typecmb['value']=("","Ayushman Card","Insurance","Pay Immediately","Pay when leave")
        member_typecmb.current(0)
        member_typecmb.grid(row=10,column=1,pady=5,padx=10,sticky="w")


        member_paylbl=Label(manage_frame,text="Mode of payment",font=("arial",15,"bold"),bg="dark blue",fg="white")
        member_paylbl.grid(row=11,column=0, padx=10,pady=5,sticky="w")

        member_paycmb=ttk.Combobox(manage_frame,text=var1,state="readonly",font=("arial",15,"bold"),width=19)
        member_paycmb['value']=("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card - Master Card","CASH","PhonePe","Google-Pay")
        member_paycmb.current(0)
        member_paycmb.grid(row=11,column=1,pady=5,padx=10,sticky="w")
        
        member_membership=Checkbutton(manage_frame,text="Memeber fees",variable=var5,onvalue=1,offvalue=0,font=("arial",15,"bold"),bg="dark blue",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0, padx=10,pady=5,sticky="w")

        member_membershiptxt=Entry(manage_frame,font=("arial",15,"bold"),state= DISABLED,justify=RIGHT,textvariable=membership)
        member_membershiptxt.grid(row=12,column=1)

        detail_frame= Frame(self.root , relief = RIDGE, bg="dark blue")
        detail_frame.place(x=500,y=100,width=820,height=590)

        detail_label=Label(detail_frame,font=("arial",11,"bold"),padx=10,pady=2,width=95,text="Date\tRef Id\tFirstname\tLastname\tMobileno\tAddress\tPincode\tGender\tMemberShip ")
        detail_label.grid(row=0,column=0,columnspan=4,sticky="w")
        detail_labeltxt=Text(detail_frame , width=123 ,height=32, font=("arial",10))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)

        receipt=Button(detail_frame,padx=15,bd=5,font=('arial',12,'bold'),
                bg='yellow',width=20,text='Receipt',command=repeiptbtn)
        receipt.grid(row=2,column=0)

        exitbtn=Button(detail_frame,padx=1,bd=5,font=('arial',12,'bold'),
                bg='yellow',width=20,text='Exit',command=exitbt)
        exitbtn.grid(row=2,column=1)

        restbtn=Button(detail_frame,padx=15,bd=5,font=('arial',12,'bold'),
                bg='yellow',width=20,text='Reset',command=resetbt)
        restbtn.grid(row=2,column=2)


        
class Doctor:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")


        date_of_reg = StringVar()
        date_of_reg.set(time.strftime("%d/%m/%y"))

        DrId = StringVar()
        Drname = StringVar()
        DateofBirth = StringVar()
        Spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experiences = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefiCard = StringVar()

        def exitbtn():
           exitbtn = tkinter.messagebox.askyesno("Doctor Management System","Are you sure you want to exit ?")
           if exitbtn > 0:
            root.destroy()
           return

        def resetfunc():
           DrId.set("")
           Drname.set("")
           DateofBirth.set("")
           Spes.set("")
           GovtPri.set("")
           Surgeries.set("")
           Experiences.set("")
           Nurses.set("")
           DrMobile.set("")
           PtName.set("")
           Apptime.set("")
           PtAge.set("")
           PatientAddress.set("")
           PtMobile.set("")
           Disease.set("")
           Case.set("")
           BenefiCard.set("")
           return


        def deletefunc():
           DrId.set("")
           Drname.set("")
           DateofBirth.set("")
           Spes.set("")
           GovtPri.set("")
           Surgeries.set("")
           Experiences.set("")
           Nurses.set("")
           DrMobile.set("")
           PtName.set("")
           Apptime.set("")
           PtAge.set("")
           PatientAddress.set("")
           PtMobile.set("")
           Disease.set("")
           Case.set("")
           BenefiCard.set("")
           return

        def Patient_idFunc():
           ranumber = random.randint(10000,999999)
           randomnumber = str(ranumber)
           DrId.set(randomnumber)


        def prescriptiondatafunc():
           Patient_idFunc()
           TextPrescriptionData.insert(END,date_of_reg.get()+"\t"+DrId.get()+"\t"
           +Drname.get()+"\t\t"+DateofBirth.get()+"\t\t"+ Spes.get()+"\t\t"+GovtPri.get()
           +"\t\t"+ Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
           PtName.get()+"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")
           return

        def prescriptionfunc():
           Patient_idFunc()
           TextPrescription.insert(END, "Date: \t\t" +date_of_reg.get()+"\n")
           TextPrescription.insert(END, "Patient Name: \t\t" +PtName.get()+"\n")
           TextPrescription.insert(END, "Appointment Time: \t\t"+Apptime.get()+"\n")
           TextPrescription.insert(END, "Age: \t\t" +PtAge.get()+"\n")
           TextPrescription.insert(END, "Address: \t\t"+PatientAddress.get()+"\n")
           TextPrescription.insert(END, "Disease: \t\t"+Disease.get()+"\n")
           TextPrescription.insert(END, "Case: \t\t" +Case.get()+"\n") 
           TextPrescription.insert(END, "Benefit Card: \t\t"+BenefiCard.get()+"\n")
           TextPrescription.insert(END, "To meet Dr.: \t\t"+Drname.get()+"\n")
           TextPrescription.insert(END, "Dr. Mobile No.: \t\t"+DrMobile.get()+"\n")
           return   


        ##################Title Label#######################
        title = Label(self.root , text = "Doctor Management System", font=("monotype corsiva",42,"bold"),bd = 5,
                relief = GROOVE , bg = "#b7d8d6", fg = "black")
        title.pack(side = TOP  , fill = X)

        Manage_Frame = Frame(self.root , width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#789e9e")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root , width = 1510 , height = 55 , bd = 4 , relief = RIDGE , bg = "#eef3db")
        Button_Frame.place(x=10,y=460)


        Data_Frame = Frame(self.root , width = 1510 , height = 270 , bd = 4 , relief = RIDGE , bg = "#266E73")
        Data_Frame.place(x=10,y=510)

        Data_Frameleft = LabelFrame(Manage_Frame , width = 1050 , text = "General Information",
          font=("arial",20,"italic bold"), height = 390 , bd = 7 , pady = 1 , relief = RIDGE , bg =  "#789e9e")
        Data_Frameleft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame , width = 450 , text = "Patient Information",
        font=("arial",20,"italic bold"), height = 390 , bd = 7 , relief = RIDGE , bg =  "#789e9e")
        Data_FrameRight.pack(side = RIGHT)

        Data_Framedata = LabelFrame(Data_Frame , width = 1050 , text = "Doctor's Details",
        font=("arial",12,"italic bold"), height = 390 , bd = 4 , relief = RIDGE , bg =  "#b7d8d6")
        Data_Framedata.pack(side = LEFT) 

        DrIdlb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Doctor ID",bg = "#789e9e")
        DrIdlb1.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrIdtxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27, state = DISABLED,textvariable = DrId)
        DrIdtxt.grid(row = 0 , column = 1 , padx = 10 , pady = 5 , sticky= E) 

        DrNamelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Doctor Name",bg = "#789e9e")
        DrNamelb1.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrNametxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Drname)
        DrNametxt.grid(row = 1 , column = 1 , padx = 10 , pady = 5 , sticky= E)  

        Dateofbirthlb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Date of birth",bg = "#789e9e")
        Dateofbirthlb1.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = DateofBirth)
        Dateofbirthtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 5 , sticky= E) 

        Speslb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Specialisation",bg = "#789e9e")
        Speslb1.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Spestxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Spes)
        Spestxt.grid(row = 3 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        GovtPrilb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Govt/Private",bg = "#789e9e")
        GovtPrilb1.grid(row = 4 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        GovtPricmb= ttk.Combobox(Data_Frameleft , textvariable = GovtPri , width = 25 , state = "readonly",
        font=("arial",12,"bold"))
        GovtPricmb['values'] = ("","Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row = 4 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        Surgerieslb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Surgeries",bg = "#789e9e")
        Surgerieslb1.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Surgeriestxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Surgeries)
        Surgeriestxt.grid(row = 5 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        Experiencelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Experience",bg = "#789e9e")
        Experiencelb1.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Experiencetxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Experiences)
        Experiencetxt.grid(row = 6 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        Nurseslb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Nurses under Dr",bg = "#789e9e")
        Nurseslb1.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Nursestxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Nurses)
        Nursestxt.grid(row = 7 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        DrMobilelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Doctor Mobile No.",bg = "#789e9e")
        DrMobilelb1.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrMobiletxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = DrMobile)
        DrMobiletxt.grid(row = 8 , column = 1 , padx = 10 , pady = 5 , sticky= E)

        Datelb1 =  Label(Data_Frameleft , font =("arial",12,"bold"),width = 20,text="Data",padx=2,bg="#789e9e")
        Datelb1.grid(row= 0 , column = 2,padx = 10 , pady = 5, sticky = W)  

        Datetxt =  Label(Data_Frameleft , font =("arial",12,"bold"),width = 27,textvariable = "Date_of_Registeration")
        Datetxt.grid(row= 0 , column = 3,padx = 10 , pady =5, sticky = E)   

        PtNamelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Patient Name",padx=2,
        bg = "#789e9e")
        PtNamelb1.grid(row = 1 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        PtNametxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = PtName)
        PtNametxt.grid(row = 1 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        Apptimelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Appointment Time",padx=2,
        bg = "#789e9e")
        Apptimelb1.grid(row = 2 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Apptimetxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Apptime)
        Apptimetxt.grid(row = 2 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        PtAgelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Patient Age",padx=2,
        bg = "#789e9e")
        PtAgelb1.grid(row = 3 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        PtAgetxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = PtAge)
        PtAgetxt.grid(row = 3 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        PtAddresslb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Patient Address",bg = "#789e9e")
        PtAddresslb1.grid(row = 4 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        PtAddresstxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = PatientAddress)
        PtAddresstxt.grid(row = 4 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        PtMobilelb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Patient Mobile",bg = "#789e9e")
        PtMobilelb1.grid(row = 5 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        PtMobiletxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = PtMobile)
        PtMobiletxt.grid(row = 5 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        Diseaselb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Patient Disease",padx=2,
        bg = "#789e9e")
        Diseaselb1.grid(row = 6 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Diseasetxt = Entry(Data_Frameleft , font=("arial",12,"bold"),width =27,textvariable = Disease)
        Diseasetxt.grid(row = 6 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        Caselb1 = Label(Data_Frameleft , font =("arial",12,"bold"),width =20,text = "Case",padx=2,
        bg = "#789e9e")
        Caselb1.grid(row = 7 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Casecmb= ttk.Combobox(Data_Frameleft , textvariable = Case,width = 25, state = "readonly",
        font=("arial",12,"bold"))
        Casecmb['values'] = ("","New Case","Old case")
        Casecmb.current(0)
        Casecmb.grid(row = 7 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        BenefitCardlb1 = Label(Data_Frameleft, font = ("arial",12,"bold"),text = "Benefit Card",width = 20,padx = 10,
        bg="#789e9e")
        BenefitCardlb1.grid(row =8 , column = 2 , sticky = W)

        BenefitCardcmb= ttk.Combobox(Data_Frameleft , textvariable ="BenefitCard",width = 25, state = "readonly",
        font=("arial",12,"bold"))
        BenefitCardcmb['values'] = ("","Ayushman Card","Health card","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row = 8 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        TextPrescription = Text(Data_FrameRight , font=("arial", 12,"bold"),width= 55 , height = 17 , padx = 3 ,
        pady = 5)
        TextPrescription.grid(row = 0 , column = 0)
        TextPrescriptionData =Text(Data_Framedata , font=("arial", 12,"bold"),width= 203 , height = 12)
        TextPrescriptionData.grid(row = 1 , column = 0)

        ##############buttons################33
        Prescriptionbtn = Button(Button_Frame, text = "Patient Information", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 20,command=prescriptiondatafunc)
        Prescriptionbtn.grid(row = 0 , column = 0, padx = 12)

        DoctorDetailbtn = Button(Button_Frame, text = "Doctor's Details", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 20,command=prescriptionfunc)
        DoctorDetailbtn.grid(row = 0 , column = 1, padx = 12)

        Resetbtn = Button(Button_Frame, text = "Reset", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 20,command=resetfunc)
        Resetbtn.grid(row = 0 , column = 2, padx = 12)

        Deletebtn = Button(Button_Frame, text = "Delete", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 20,command=deletefunc)
        Deletebtn.grid(row = 0 , column = 3, padx = 12)

        Exitbtn = Button(Button_Frame, text = "Exit", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 20,command=exitbtn)
        Exitbtn.grid(row = 0 , column = 4, padx = 12)

        TextPrescriptionDatarow = Label(Data_Framedata , bg = "white", font =("arial",12,"bold"),
        text = "Date\tDoctor Id\tDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No.\tPatient Name\tCase\Pt.Age")
        TextPrescriptionDatarow.grid(row = 0 , column = 0 , sticky = W)


        
class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")


        #########variable declartion #############################
        Data_of_Registration = StringVar()
        Data_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTableNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHnumver = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()


        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return
                
        def deletefunc():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")

            TextPresciptionData.delete("1.0",END)
            return

        def resetfunc():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            return

 
        title = Label(self.root,text = "Hospital Management System",font =("monotype corsive",42,"bold"),bd = 5,
            relief = GROOVE,bg = "#2eb8b8",fg = "black")
        title.pack(side = TOP ,fill = X)


############# FRAMES #############################################3
        Manage_Frame = Frame(self.root,width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root, width = 1510 , height = 55 , bd=4, relief = RIDGE , bg = "#328695")
        Button_Frame.place(x=10,y = 460)

        Data_Frame = LabelFrame(self.root , width = 1510 , height = 270, bd = 4 , relief = RIDGE , bg ="#266e73")
        Data_Frame.place(x=10,y=510)


        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050,text = "general Informatoin", font = ("arial",20,"italic bold"), 
        height = 390, bd = 7 , relief = RIDGE , bg = "#0099CC")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width= 1050,text= "prescriptiom",
        font = ("arial",15,"italic bold"), height = 390, bd = 7 , relief = RIDGE , bg = "#0099cc")
        Data_FrameRight.pack(side = RIGHT)

        Data_Framedata = LabelFrame(Data_Frame,width = 1050 , text = "Prescription Data", font = ("arial",12,"italic bold"),
         height = 390 , bd = 4 , relief = RIDGE , bg = "#3eb7bb")
        Data_Framedata.pack(side = LEFT)

        #############LABELS ##############################
        Datelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Data",padx = 2 , bg ="#0099cc")
        Datelbl.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Datetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = "Date_of_Registration ")
        Datetxt.grid(row = 0 , column = 1 , padx = 10 , pady = 5 , sticky = E)


        ###REF
        Reflbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Reference Number", padx = 2 , bg ="#0099cc")
        Reflbl.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Reftxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = Ref)
        Reftxt.grid(row = 1 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        ###Patient ID
        PatientIdlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Id", padx = 2 , bg ="#0099cc")
        PatientIdlbl.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientIdtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = PatientId)
        PatientIdtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 5 , sticky = E)
      
        ###Patient Name
        
        PatientNamelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Id", padx = 2 , bg ="#0099cc")
        PatientNamelbl.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientNametxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = Patientname)
        PatientNametxt.grid(row = 3 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        ###Date of birth


        Dateofbirthlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Birth", padx = 2 , bg ="#0099cc")
        Dateofbirthlbl.grid(row = 4 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = Dateofbirth)
        Dateofbirthtxt.grid(row = 4 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        ###Address

        Addresslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Address", padx = 2 , bg ="#0099cc")
        Addresslbl.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Addresstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = PatientAddress)
        Addresstxt.grid(row = 5 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        ###NHS number

        NHSnumberlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "NHS unique number", padx = 2 , bg ="#0099cc")
        NHSnumberlbl.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        NHSnumbertxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = NHSnumber)
        NHSnumbertxt.grid(row = 6 , column = 1 , padx = 10 , pady = 5 , sticky = E)
 

        ######Tablet name

        Tabletlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Tablet", padx = 2 , bg ="#0099cc")
        Tabletlbl.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft , textvariable = "cmbTabletNames" ,width = 25 , state = "readonly",
            font = ("arial",12,"bold"))
        Tabletcmb['values'] = ("","Paracetamol","Dan-p","Dio-1 one","calpol","Amlodipine Besylate","Nexium",
                                   "Singular","plavix","Amoxicillian","Azithromycin","Limcin-900")
        Tabletcmb.current(0)  # we will keep index 0 when nothing is selected
        Tabletcmb.grid(row=7 , column = 1 , padx = 10 , pady =  5)


        #####No of tablets to take 

        No_of_Tabletslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "No of Tablets", padx = 2 , bg ="#0099cc")
        No_of_Tabletslbl.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        No_of_Tabletstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 27 , textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8 , column = 1 , padx = 10 , pady = 5 , sticky = E)


        ##### now we will make 2nd coloumn of other details in same frame

        ####hospital code

        HospitalCodelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Hospital Code", padx = 2 , bg ="#0099cc")
        HospitalCodelbl.grid(row = 0 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        HospitalCodetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = HospitalCode)
        HospitalCodetxt.grid(row = 0 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #####Storage advice where to keep medicine

        StorageAdvicelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "storage Advice`", padx = 2 , bg ="#0099cc")
        StorageAdvicelbl.grid(row = 1 , column = 2 , padx = 10 , pady = 5 , sticky = W)

        StorageAdvicecmb =ttk.Combobox(Data_FrameLeft , textvariable = StorageAdvice ,width = 23 , state = "readonly",
            font = ("arial",12,"bold"))
        StorageAdvicecmb['values'] = ("","Under room temp","below 5*C","below 0*C","Refrigration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row = 1 , column = 3 , padx = 10 , pady = 5 , sticky = E)


        #####Lot number of medicine

        Lot_nolbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Lot number", padx = 2 , bg ="#0099cc")
        Lot_nolbl.grid(row = 2 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Lot_noltxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = Lot)
        Lot_noltxt.grid(row = 2 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ### Issued Date

        IssuedDatelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Issue", padx = 2 , bg ="#0099cc")
        IssuedDatelbl.grid(row = 3 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        IssuedDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 3 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #####Expiry Date

        ExpiryDatelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Expiry", padx = 2 , bg ="#0099cc")
        ExpiryDatelbl.grid(row = 4 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        ExpiryDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = ExpiryDate)
        ExpiryDatetxt.grid(row = 4 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #####Daily Dose

        Dailydoselbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Dose", padx = 2 , bg ="#0099cc")
        Dailydoselbl.grid(row = 5 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Dailydosetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = "Dailydose")
        Dailydosetxt.grid(row = 5 , column = 3 , padx = 10 , pady = 5 , sticky = E)


        #####Side Effects

        SideEffectslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Side Effects", padx = 2 , bg ="#0099cc")
        SideEffectslbl.grid(row = 6 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        SideEffectstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = SideEffects)
        SideEffectstxt.grid(row = 6 , column = 3 , padx = 10 , pady = 5 , sticky = E)

      
        ####More Information Like meet dr. or any other related to patient which is important but not covered in in list

        MoreInformationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "More Information", padx = 2 , bg ="#0099cc")
        MoreInformationlbl.grid(row = 7 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        MoreInformationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = "More Information")
        MoreInformationtxt.grid(row = 7 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #####Medication(yes/no)

        Medicationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Medication", padx = 2 , bg ="#0099cc")
        Medicationlbl.grid(row = 8 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Medicationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"), width = 25 , textvariable = Medication)
        Medicationtxt.grid(row = 8 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #######Text field for prescription
        TextPresciption = Text(Data_FrameRight , font = ("arail",12,"bold"), width = 55 , height = 17 , padx = 3,
          pady = 5)
        TextPresciption.grid(row = 0 , column = 0)


        #######Text FOR prescription Date

        TextPresciptionData = Text(Data_Framedata, font = ("arail",12,"bold"), width = 203 , height = 12)
        TextPresciptionData.grid(row = 1 , column = 0)

        ######Now we will add button to our middle frame 
       
        Prescriptionbtn = Button(Button_Frame, text = "Presciption" , bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 20 )
        Prescriptionbtn.grid(row =0 , column =0 ,padx = 13)

        Reciptionbtn = Button(Button_Frame, text = "Presciption Data" , bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 20 )
        Reciptionbtn.grid(row =0 , column = 1 , padx = 13)

        Resetbtn = Button(Button_Frame, text = "Reset" , bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 20 , command = resetfunc )
        Resetbtn.grid(row =0 , column =2 ,padx = 13)

        Deletebtn = Button(Button_Frame, text = "Delete" , bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 20,command = deletefunc )
        Deletebtn.grid(row =0 , column =3 ,padx = 13)

        Exitbtn = Button(Button_Frame, text = "Exit" , bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 20, command = exitbtn)
        Exitbtn.grid(row =0 , column =4 ,padx = 16)
      

        prescriptiondatarow=Label(Data_Framedata, bg="white", font=("arial",12,"bold"),text ="Date\tReference Id\tPatient Name\tDate of Birth\tNHS Numbe\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\t)")
        prescriptiondatarow.grid(row=0, column=1, sticky=W) 


        
class windows5:
    def __init__(self,master):
        self.master= master
        self.master.title("Hospdash[META]__wormflash")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        


if __name__== "__main__":
    main()
