print("Welcome to MazeBank")
Trails=3
Userpin=1234

while Trails != 0:
    pin =int(input("Please Enter Your 4 digit Pin Number :")) 
    if pin !=Userpin:
        Trails -= 1
        print("Wrong Passward Try Again")
    else:
        UserChoice=input("D: Deposit or W : Withdraw")
        if UserChoice == "D":
            UserDeposit=input("Enter thee amount you whould like to Deposite:")
            print(UserDeposit,"$ Have Been Deposited Into Your Account")
        if UserChoice == "W":
            UserWithdraw= input("Enter The Amount You Would Like To Deposit")
            print(UserWithdraw,"$ Have Been Withdrawen From you Account")
    UserExit=input("Would You Like to Continue ? Y/N:")
    if UserExit=="N":
        print("Thank you For using MaxeBank")
        break
    else:
        continue


     