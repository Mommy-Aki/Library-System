import tkinter # makes sure to import the GUI to start with
from random import randint # imports randomness
from colorama import Fore as Set
from time import sleep as eep

try: # makes sure the program can still run with no errors
    
    with open("README\CyrnfrQbagQryrgrZrjnnnnn.txt","r") as Verification: # makes sure info has not be deleted
        CollectedData = Verification.readlines()
        Error = False
        Multiplier = 45
        for line in CollectedData: # checks each line
            if Multiplier > 79: # breaks if the multiplier extends the range
                break
            NewKey =  926746727 * Multiplier # id
            if "Key" not in line or str(NewKey) not in line: # checks if the number is in the line
                Error = True # goes o shit there is an error
            Multiplier += 1
    
    if Error == True: # breaks the try statement if an error is shat out
        BreakConstant = "a"
        int(BreakConstant)
    
    PassWordWindow = tkinter.Tk()
    Icon = tkinter.PhotoImage(file="Icon.png")
    PassWordWindow.iconphoto(False,Icon)
    PassWordWindow.resizable(width=False,height=False)
    PassWordWindow.title("Required Password")
    TitleLabel = tkinter.Label(text="[Input Prompt]",width=36)
    NewPass = tkinter.Entry(name="bitch")
    Status = tkinter.Label(text="")
    TitleLabel.pack()
    NewPass.pack()  
    Status.pack()
    
    
    def AcceptPassword(event):
        NewInput = NewPass.get()
        with open("README\WhzzdvykVmUbaopu.txt","r") as Secret:
            CurrentLine = 1
            for line in Secret.readlines():
                if CurrentLine == 4:
                    NewPassWord = str(line).strip()
                CurrentLine += 1
            if event.keysym == "Return":
                if NewInput == NewPassWord:
                    print("Password Accepted")
                    
                    PassWordWindow.destroy()   
                else:
                    print("Invalid Password")
                    Status.configure(text="Error: Invalid Password",fg="#FF0000")
                    NewPass.delete(0,tkinter.END)


    
    PassWordWindow.bind("<Key>",AcceptPassword)
    PassWordWindow.mainloop()
    
    with open("README\WhzzdvykVmUbaopu.txt","r") as Secret:
        Authorized = False
        CurrentLine = 1
        for line in Secret.readlines():
            if CurrentLine == 4:
                VerifyPass = str(line).strip()
            CurrentLine += 1
        if VerifyPass == NewPassword:
            Authorized = True

    if Authorized == True:
        SelectionWindow = tkinter.Tk()
        SelectionWindow.title("Fuck off")
        SelectionWindow.iconphoto(False,Icon)
        NewPrompt = tkinter.Label(text="[Insert Prompt]",master=SelectionWindow)
        NewPrompt.pack()
        SelectionWindow.mainloop()


except:
    print("Error during Runtime")


