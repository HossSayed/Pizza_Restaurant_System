"""
Developed by Hossam Sayed, 2020
Email: hosamsayed425@gmail.com

"""

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import datetime
import time
from PizzaData import *
import os, tempfile


class ElsalamPizza():
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Restaurant Management")
        self.root.geometry("1350x690+0+0")
        self.root.config(bg='#323233')
    
        
        MainFrame = Frame(self.root, bd=10, width=1350, height=690, bg='#323233', relief=RIDGE)
        MainFrame.grid()

        TopFrame2 = Frame(MainFrame, bd=7, width=1334, height=465, bg='#4C4C4D', relief=RIDGE)
        TopFrame2.pack(side=TOP)
        TopFrame1 = Frame(MainFrame, bd=7, width=1334, height=210, bg='#4C4C4D', relief=RIDGE)
        TopFrame1.pack(side=BOTTOM)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=662, height=453, bg='#4C4C4D', relief=RIDGE)
        TopFrame2Left.pack(side=LEFT)
        TopFrame2Right = Frame(TopFrame2, bd=5, width=662, height=453, bg='#4C4C4D', relief=RIDGE)
        TopFrame2Right.pack(side=RIGHT)

        TopFrame1Left = Frame(TopFrame1, bd=5, width=656, height=205, bg='#4C4C4D', relief=RIDGE)
        TopFrame1Left.pack(side=LEFT)
        TopFrame1Right = Frame(TopFrame1, bd=5, width=662, height=205, bg='#4C4C4D', relief=RIDGE)
        TopFrame1Right.pack(side=RIGHT)

        TopFrame1Righta = Frame(TopFrame1Right, bd=2, width=660, height=130, bg='#4C4C4D', relief=RIDGE)
        TopFrame1Righta.pack(side=TOP)
        TopFrame1Rightb = Frame(TopFrame1Right, bd=2, width=660, height=65, bg='#4C4C4D', relief=RIDGE)
        TopFrame1Rightb.pack(side=BOTTOM)

#=============================================== VARIABLES ==================================================
        # Variables of the CheckButtons
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        
        # Variables of Food's quantity 
        EasternPizza = StringVar()
        ItalianPizza = StringVar()
        AlexPies = StringVar()
        PizzaRolls = StringVar()
        Shawarma = StringVar()
        Hawawshi = StringVar()
        BakedPasta = StringVar()

        # Variables of Sweets's quantity
        Cripe = StringVar()
        SweetCripe = StringVar()
        Muejanat = StringVar()
        Sweets = StringVar()
        Chocolates = StringVar()
        Patissries = StringVar()
        SweetPies = StringVar()

        # Variables of Comboboxex of the Food Type and Size
        E_PizzaType = StringVar()
        E_PizzaSize = IntVar()
        It_PizzaType = StringVar()
        It_PizzaSize = IntVar()
        Alx_PiesType = StringVar()
        Alx_PiesSize = IntVar()
        Rol_PizzaType = StringVar()
        Rol_PizzaSize = IntVar()
        Shw_Type = StringVar()
        Shw_Size = IntVar()
        Haw_Type = StringVar()
        Haw_Size = IntVar()
        BPasta_Type = StringVar()
        BPasta_Size = IntVar()

        # Variables of Comboboxes of Sweets Type and Size
        Cr_Type = StringVar()
        Cr_Size = IntVar()
        SwCr_Type = StringVar()
        SwCr_Size = IntVar()
        Muj_Type = StringVar()
        Muj_Size = IntVar()
        Swts_Type = StringVar()
        Swts_Size = IntVar()
        Choco_Type = StringVar()
        Choco_Size = IntVar()
        Patiss_Type = StringVar()
        Pattis_Size = IntVar()
        SwPies_Type = StringVar()
        SwPies_Size = IntVar()

        # Variables of Payment Division
        Paid = StringVar()
        ReqNumber = StringVar()
        SubTotal = StringVar()
        Total = StringVar()

        # Assigning the Values of Quantity of the Food and Sweets to Zeros by default
        EasternPizza.set("0")
        ItalianPizza.set("0")
        AlexPies.set("0")
        PizzaRolls.set("0")
        Shawarma.set("0")
        Hawawshi.set("0")
        BakedPasta.set("0")
        Cripe.set("0")
        SweetCripe.set("0")
        Muejanat.set("0")
        Sweets.set("0")
        Chocolates.set("0")
        Patissries.set("0")
        SweetPies.set("0")

