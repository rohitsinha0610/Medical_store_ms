import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="",database="Project_2021")
cursor=mycon.cursor()

print("HELLO!! HAVE A GOOD DAY!!")
print("  ")
def main():
   print("Select your Choice of Action")
   print("MENU")
   print("1 Procurement")
   print("2 Sale")
   print("3 Expenditure")
   print("4 Exit")
   c=int(input("Enter your choice: "))
   if c==1:
        pcy()
   elif c==2:
        scy()
   elif c==3:
        emy()
   elif c==4:
        exit()
   else:
      print(" ")
      print("Error!!Please try again")
      print(" ")
      main()

def pcy():
    print("PROCUREMENT MENU/YEAR")
    print("1 2021")
    print("2 Back")
    print("3 Exit")
    c=int(input("Enter your choice(1|2|3): "))
    if c==1:
        pcm()
    elif c==2:
        print()#main()
    elif c==3:
        exit()
    else:
        print(" ")
        print("There is an error please try again")
        print(" ")
        pcy()
        
def pcm():
    print("PROCUREMENT MENU/MONTH")
    print(" 1.January")
    print(" 2.Febuary")
    print(" 3.March")
    print(" 4.April")
    print(" 5.May")
    print(" 6.June")
    print(" 7.July")
    print(" 8.August")
    print(" 9.September")
    print("10.October")
    print("11.November")
    print("12.December")
    print("13 Back")
    print("14 Exit")
    ch=int(input("Enter your choice(1-14): "))
    if ch==1 :
        b='procurement_jan'
        p_insert(b)
    elif ch==2 :
        b='procurement_feb'
        p_insert(b)
    elif ch==3 :
        b='procurement_march'
        p_insert(b)
    elif ch==4 :
        b='procurement_april'
        p_insert(b)
    elif ch==5 :
        b='procurement_may'
        p_insert(b)
    elif ch==6 :
        b='procurement_june'
        p_insert(b)
    elif ch==7 :
        b='procurement_july'
        p_insert(b)
    elif ch==8 :
        b='procurement_august'
        p_insert(b)
    elif ch==9 :
        b='procurement_september'
        p_insert(b)
    elif ch==10 :
        b='procurement_october'
        p_insert(b)
    elif ch==11 :
        b='procurement_november'
        p_insert(b)
    elif ch==12 :
        b='procurement_december'
        p_insert(b)
    elif ch==13:
        pcy()
    elif ch==14:
        exit()
    else:
        print(" ")
        print("There is an error please try again")
        print(" ")
        pcm()

def p_insert(a):
    d_name=input("Enter distributor name :")
    p_name=input("Enter product name :")
    Exp=input( "Enter expire date of the product in the format MM.YYYY:")
    MRP=float(input("Enter MRP of the product:"))
    Qty=int(input("Enter Quantity of the product:"))
    Amount=MRP*Qty
    print("Total Amount:",Amount)
    quere="""insert into %s
    	     values('%s','%s',%s,%s,%s,%s)"""%(a,d_name,p_name,Exp,MRP,Qty,Amount)
    cursor.execute(quere)
    mycon.commit()
    print(" ")
    print(d_name,p_name,Exp,MRP,Qty,Amount)
    query="""Select SUM(Amount)
             from %s ;""" %(a,)
    cursor.execute(query)
    data=cursor.fetchall()
    global d
    for i in data :
        d=i[0]
        print("Net procurement amount =",d)
        main()
        
def scy():
    print("SALE MENU/YEAR")
    print("1 2021")
    print("2 Back")
    print("3 Exit")
    c=int(input("Enter your choice(1|2|3): "))
    if c==1:
        scm()
    elif c==2:
        main()
    elif c==3:
        exit()
    else:
        print(" ")
        print("There is an error please try again")
        print(" ")
        scy()
   
