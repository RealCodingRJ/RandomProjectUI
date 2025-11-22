from tkinter import *
from URLImage import getURL
import Birthday

URL = "https://www.github.com/RealCodingRJ"
TITLE = "Github Profile Application"

root = Tk()

while True:

    try:

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
        root.mainloop()
        
        isRunning = True
        break

    except:
        print("Cannot Run Application")
        break