#===================================== FUNCTIONS OF THE BUTTONS ==============================================================
        # Exit Function
        def Exit():
                iExit = tkinter.messagebox.askyesno(" Pizza Restaurant Management  ", " Do you want to exit from the system?                     ")
                if iExit > 0:
                        root.destroy()
                        return
        
        # Print Function
        def iPrint():
            q = self.txtReceipt.get("1.0", "end -1c")
            filename = tempfile.mktemp(".doc")
            open (filename, "w").write(q)
            os.startfile(filename, "print")

        # Total Cost Function
        def TotalCost():
                # Get the Sum of the Required Quantity
                a = int(EasternPizza.get())
                b = int(ItalianPizza.get())
                c = int(AlexPies.get())
                d = int(PizzaRolls.get())
                e = int(Shawarma.get())
                f = int(Hawawshi.get())
                g = int(BakedPasta.get())
                h = int(Cripe.get())
                i = int(SweetCripe.get())
                j = int(Muejanat.get())
                k = int(Sweets.get())
                l = int(Chocolates.get())
                m = int(Patissries.get())
                n = int(SweetPies.get())
                rn = a + b + c + d + e + f + g + h + i + j + k + l + m + n
                ReqNumber.set(rn)
                
                # Get The Size of the required food or sweets from the Size's ComboBoxes
                a1 = E_PizzaSize.get()
                b1 = It_PizzaSize.get()
                c1 = Alx_PiesSize.get()
                d1 = Rol_PizzaSize.get()
                e1 = Shw_Size.get()
                f1 = Haw_Size.get()
                g1 = BPasta_Size.get() 
                h1 = Cr_Size.get()
                i1 = SwCr_Size.get()
                j1 = Muj_Size.get()
                k1 = Swts_Size.get()
                l1 = Choco_Size.get()
                m1 = Pattis_Size.get()
                n1 = SwPies_Size.get()

                try:
                        # Calculate the Total Cost
                        t = (a*a1) + (b*b1) + (c*c1) + (d*d1) + (e*e1) + (f*f1) + (g*g1) + (h*h1) + (i*i1) + (j*j1) + (k*k1) + (l*l1) + (m*m1) + (n*n1)
                        Total.set(t)

                        # Calculate the remaining money(SubTotal) by subtracting what the client paid from total cost 
                        st = int(Paid.get()) - t
                        SubTotal.set(st)
                # Raise a warning message if the Paid box is not numeric or not empty
                except ValueError:
                        if (Paid.get() == ""):
                                pass
                        else:
                                tkinter.messagebox.showwarning(" Pizza Restaurant Management  ", "  من فضلك تاكد من أن خانة 'المبلغ المدفوع ' بها أرقام فقط أو اتركها فارغة")
                        

        # Reset Function
        def Reset():
                var1.set(0)
                var2.set(0)
                var3.set(0)
                var4.set(0)
                var5.set(0)
                var6.set(0)
                var7.set(0)
                var8.set(0)
                var9.set(0)
                var10.set(0)
                var11.set(0)
                var12.set(0)
                var13.set(0)
                var14.set(0)

                EasternPizza.set("0")
                ItalianPizza.set("0")
                AlexPies.set("0")
                PizzaRolls.set("0")
                Shawarma.set("0")
                Hawawshi.set("0")
                BakedPasta.set("0")
                Cripe.set("0")
                SweetCripe.set("0")
                Muejanat.set("0")
                Sweets.set("0")
                Chocolates.set("0")
                Patissries.set("0")
                SweetPies.set("0")

                Paid.set("")
                ReqNumber.set("")
                SubTotal.set("")
                Total.set("")
                self.txtReceipt.delete("1.0", END)

                E_PizzaType.set("")
                E_PizzaSize.set("0")
                It_PizzaType.set("")
                It_PizzaSize.set("0")
                Alx_PiesType.set("")
                Alx_PiesSize.set("0")
                Rol_PizzaType.set("")
                Rol_PizzaSize.set("0")
                Shw_Type.set("")
                Shw_Size.set("0")
                Haw_Type.set("")
                Haw_Size.set("0")
                BPasta_Type.set("")
                BPasta_Size.set("0")

                Cr_Type.set("")
                Cr_Size.set("0")
                SwCr_Type.set("")
                SwCr_Size.set("0")
                Muj_Type.set("")
                Muj_Size.set("0")
                Swts_Type.set("")
                Swts_Size.set("0")
                Choco_Type.set("")
                Choco_Size.set("0")
                Patiss_Type.set("")
                Pattis_Size.set("0")
                SwPies_Type.set("")
                SwPies_Size.set("0")

                self.txtEasternPizzaN.configure(state=DISABLED)
                self.txtItalianPizzaN.configure(state=DISABLED)
                self.txtAlexPiesN.configure(state=DISABLED)
                self.txtPizzaRollN.configure(state=DISABLED)
                self.txtShawarmaN.configure(state=DISABLED)
                self.txtHawawshiN.configure(state=DISABLED)
                self.txtBakedPastaN.configure(state=DISABLED)
                self.txtCripeN.configure(state=DISABLED)
                self.txtSweetCripeN.configure(state=DISABLED)
                self.txtMuejnatN.configure(state=DISABLED)
                self.txtSweetsN.configure(state=DISABLED)
                self.txtChocolatesN.configure(state=DISABLED)
                self.txtPattissriesN.configure(state=DISABLED)
                self.txtSweetPiesN.configure(state=DISABLED)
                self.cboEasternPizza.configure(state='disabled')
                self.cboEasternPizzaS.configure(state='disabled')
                self.cboItalianPizza.configure(state='disabled')
                self.cboItalianPizzaS.configure(state='disabled')
                self.cboPizzaRoll.configure(state='disabled')
                self.cboPizzaRollS.configure(state='disabled')
                self.cboAlexPies.configure(state='disabled')
                self.cboAlexPiesS.configure(state='disabled')
                self.cboShawarma.configure(state='disabled')
                self.cboShawarmaS.configure(state='disabled')
                self.cboHawawshi.configure(state='disabled')
                self.cboHawawshiS.configure(state='disabled')
                self.cboBakedPasta.configure(state='disabled')
                self.cboBakedPastaS.configure(state='disabled')
                self.cboCripe.configure(state='disabled')
                self.cboCripeS.configure(state='disabled')
                self.cboSweetCripe.configure(state='disabled')
                self.cboSweetCripeS.configure(state='disabled')
                self.cboMuejnat.configure(state='disabled')
                self.cboMuejnatS.configure(state='disabled')
                self.cboSweets.configure(state='disabled')
                self.cboSweetsS.configure(state='disabled')
                self.cboChocolates.configure(state='disabled')
                self.cboChocolatesS.configure(state='disabled')
                self.cboPattissries.configure(state='disabled')
                self.cboPattissriesS.configure(state='disabled')
                self.cboSweetPies.configure(state='disabled')
                self.cboSweetPiesS.configure(state='disabled')        

