import os
import sys
import time
def login_Main():
    import time
    import holder
    import sys
    from momo import MoMo_Main

    def mmt2_Main():
        print("\n=======================")
        print("MobileMoney Transaction Program")
        global ask
        ask = int(input("\nHow much is in your acount? "))
        MoMo_Main()



    def login(user="user",passw=0000):
        while True:
            try:
                users=holder.users_list.keys()
                passc=holder.users_list.values()
                os.system("cls")
                print("=======================")
                print("Login".upper())
                userinput=str(input("Enter your username: "))
                passinput=int(input("Enter your pin: "))

                if(userinput in users or userinput==user):
                    if(passinput in passc or passinput==passw):
                        mmt2_Main()
                    else:
                        print("\nInvalid Password.")
                        continue
                else:
                    print("\nUsername not found.")
                    continue
            except Exception:
                os.system("cls")
                print("\n\nTransaction Failed.")
            sys.exit()


    def register(newuser="user",newpin=0000):
        try:
            try:
                print("\n==============")
                print("Register")
                print("Enter your Username")
                newuser=str(input("")).lower()
                print("Enter your new pin")
                newpin=int(input(""))
            except Exception:
                print("Input required.\nplease try again.")
                sys.exit()
                
            if(newuser=="user" and newpin==0000):
                print("\n==============")
                print("Your username and pin are insecured.")
                cont=str(input("Do you want to continue?(Y/N) ")).lower()
                if(cont=="y"):
                    holder.users_list[newuser]=newpin
                    print("registered successfully.")
                    login()
                elif(cont=="n"):
                    register()
                else:
                    print("\nInput required.")
                    sys.exit()
            holder.users_list[newuser]=newpin
            print("registered successfully.")
            login()
        except Exception:
            print("Something went wrong.\nPlease try again.")
            sys.exit()

    class start:
        try:
            os.system("cls")
            print("\nWelcome To MoMo Program")
            print("1 : Login")
            print("2 : Register")
            select=int(input(">"))
            if(select==1):
                login()
            elif(select==2):
                register(newuser="user",newpin=0000)
            else:
                print("\nInvalid selection")
        except Exception:
            print("Input required. please try again.")
            sys.exit()
    start


def ussd(dcode="962"):
    try:
        os.system("cls")
        print("Enter Code")
        code=str(input(">"))
        if(code=="962"):
            os.system("cls")
            print("USSD code running...")
            time.sleep(5)
            login_Main()
        else:
            print("Invalid Code.")
            time.sleep(1)
            os.system("cls")
    except Exception:
        os.system("cls")
        print("\n\nUnknow application.")
        sys.exit()
ussd(dcode="962")