def scm():
    print("SALE MENU/MONTH")
    print(" 1.January")
    print(" 2.Febuary")
    print(" 3.March")
    print(" 4.April")
    print(" 5.May")
    print(" 6.June")
    print(" 7.July")
    print(" 8.August")
    print(" 9.September")
    print("10.October")
    print("11.November")
    print("12.December")
    print("13 Back")
    print("14 Exit")
    ch=int(input("Enter your choice(1-14): "))
    if ch==1:
      b='sale_medicine_jan'
      s_insert(b)
    elif ch==2:
      b='sale_medicine_feb'
      s_insert(b)
    elif ch==3:
      b='sale_medicine_march'
      s_insert(b)
    elif ch==4:
      b='sale_medicine_april'
      s_insert(b)
    elif ch==5:
      b='sale_medicine_may'
      s_insert(b)
    elif ch==6:
      b='sale_medicine_june'
      s_insert(b)
    elif ch==7:
      b='sale_medicine_july'
      s_insert(b)
    elif ch==8:
      b='sale_medicine_august'
      s_insert(b)
    elif ch==9:
      b='sale_medicine_sept'
      s_insert(b)
    elif ch==10:
      b='sale_medicine_octb'
      s_insert(b)
    elif ch==11:
      b='sale_medicine_nov'
      s_insert(b)
    elif ch==12:
      b='sale_medicine_dec'
      s_insert(b)
    elif ch==13:
      scy()
    elif ch==14:
      exit()
    else:
      print(" ")
      print("There is an error please try again")
      print(" ")
      scm()
		
def s_insert(a):
    m_name=input("Enter medicine name :")
    sp_s=float(input("Enter sellingprice of product :"))
    quantity=int(input("Enter quantity of the product :"))
    
    dt=input("Enter present date in the format YYYYMMDD :")
    p_rofit=sp_s*quantity
    print("Total sale of the product:",p_rofit)
    quere="""insert into %s
    	     values('%s',%s,%s,%s,%s)"""%(a,m_name,sp_s,quantity,dt,p_rofit)
    cursor.execute(quere)
    mycon.commit()
    print(m_name,sp_s,quantity,dt,p_rofit)
    query="""Select SUM(p_rofit)
                 from %s ;""" %(a,)
    cursor.execute(query)
    global k
    data=cursor.fetchall()
    for j in data :
          k=j[0]
          print("Net sale amount =",k)
          main()

def emy():
        print("EXPENDITURE MENU/YEAR")
        print("1 2021")
        print("2 Back")
        print("3 Exit")
        c=int(input("Enter choice: "))
        if c==1:
            ecm()
        elif c==2:
            main()
        elif c==3:
            exit()
        else:
            print("Error")
            emy()
            
def ecm():
    print("EXPENDITURE MENU/MONTH")
    print("1 January")
    print("2 Febuary")
    print("3 March")
    print("4 April")
    print("5 May")
    print("6 June")
    print("7 July")
    print("8 August")
    print("9 September")
    print("10 October")
    print("11 November")
    print("12 December")
    print("13 Back")
    print("14 Exit")
    c=int(input("Enter your choice(1|2|3|4): "))
    if c==1:
        b="expenditure_jan"
        e_insert(b)
    elif c==2:
        b="expenditure_feb"
        e_insert(b)
    elif c==3:
        b="expenditure_march"
        e_insert(b)
    elif c==4:
        b="expenditure_april"
        e_insert(b)
    elif c==5:
        b="expenditure_may"
        e_insert(b)
    elif c==6:
        b="expenditure_june"
        e_insert(b)
    elif c==7:
        b="expenditure_july"
        e_insert(b)
    elif c==8:
        b="expenditure_aug"
        e_insert(b)
    elif c==9:
        b="expenditure_sept"
        e_insert(b)
    elif c==10:
        b="expenditure_oct"
        e_insert(b)
    elif c==11:
        b="expenditure_nov"
        e_insert(b)
    elif c==12:
        b="expenditure_dec"
        e_insert(b)
    elif c==13:
        emy()
    elif c==4:
        exit
    else:
        print("There is an error please try again")
        ecm()

def e_insert(a):
    r=float(input("Enter the rent: "))
    es=float(input("Enter the employee salary: "))
    oe=float(input("Enter other expenditurte: "))
    tots=r+es+oe
    npl=d-k
    quere="""insert into %s
            values ('%s','%s','%s','%s','%s')"""%(a,r,es,oe,tot,npl)
    cursor.execute(quere)
    mycon.commit()
    print(" ")
    print(a,r,es,oe,tot,npl)
    main()
main()