#================================== DISABLE THE COMBOBOXES AND TEXTBOXES IF THE CHECKBUTTON IS NOT SELECTED =========================
        def ch_EasternPizza():
                if (var1.get() == 1):
                        self.txtEasternPizzaN.configure(state=NORMAL)
                        self.txtEasternPizzaN.delete('0', END)
                        EasternPizza.set("")
                        self.cboEasternPizza.configure(state='readonly')
                        self.cboEasternPizzaS.configure(state='readonly')
                elif (var1.get() == 0):
                        self.txtEasternPizzaN.configure(state=DISABLED)
                        EasternPizza.set("0")
                        self.cboEasternPizza.configure(state='disabled')
                        self.cboEasternPizzaS.configure(state='disabled')
                        E_PizzaType.set("")
                        E_PizzaSize.set("0")
                                 
        def ch_ItalianPizza():
                if (var2.get() == 1):
                        self.txtItalianPizzaN.configure(state=NORMAL)
                        self.txtItalianPizzaN.delete('0', END)
                        ItalianPizza.set("")
                        self.cboItalianPizza.configure(state='readonly')
                        self.cboItalianPizzaS.configure(state='readonly')
                elif (var2.get() == 0):
                        self.txtItalianPizzaN.configure(state=DISABLED)
                        ItalianPizza.set("0")
                        self.cboItalianPizza.configure(state='disabled')
                        self.cboItalianPizzaS.configure(state='disabled')
                        It_PizzaType.set("")
                        It_PizzaSize.set("0")

        def ch_PizzaRoll():
                if (var3.get() == 1):
                        self.txtPizzaRollN.configure(state=NORMAL)
                        self.txtPizzaRollN.delete('0', END)
                        PizzaRolls.set("")
                        self.cboPizzaRoll.configure(state='readonly')
                        self.cboPizzaRollS.configure(state='readonly')

                elif (var3.get() == 0):
                        self.txtPizzaRollN.configure(state=DISABLED)
                        PizzaRolls.set("0")
                        self.cboPizzaRoll.configure(state='disabled')
                        self.cboPizzaRollS.configure(state='disabled')
                        Rol_PizzaSize.set("")
                        Rol_PizzaType.set("0")

        def ch_AlexPies():
                if (var4.get() == 1):
                        self.txtAlexPiesN.configure(state=NORMAL)
                        self.txtAlexPiesN.delete('0', END)
                        AlexPies.set("")
                        self.cboAlexPies.configure(state='readonly')
                        self.cboAlexPiesS.configure(state='readonly')
                elif (var4.get() == 0):
                        self.txtAlexPiesN.configure(state=DISABLED)
                        AlexPies.set("0")
                        self.cboAlexPies.configure(state='disabled')
                        self.cboAlexPiesS.configure(state='disabled')
                        Alx_PiesType.set("")
                        Alx_PiesSize.set("0")

        def ch_Shawrma():
                if (var5.get() == 1):
                        self.txtShawarmaN.configure(state=NORMAL)
                        self.txtShawarmaN.delete('0', END)
                        Shawarma.set("")
                        self.cboShawarma.configure(state='readonly')
                        self.cboShawarmaS.configure(state='readonly')
                elif (var5.get() == 0):
                        self.txtShawarmaN.configure(state=DISABLED)
                        Shawarma.set("0")
                        self.cboShawarma.configure(state='disabled')
                        self.cboShawarmaS.configure(state='disabled')
                        Shw_Type.set("")
                        Shw_Size.set("0")

        def ch_Hawawshi():
                if (var6.get() == 1):
                        self.txtHawawshiN.configure(state=NORMAL)
                        self.txtHawawshiN.delete('0', END)
                        Hawawshi.set("")
                        self.cboHawawshi.configure(state='readonly')
                        self.cboHawawshiS.configure(state='readonly')
                elif (var6.get() == 0):
                        self.txtHawawshiN.configure(state=DISABLED)
                        Hawawshi.set("0")
                        self.cboHawawshi.configure(state='disabled')
                        self.cboHawawshiS.configure(state='disabled')
                        Haw_Type.set("")
                        Haw_Size.set("0")

        def ch_BakedPasta():
                if (var7.get() == 1):
                        self.txtBakedPastaN.configure(state=NORMAL)
                        self.txtBakedPastaN.delete('0', END)
                        BakedPasta.set("")
                        self.cboBakedPasta.configure(state='readonly')
                        self.cboBakedPastaS.configure(state='readonly')
                elif (var7.get() == 0):
                        self.txtBakedPastaN.configure(state=DISABLED)
                        BakedPasta.set("0")
                        self.cboBakedPasta.configure(state='disabled')
                        self.cboBakedPastaS.configure(state='disabled')
                        BPasta_Type.set("")
                        BPasta_Size.set("0")

        def ch_Cripe():
                if (var8.get() == 1):
                        self.txtCripeN.configure(state=NORMAL)
                        self.txtCripeN.delete('0', END)
                        Cripe.set("")
                        self.cboCripe.configure(state='readonly')
                        self.cboCripeS.configure(state='readonly')
                elif (var8.get() == 0):
                        self.txtCripeN.configure(state=DISABLED)
                        Cripe.set("0")
                        self.cboCripe.configure(state='disabled')
                        self.cboCripeS.configure(state='disabled')
                        Cr_Type.set("")
                        Cr_Size.set("0")

        def ch_SweetCripe():
                if (var9.get() == 1):
                        self.txtSweetCripeN.configure(state=NORMAL)
                        self.txtSweetCripeN.delete('0', END)
                        SweetCripe.set("")
                        self.cboSweetCripe.configure(state='readonly')
                        self.cboSweetCripeS.configure(state='readonly')
                elif (var9.get() == 0):
                        self.txtSweetCripeN.configure(state=DISABLED)
                        SweetCripe.set("0")
                        self.cboSweetCripe.configure(state='disabled')
                        self.cboSweetCripeS.configure(state='disabled')
                        SwCr_Type.set("")
                        SwCr_Size.set("0")

        def ch_Muejanat():
                if (var10.get() == 1):
                        self.txtMuejnatN.configure(state=NORMAL)
                        self.txtMuejnatN.delete('0', END)
                        Muejanat.set("")
                        self.cboMuejnat.configure(state='readonly')
                        self.cboMuejnatS.configure(state='readonly')
                elif (var10.get() == 0):
                        self.txtMuejnatN.configure(state=DISABLED)
                        Muejanat.set("0")
                        self.cboMuejnat.configure(state='disabled')
                        self.cboMuejnatS.configure(state='disabled')
                        Muj_Type.set("")
                        Muj_Size.set("0")

        def ch_Sweets():
                if (var11.get() == 1):
                        self.txtSweetsN.configure(state=NORMAL)
                        self.txtSweetsN.delete('0', END)
                        Sweets.set("")
                        self.cboSweets.configure(state='readonly')
                        self.cboSweetsS.configure(state='readonly')
                elif (var11.get() == 0):
                        self.txtSweetsN.configure(state=DISABLED)
                        Sweets.set("0")
                        self.cboSweets.configure(state='disabled')
                        self.cboSweetsS.configure(state='disabled')
                        Swts_Type.set("")
                        Swts_Size.set("0")

        def ch_Chocolates():
                if (var12.get() == 1):
                        self.txtChocolatesN.configure(state=NORMAL)
                        self.txtChocolatesN.delete('0', END)
                        Chocolates.set("")
                        self.cboChocolates.configure(state='readonly')
                        self.cboChocolatesS.configure(state='readonly')
                elif (var12.get() == 0):
                        self.txtChocolatesN.configure(state=DISABLED)
                        Chocolates.set("0")
                        self.cboChocolates.configure(state='disabled')
                        self.cboChocolatesS.configure(state='disabled')
                        Choco_Type.set("")
                        Choco_Size.set("0")

        def ch_Patisseries():
                if (var13.get() == 1):
                        self.txtPattissriesN.configure(state=NORMAL)
                        self.txtPattissriesN.delete('0', END)
                        Patissries.set("")
                        self.cboPattissries.configure(state='readonly')
                        self.cboPattissriesS.configure(state='readonly')
                elif (var13.get() == 0):
                        self.txtPattissriesN.configure(state=DISABLED)
                        Patissries.set("0")
                        self.cboPattissries.configure(state='disabled')
                        self.cboPattissriesS.configure(state='disabled')
                        Patiss_Type.set("")
                        Pattis_Size.set("0")

        def ch_SweetPies():
                if (var14.get() == 1):
                        self.txtSweetPiesN.configure(state=NORMAL)
                        self.txtSweetPiesN.delete('0', END)
                        SweetPies.set("")
                        self.cboSweetPies.configure(state='readonly')
                        self.cboSweetPiesS.configure(state='readonly')
                elif (var14.get() == 0):
                        self.txtSweetPiesN.configure(state=DISABLED)
                        SweetPies.set("0")
                        self.cboSweetPies.configure(state='disabled')
                        self.cboSweetPiesS.configure(state='disabled')
                        SwPies_Type.set("")
                        SwPies_Size.set("0")

