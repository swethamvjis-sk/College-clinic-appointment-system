#COLLEGE CLINIC APPOINTMENT SYSTEM

def Fees():
    print("1.General Doctor-->Rs 100")
    print("2.Specialist Doctor-->Rs 200")

def Appointment():
    Number=int(input("Enter the number of students visiting doctor:"))
    Token=1
    Fees=0
    for i in range(Number):
        
        if Token<=10:
            
            Name=input("Enter your name:")
            Department=input("Enter the department you belong to:")
            Doctor=input("Enter which type of doctor you want to visit:")
            if Doctor.lower()=="general":
                print(f"{Token}-->{Name}-->{Department}-->{Doctor}-->Rs 100")
                Fees+=100
                
            elif Doctor.lower()=="specialist":
                print(f"{Token}-->{Name}-->{Department}-->{Doctor}-->Rs 200")
                Fees+=200
                
            else:
                print("INCORRECT CHOICE")
                continue
            Token+=1
            print("Total students:",Token-1)
            print("Total fees:",Fees)
            
        else:
            print("The clinic is crowded!")
            
ch="yes"
while ch.lower() in ["yes","y"]:
    print("---COLLEGE CLINIC APPOINTMENT---")
    print("1.Fees")
    print("2.Appointment")
    print("3.Exit")
    choice=int(input("Enter the choice number:"))
    if choice==1:
        Fees()
    elif choice==2:
        Appointment()
    elif choice==3:
        print("Thanks for visiting college clinic!")
        break
    else:
        print("INVALID CHOICE")
    ch=input("Do you want to continue(yes/no)?")
