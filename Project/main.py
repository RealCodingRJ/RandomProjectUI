from tkinter import *
from URLImage import getURL
import Birthday
from datetime import datetime

URL = "https://www.github.com/RealCodingRJ"
TITLE = "Github Profile Application"

root = Tk()
    
try:

    dateNow = Birthday.NOW
    datBirtday = datetime.now().month
    datetimeBirthdayMonth = 11
    dayBirthdayMonth = abs(datetimeBirthdayMonth - datBirtday)
    dayBirthday = int(dateNow.day)

    dateBirth = abs(datBirtday - datetimeBirthdayMonth)
    dayBirth = abs(dateBirth - datBirtday)


    if dateNow == dateBirth:
        
        labelTitle = Label(root, text=f"{TITLE}")
        labelGithub = Label(root, text=f"{URL}")

        labelTitle.config(font=("sans-seif", 10, "bold"))
        labelTitle.pack()
        urlConfig = getURL("app.png")
        root.geometry(f"{int(800 / 2)}x{int(1200 / 2)}")
        root.resizable(False, False)
        root.title("App")
        photo = PhotoImage(file=urlConfig)

        label = Label(root, image=photo)
        label.pack()

        message = "Happy " + str(Birthday.year) + "th Birthday"
        label1 = Label(root, text=message)
        label1.config(font=("sans-serif", 15, "bold"))
        label1.pack()
        labelGithub.config(font=("sans-serif", 10))
        labelGithub.pack();
        print("ell")
    else:

        labelBirthday = Label(root, text=f"Your Birthday was : {int(dayBirth - dateBirth - 6)} Days Ago")

        labelGithub = Label(root, text=f"{URL}")
        urlConfig = getURL("app.png")
        root.geometry(f"{int(800 / 2)}x{int(1200 / 2)}")
        root.resizable(False, False)
        root.title("App")
        photo = PhotoImage(file=urlConfig)
        labelTitle = Label(root, text=f"{TITLE}")
        labelGithub = Label(root, text=f"{URL}")

        labelTitle.config(font=("sans-seif", 10, "bold"))
        labelTitle.pack()
        urlConfig = getURL("app.png")
        root.geometry(f"{int(800 / 2)}x{int(1200 / 2)}")
        root.resizable(False, False)
        root.title("App")
        photo = PhotoImage(file=urlConfig)
                
        label = Label(root, image=photo)
        label.pack()

        message = "Happy " + str(Birthday.year) + "th Birthday"
        label1 = Label(root, text=message)
        label1.config(font=("sans-serif", 15, "bold"))
        label1.pack()
        labelGithub.config(font=("sans-serif", 10))
        labelBirthday.pack()
        labelGithub.pack();


    # isRunning = True
    root.mainloop()


except:
    print("Cannot Run Application")
        