#============================== FUNCTIONS TO POPULATE THE COMBOBOXES OF SIZE BASED ON COMBOBOXES OF TYPE =========================================         
        def iEaster_Pizz(event):
                EpType = str(self.cboEasternPizza.get())
                if EpType == E1 or EpType==E3:
                        size_EP=['30','40','50']
                elif EpType == E2:
                        size_EP=['25','35','50']
                elif EpType == E4:
                        size_EP=['32','45','55']
                elif EpType == E5 or EpType == E7 or EpType == E8:
                        size_EP=['30','45','60']
                elif EpType == E6:
                        size_EP=['40','50','60']
                elif EpType == E9 or EpType == E10:
                        size_EP=['35','45','60']
                elif EpType == E11:
                        size_EP=['35','45','55']
                elif EpType == E12 or EpType == E13:
                        size_EP=['40','55','65']
                elif EpType == E14:
                        size_Ep=['35','50','65']
                elif EpType == E15:
                        size_Ep=['40','50','65']
                elif EpType == E16:
                        size_Ep=['33','45','60']
                elif EpType == E17:
                        size_EP =['40','52','65']
                elif EpType == E18:
                        size_Ep =['55','65']
                self.cboEasternPizzaS.config(values=size_EP)

        def iItalian_Pizza(event):
                IpType = str(self.cboItalianPizza.get())
                if IpType == I1 or IpType == I3 or IpType == I5:
                        size_Ip=['30','40','50']
                elif IpType == I2 or IpType == I4 or IpType == I6:
                        size_Ip=['25','35','50']
                elif IpType == I7 or IpType == I9 or IpType == I11:
                        size_Ip=['35','45','55']
                elif IpType == I8 or IpType == I10 or IpType == I12:
                        size_Ip=['35','40','60']
                elif IpType == I13 or IpType == I15 or IpType == I17 or IpType == I19:
                        size_Ip=['40','50','65']
                elif IpType == I14 or IpType == I16 or IpType == I18:
                        size_Ip=['25','45','65']             
                self.cboItalianPizzaS.config(values=size_Ip)

        def iPizza_Roll(event):
                PrType = str(self.cboPizzaRoll.get())
                if PrType == PR1 or PrType == PR3:
                        size_Pr=['30','40','50']
                elif PrType == PR2 or PrType == PR4:
                        size_Pr=['25','35','50']
                elif PrType== PR5 or PrType == PR7:
                        size_Pr=['35','45','55']
                elif PrType == PR6 or PrType == PR8:
                        size_Pr=['35','40','60']
                elif PrType == PR9 or PrType == PR11:
                        size_Pr=['40','50','65']
                elif PrType == PR10 or PrType == PR12:
                        size_Pr=['25','45','65']              
                self.cboPizzaRollS.config(values=size_Pr)

        def iAlex_Pies(event):
                ApType = str(self.cboAlexPies.get())
                if ApType == AP1 or ApType == AP3 or ApType == AP5:
                        size_Ap=['30','40','50']
                elif ApType == AP2 or ApType == AP4 or ApType == AP6:
                        size_Ap=['25','35','50']
                elif ApType == AP7 or ApType == AP9 or ApType == AP11:
                        size_Ap=['35','45','55']
                elif ApType == AP8 or ApType == AP10 or ApType == AP12:
                        size_Ap=['35','40','60']
                elif ApType == AP13 or ApType == AP15 or ApType == AP17 or ApType == AP19:
                        size_Ap=['40','50','65']
                elif ApType == AP14 or ApType == AP16 or ApType == AP18:
                        size_Ap=['25','45','65']              
                self.cboAlexPiesS.config(values=size_Ap)

        def iShawrma(event):
                ShType = str(self.cboShawarma.get())
                if ShType == SH1 or ShType == SH3:
                        size_Sh=['30','40','50']
                elif ShType == SH2 or ShType == SH4:
                        size_Sh=['35','45','55']
                elif ShType == SH5 or ShType == SH6:
                        size_Sh=['40','50','65']
                self.cboShawarmaS.config(values=size_Sh)

        def iHawashi(event):
                HwType = str(self.cboHawawshi.get())
                if HwType == HW1 or HwType == HW3 or HwType == HW4:
                        size_hw = ['30','40','50']
                elif HwType == HW2 or HwType == HW5:
                        size_hw = ['35','45','55']
                self.cboHawawshiS.config(values=size_hw)

        def iBaked_Pasta(event):
                BpType = str(self.cboBakedPasta.get())
                if BpType == BP1 or BpType == BP3 or BpType == BP5:
                        size_bp = ['25','35','50']
                elif BpType == BP2 or BpType == BP4 or BpType == BP6:
                        size_bp = ['30','40','50']
                elif BpType == BP7 or BpType == BP8:
                        size_bp = ['40','50','65']
                self.cboBakedPastaS.config(values=size_bp)

        def iCripe(event):
                cType = str(self.cboCripe.get())
                if cType == C1 or cType == C3 or cType == C5 or cType == C7:
                        size_c = ['30','40','50']
                elif cType == C2 or cType == C4 or cType == C6 or cType == C8:
                        size_c = ['25','45','65']
                elif cType == C9 or cType == C11 or cType == C13 or cType == C15:
                        size_c = ['35','45','55']
                elif cType == C10 or cType == C12 or cType == C14 or cType == C16:
                        size_c = ['40','50','65']
                elif cType == C17 or cType == C19 or cType == C21 or cType == C23 or cType == C25:
                        size_c = ['35','45','55']
                elif cType == C18 or cType == C20 or cType == C22 or cType == C24:
                        size_c = ['55','65']
                self.cboCripeS.config(values=size_c)

        def iSweet_cripe(event):
                scType = str(self.cboSweetCripe.get())
                if scType == SC1:
                        size_sw = ['25','45','65']
                elif scType == SC2:
                        size_sw = ['30','40','50']
                self.cboSweetCripeS.config(values=size_sw)

        def iMujnat(event):
                mType = str(self.cboMuejnat.get())
                if mType == M1 or mType == M3 or mType == M5:
                        size_m = ['25','45','65']
                elif mType == M2 or mType == M4:
                        size_m = ['30','40','50']
                self.cboMuejnatS.config(values=size_m)

        def iSweets(event):
                sType = str(self.cboSweets.get())
                if sType == S1 or sType == S3 or sType == S5:
                        size_s = ['25','45','65']
                elif sType == S2 or sType == S4 or sType == S6:
                        size_s = ['35','45','55']
                elif sType == S7 or sType == S8:
                        size_s = ['30','40','50']
                self.cboSweetsS.config(values=size_s)

        def iChocolates(event):
                chType = str(self.cboChocolates.get())
                if chType == CH1 or chType == CH3:
                        size_ch = ['25','45','65']
                elif chType == CH2 or chType == CH4:
                        size_ch = ['30','40','50']
                self.cboChocolatesS.config(values=size_ch)   

        def iPattissries(event):
                psType = str(self.cboPattissries.get())
                if psType == P1 or psType == P3 or psType == P5:
                        size_ps = ['25','45','65']
                elif psType == P2 or psType == P4 or psType == P6:
                        size_ps = ['30','40','50']
                self.cboPattissriesS.config(values=size_ps)

        def iSweet_pies(event):
                spType = str(self.cboSweetPies.get())
                if spType == SP1 or spType == SP3 or spType == SP5:
                        size_sp = ['30','40','50']
                elif spType == SP2 or spType == SP4 or spType == SP6:
                        size_sp = ['25','45','65']
                elif spType == SP7 or spType == SP9 or spType == SP10:
                        size_sp = ['35','45','55']
                self.cboSweetPiesS.config(values=size_sp)

