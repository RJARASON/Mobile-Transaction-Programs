def MoMo_Main():
    class Momo():
        import time
        import sys
        import getpass
        from MAIN import ask
        import os
        try:
            for T in range(3):
                os.system("cls")
                print("\n=====================")
                for rerun in range(3):
                    print("\nSelect from the Menu")
                    print("1 : Deposit")
                    print("2 : Withdrawal")
                    print("3 : Check Balance")
                    print("4 : version")
                    print("5 : Exit")
                    select=int(input(">"))
                    if(select==1):
                        os.system("cls")
                        print("Deposit\n".upper())
                        much1 = int(input("How much do you want to Deposit? "))
                        print("please wait....")
                        time.sleep(2)
                        os.system("cls")
                        num = str(input("Enter your Mobile Number: "))
                        if(len(num)>=10 or num.__contains__(f"+ {num}")):
                            print("Loading.....")
                            time.sleep(1)
                            os.system("cls")
                            print("NOTE: Pin is hidden.")
                            pin=getpass.getpass("Enter your pin: ")
                            print("Loading.......")
                            time.sleep(2)
                            os.system("cls")
                            print("====================================")
                            print(f"Your Deposit of  {much1} was Successful.")
                            ask+=much1
                            print("Your Balance left is ",ask,"Ghc")
                            print("Thank you.")
                            print("====================================")
                            rerun
                        else:
                            os.system("cls")
                            print("\nInvalid Number.\nnumber is not up to 10 digits.\n")
                            sys.exit()
                    elif(select==2):
                        os.system("cls")
                        print("\nWithDrawn\n".upper())
                        much = int(input("How Much? "))
                        if much > ask:
                            print("Your Balance is too Low")
                        elif much < ask:
                            os.system("cls")
                            num1 = str(input("Enter your Mobile Number: "))
                            if(len(num1)>=10 or num.__contains__(f"+ {num1}")):
                                print("please wait...")
                                time.sleep(2)
                                os.system("cls")
                                prompt1 = str(input("Allow Cashout 'Yes' or 'No': ")).lower()
                                if (prompt1 == ("yes")):
                                    time.sleep(2)
                                    print("Cashout is Allowed!")
                                    print("NOTE: Pin is hidden.")
                                    time.sleep(2)
                                    os.system("cls")
                                    getpass.getpass("Enter yout pin: ")
                                    time.sleep(3)
                                    print("Loading....")
                                    time.sleep(1)
                                    os.system("cls")
                                    print("-------------------------------")
                                    print("Cashout for", much, "Sucessful.")
                                    ask-=much
                                    print(f"Your Balance left is {ask}Ghc")
                                    print("Thank you.")
                                    print("-------------------------------")
                                    continue
                                elif (prompt1 == ("no")):
                                    os.system("cls")
                                    print("\nCashout denied.")
                            else:
                                os.system("cls")
                                print("\nInvalid Number.\nnumber is not up to 10 digits.")
                                sys.exit()
                    elif(select==3):
                        os.system("cls")
                        print("\nCheck Balance\n")
                        time.sleep(1)
                        pin1=int(input("Enter your Pin "))
                        os.system("cls")
                        print("=============")
                        print(f"Your current Balance is {ask}Ghc.")
                        print("=============")
                        rerun
                    elif(select==4):
                        time.sleep(2)
                        os.system("cls")
                        print("======================")
                        print("Program name : MobileMoney Transaction Program")
                        print("Program version : ver 1.2")
                        print("======================")
                    elif(select==5):
                        os.system("cls")
                        print("\nProgram terminated.")
                        sys.exit()
                    else:
                        print("ERROR : Invalid.")
        except Exception:
            os.system("cls")
            print("\nSystem failed. try again.")
            sys.exit()
    Momo()
MoMo_Main()