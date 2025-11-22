from tkinter import *
from URL import getURL, urlConfig
import Birthday


root = Tk()

while True:
    try:

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
        print("ell")
        root.mainloop()
        
        isRunning = True
        break

    except:
        print("Cannot Run Application")