#================================================= TOP FRAME 2 RIGHT =====================================================       
        
        # Eastern Pizza
        self.chEasternPizza = Checkbutton(TopFrame2Right, variable=var1, onvalue=1, offvalue=0, command=ch_EasternPizza, text=" بيتزا شرقي ",  font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chEasternPizza.grid(row=1,column=3, pady=7) 
  
        self.cboEasternPizza = ttk.Combobox(TopFrame2Right, state='disabled', font=('calibri', 12), justify=CENTER, textvariable=E_PizzaType)
        self.cboEasternPizza.bind("<<ComboboxSelected>>", iEaster_Pizz)
        self.cboEasternPizza.option_add('*TCombobox*Listbox.Justify', 'center') 
        self.cboEasternPizza['value'] = ('', E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18)
        self.cboEasternPizza.current(0)
        self.cboEasternPizza.grid(row=1, column=2, padx=7, pady=7)

        self.cboEasternPizzaS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=E_PizzaSize)
        self.cboEasternPizzaS.grid(row=1, column=1, padx=7, pady=7)
            
        self.txtEasternPizzaN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=EasternPizza, justify=CENTER)
        self.txtEasternPizzaN.grid(row=1, column=0, padx=7, pady=7)
               
        # Italian Pizza
        self.chItalianPizza = Checkbutton(TopFrame2Right, variable=var2, onvalue=1, offvalue=0, command=ch_ItalianPizza, text=" بيتزا إيطالي", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chItalianPizza.grid(row=2,column=3, pady=7)  

        self.cboItalianPizza = ttk.Combobox(TopFrame2Right, state='disabled', font=('calibri', 12),justify=CENTER, textvariable=It_PizzaType)
        self.cboItalianPizza.bind("<<ComboboxSelected>>", iItalian_Pizza)
        self.cboItalianPizza['value'] = ('', I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,I18,I19)
        self.cboItalianPizza.current(0)
        self.cboItalianPizza.grid(row=2, column=2, padx=7, pady=7)

        self.cboItalianPizzaS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=It_PizzaSize)
        self.cboItalianPizzaS.grid(row=2, column=1, padx=7, pady=7)
        
        self.txtItalianPizzaN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=ItalianPizza, justify=CENTER)
        self.txtItalianPizzaN.grid(row=2, column=0, padx=7, pady=7)

        # Pizza Roll
        self.chPizzaRoll = Checkbutton(TopFrame2Right, variable=var3, onvalue=1, offvalue=0, command=ch_PizzaRoll,text=" بيتزا صواريخ ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chPizzaRoll.grid(row=3,column=3,pady=7)  

        self.cboPizzaRoll = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Rol_PizzaType)
        self.cboPizzaRoll.bind("<<ComboboxSelected>>", iPizza_Roll)
        self.cboPizzaRoll['value'] = ('',PR1,PR2,PR3,PR4,PR5,PR6,PR7,PR8,PR9,PR10,PR11,PR12)
        self.cboPizzaRoll.current(0)
        self.cboPizzaRoll.grid(row=3, column=2, padx=7, pady=7)

        self.cboPizzaRollS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Rol_PizzaSize)
        self.cboPizzaRollS.grid(row=3, column=1, padx=7, pady=7)
        
        self.txtPizzaRollN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=PizzaRolls, justify=CENTER)
        self.txtPizzaRollN.grid(row=3, column=0, padx=7, pady=7)

        # Alex Pies
        self.chAlexPies = Checkbutton(TopFrame2Right, variable=var4, onvalue=1, offvalue=0, command=ch_AlexPies, text=" فطائر إسكندراني ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chAlexPies.grid(row=4,column=3, pady=7)  

        self.cboAlexPies= ttk.Combobox(TopFrame2Right, state='disabled', font=('calibri', 12), textvariable=Alx_PiesType, justify=CENTER)
        self.cboAlexPies.bind("<<ComboboxSelected>>", iAlex_Pies)
        self.cboAlexPies['value'] = ('', AP1,AP2,AP3,AP4,AP5,AP6,AP6,AP7,AP8,AP9,AP10,AP11,AP12,AP13,AP14,AP15,AP16,AP17,AP18,AP19)
        self.cboAlexPies.current(0)
        self.cboAlexPies.grid(row=4, column=2, padx=7, pady=7)

        self.cboAlexPiesS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Alx_PiesSize)
        self.cboAlexPiesS.grid(row=4, column=1, padx=7, pady=7)
        
        self.txtAlexPiesN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=AlexPies, justify=CENTER)
        self.txtAlexPiesN.grid(row=4, column=0, padx=7, pady=7)

        # Shawarma
        self.chShawarma = Checkbutton(TopFrame2Right, variable=var5, onvalue=1, offvalue=0, command=ch_Shawrma, text=" شاورما السلام ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chShawarma.grid(row=5,column=3,pady=7) 

        self.cboShawarma= ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Shw_Type)
        self.cboShawarma.bind("<<ComboboxSelected>>", iShawrma)
        self.cboShawarma['value'] = ('', SH1,SH2,SH3,SH4,SH5,SH6)
        self.cboShawarma.current(0)
        self.cboShawarma.grid(row=5, column=2, padx=7, pady=7)

        self.cboShawarmaS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Shw_Size)
        self.cboShawarmaS.grid(row=5, column=1, padx=7, pady=7)
        
        self.txtShawarmaN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Shawarma, justify=CENTER)
        self.txtShawarmaN.grid(row=5, column=0, padx=7, pady=7)

        # Hawawshi
        self.chHawawshi = Checkbutton(TopFrame2Right, variable=var6, onvalue=1, offvalue=0, command=ch_Hawawshi, text=" حواوشي إسكندراني ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chHawawshi.grid(row=6,column=3, pady=7)  

        self.cboHawawshi = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Haw_Type)
        self.cboHawawshi.bind("<<ComboboxSelected>>", iHawashi)
        self.cboHawawshi['value'] = ('', HW1,HW2,HW3,HW4,HW5)
        self.cboHawawshi.current(0)
        self.cboHawawshi.grid(row=6, column=2, padx=7, pady=7)

        self.cboHawawshiS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Haw_Size)
        self.cboHawawshiS.grid(row=6, column=1, padx=7, pady=7)
        
        self.txtHawawshiN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Hawawshi, justify=CENTER)
        self.txtHawawshiN.grid(row=6, column=0, padx=7, pady=7)

        # Baked Pasta
        self.chBakedPasta = Checkbutton(TopFrame2Right, variable=var7, onvalue=1, offvalue=0, command=ch_BakedPasta, text=" مكرونة فرن ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chBakedPasta.grid(row=7,column=3, pady=17) 

        self.cboBakedPasta= ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=BPasta_Type)
        self.cboBakedPasta.bind("<<ComboboxSelected>>", iBaked_Pasta)
        self.cboBakedPasta['value'] = ('', BP1,BP2,BP3,BP4,BP5,BP6,BP7,BP8,BP9)
        self.cboBakedPasta.current(0)
        self.cboBakedPasta.grid(row=7, column=2, padx=7, pady=7)

        self.cboBakedPastaS = ttk.Combobox(TopFrame2Right, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=BPasta_Size)
        self.cboBakedPastaS.grid(row=7, column=1, padx=7, pady=7)
        
        self.txtBakedPastaN = Entry(TopFrame2Right, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=BakedPasta, justify=CENTER)
        self.txtBakedPastaN.grid(row=7, column=0, padx=7, pady=7) 

#================================================= TOP FRAME 2 LEFT =====================================================
        # Cripe 
        self.chCripe = Checkbutton(TopFrame2Left, variable=var8, onvalue=1, offvalue=0, command=ch_Cripe, text=" كريب حادق ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chCripe.grid(row=1,column=3, pady=7) 
  
        self.cboCripe = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Cr_Type)
        self.cboCripe.bind("<<ComboboxSelected>>", iCripe)
        self.cboCripe['value'] = ('', C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,C25)
        self.cboCripe.current(0)
        self.cboCripe.grid(row=1, column=2, padx=7, pady=7)

        self.cboCripeS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Cr_Size)
        self.cboCripeS.grid(row=1, column=1, padx=7, pady=7)
        
        self.txtCripeN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Cripe, justify=CENTER)
        self.txtCripeN.grid(row=1, column=0, padx=7, pady=7)
               
        # Sweet Cripe
        self.chSweetCripe = Checkbutton(TopFrame2Left, variable=var9, onvalue=1, offvalue=0, command=ch_SweetCripe, text=" كريب حلو ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chSweetCripe.grid(row=2,column=3, pady=7)  

        self.cboSweetCripe = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=SwCr_Type)
        self.cboSweetCripe.bind("<<ComboboxSelected>>", iSweet_cripe)
        self.cboSweetCripe['value'] = ('', SC1,SC2)
        self.cboSweetCripe.current(0)
        self.cboSweetCripe.grid(row=2, column=2, padx=7, pady=7)

        self.cboSweetCripeS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=SwCr_Size)
        self.cboSweetCripeS.grid(row=2, column=1, padx=7, pady=7)
        
        self.txtSweetCripeN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=SweetCripe, justify=CENTER)
        self.txtSweetCripeN.grid(row=2, column=0, padx=7, pady=7)

        # Muejnat
        self.chMuejnat = Checkbutton(TopFrame2Left, variable=var10, onvalue=1, offvalue=0, command=ch_Muejanat, text=" معجنات ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chMuejnat.grid(row=3,column=3,pady=7)  

        self.cboMuejnat = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Muj_Type)
        self.cboMuejnat.bind("<<ComboboxSelected>>", iMujnat) 
        self.cboMuejnat['value'] = ('', M1,M2,M3,M4,M5)
        self.cboMuejnat.current(0)
        self.cboMuejnat.grid(row=3, column=2, padx=7, pady=7)

        self.cboMuejnatS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Muj_Size)
        self.cboMuejnatS.grid(row=3, column=1, padx=7, pady=7)
        
        self.txtMuejnatN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Muejanat, justify=CENTER)
        self.txtMuejnatN.grid(row=3, column=0, padx=7, pady=7)

        # Sweets
        self.chSweets = Checkbutton(TopFrame2Left, variable=var11, onvalue=1, offvalue=0, command=ch_Sweets, text=" حلويات ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chSweets.grid(row=4,column=3, pady=7)  

        self.cboSweets = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Swts_Type)
        self.cboSweets.bind("<<ComboboxSelected>>", iSweets)
        self.cboSweets['value'] = ('', S1,S2,S3,S4,S5,S6,S7,S8)
        self.cboSweets.current(0)
        self.cboSweets.grid(row=4, column=2, padx=7, pady=7)

        self.cboSweetsS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Swts_Size)
        self.cboSweetsS.grid(row=4, column=1, padx=7, pady=7)
        
        self.txtSweetsN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Sweets, justify=CENTER)
        self.txtSweetsN.grid(row=4, column=0, padx=7, pady=7)

        # Chocolates
        self.chChocolates = Checkbutton(TopFrame2Left, variable=var12, onvalue=1, offvalue=0, command=ch_Chocolates, text=" شيكولاتات ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chChocolates.grid(row=5,column=3,pady=7) 

        self.cboChocolates = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=Choco_Type)
        self.cboChocolates.bind("<<ComboboxSelected>>", iChocolates) 
        self.cboChocolates['value'] = ('', CH1,CH2,CH3,CH4)
        self.cboChocolates.current(0)
        self.cboChocolates.grid(row=5, column=2, padx=7, pady=7)

        self.cboChocolatesS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Choco_Size)
        self.cboChocolatesS.grid(row=5, column=1, padx=7, pady=7)
        
        self.txtChocolatesN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Chocolates, justify=CENTER)
        self.txtChocolatesN.grid(row=5, column=0, padx=7, pady=7)

        # Pattissries
        self.chPattissries = Checkbutton(TopFrame2Left, variable=var13, onvalue=1, offvalue=0, command=ch_Patisseries, text=" مخبوزات ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chPattissries.grid(row=6,column=3, pady=7)  

        self.cboPattissries = ttk.Combobox(TopFrame2Left, state='disabled',justify=CENTER, font=('calibri', 12), textvariable=Patiss_Type)
        self.cboPattissries.bind("<<ComboboxSelected>>", iPattissries)
        self.cboPattissries['value'] = ('', P1,P2,P3,P4,P5,P6)
        self.cboPattissries.current(0)
        self.cboPattissries.grid(row=6, column=2, padx=7, pady=7)

        self.cboPattissriesS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=Pattis_Size)
        self.cboPattissriesS.grid(row=6, column=1, padx=7, pady=7)
        
        self.txtPattissriesN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=Patissries, justify=CENTER)
        self.txtPattissriesN.grid(row=6, column=0, padx=7, pady=7)

        # Sweet Pies
        self.chSweetPies = Checkbutton(TopFrame2Left, variable=var14, onvalue=1, offvalue=0, command=ch_SweetPies, text=" فطائر حلوة ", font=('arial', 18, 'bold'), width=12, bg='#7E7E81')
        self.chSweetPies.grid(row=7,column=3, pady=17) 

        self.cboSweetPies = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 12), textvariable=SwPies_Type)
        self.cboSweetPies.bind("<<ComboboxSelected>>", iSweet_pies)
        self.cboSweetPies['value'] = ('', SP1,SP2,SP3,SP4,SP4,SP6,SP7,SP8,SP9,SP10)
        self.cboSweetPies.current(0)
        self.cboSweetPies.grid(row=7, column=2, padx=7, pady=7)

        self.cboSweetPiesS = ttk.Combobox(TopFrame2Left, state='disabled', justify=CENTER, font=('calibri', 8,'bold'), textvariable=SwPies_Size)
        self.cboSweetPiesS.grid(row=7, column=1, padx=7, pady=7)
        
        self.txtSweetPiesN = Entry(TopFrame2Left, font=('arial', 10,'bold'), width=10, state=DISABLED, textvariable=SweetPies, justify=CENTER)
        self.txtSweetPiesN.grid(row=7, column=0, padx=7, pady=7)  

#================================== TOP FRAME 1 LEFT ========================================================================
        self.txtReceipt = Text(TopFrame1Left, state='disabled', font=('courier', 12), width=64, height=12)
        self.txtReceipt.grid(row=0, column=0)

#================================== TOP FRAME 1 RIGHT b ========================================================================
        # Buttons
        self.btnTotal = Button(TopFrame1Rightb, text="المبلغ الكلي", padx=25, pady=1, font=('arial', 18, 'bold'), bd=5, bg='#818183', command=TotalCost).grid(row=0, column=3, pady=1)
        self.btnPrint = Button(TopFrame1Rightb, text="   طباعة   ", padx=25, pady=1, font=('arial', 18, 'bold'), bd=5, bg='#818183', command=iPrint).grid(row=0, column=2, pady=1)
        self.btnReset = Button(TopFrame1Rightb, text="   مسح   ", padx=25, pady=1, font=('arial', 18, 'bold'), bd=5, bg='#818183', command=Reset).grid(row=0, column=1, pady=1)
        self.btnExit = Button(TopFrame1Rightb, text="   خروج   ", padx=25, pady=1, font=('arial', 18, 'bold'), bd=5, bg='#818183', command=Exit).grid(row=0, column=0, pady=1)

#================================== TOP FRAME 1 RIGHT A ========================================================================
        # Function of PlaceHolder in Paid Entry Box
        def paidText(event):
                self.txtPaid.delete(0, END)
                paidCheck = True
        paidCheck = False

        # Label and Textboxes of Payment Division
        self.lblRequiredNum = Label(TopFrame1Righta, text="العدد المطلوب", font=('arial', 18, 'bold'), bd=5, bg='#7E7E81', fg='black')
        self.lblRequiredNum.grid(row=0, column=3, padx=5, pady=17)
        self.txtRequiredNum = Entry(TopFrame1Righta, state='readonly', font=('arial', 18, 'bold'), bd=5, width=12, justify=RIGHT, textvariable=ReqNumber)
        self.txtRequiredNum.grid(row=0, column=2, padx=13, pady=17)

        self.lblPaid = Label(TopFrame1Righta, text= "المبلغ المدفوع", font=('arial', 18, 'bold'), bd=5, bg='#7E7E81', fg='black')
        self.lblPaid.grid(row=0, column=1, padx=5, pady=17)
        # This Value must be entered by the Admin(e.g. Cashier)
        self.txtPaid = Entry(TopFrame1Righta, font=('arial', 18, 'bold'), bd=5, width=12, justify=RIGHT, textvariable=Paid)
        self.txtPaid.grid(row=0, column=0, padx=13, pady=17)
        self.txtPaid.insert(0, 'أدخل المبلغ')
        self.txtPaid.bind('<Button>', paidText)

        self.lblTotal = Label(TopFrame1Righta, text= "   الحساب    ", font=('arial', 18, 'bold'), bd=5, bg='#7E7E81', fg='black')
        self.lblTotal.grid(row=1, column=3, pady=5)
        self.txtTotal = Entry(TopFrame1Righta, state='readonly', font=('arial', 18, 'bold'), bd=5, width=12, justify=RIGHT, textvariable=Total)
        self.txtTotal.grid(row=1, column=2, padx=13, pady=17)

        self.lblSubTotal = Label(TopFrame1Righta, text=" باقي الحساب ", font=('arial', 18, 'bold'), bd=5, bg='#7E7E81', fg='black')
        self.lblSubTotal.grid(row=1, column=1, padx=5, pady=17)
        self.txtSubTotal = Entry(TopFrame1Righta, state='readonly', font=('arial', 18, 'bold'), bd=5, width=12, justify=RIGHT, textvariable=SubTotal)
        self.txtSubTotal.grid(row=1, column=0, padx=13, pady=17)


if __name__ == "__main__":
    root = Tk()
    ElsalamPizza(root)
    root.mainloop()   
