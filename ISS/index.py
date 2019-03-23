
from databaseFile import *
from homeTracking import *



print("index.py")
print("Name: Pavithra")
print("ID: admin")
print("Pass: admin")


trackLoc=""
root = Tk()
root.title("ISS Tracking Login Portal")
width = 400
height = 280
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
xCoordinate = (s_width/2) - (width/2)
yCoordinate = (s_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, xCoordinate, yCoordinate))
root.resizable(0, 0)


loadBgImage= Image.open('images/bg_login.jpg')
render=ImageTk.PhotoImage(loadBgImage)
bg_image =Label(root,image=render)
bg_image.image = render
bg_image.place(x=0,y=0)


def LoginCheck(event=None):
    try:
        
        createDatabase()

        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_txt.config(text="Username or Password not Entered!", fg="red")
        else:
            value = getLoginDetails(USERNAME.get(), PASSWORD.get())
            if value == True:
                HomeWindow(root)
                USERNAME.set("")
                PASSWORD.set("")
                lbl_txt.config(text="")
            else:
                lbl_txt.config(text="Invalid Username or Password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
    except Exception as e:
        print("Exception :",e)
        exit(1)



USERNAME = StringVar()
PASSWORD = StringVar()


loginFrame = Frame(root, height=190)
loginFrame.pack(side=TOP, pady=40)


lbl_un = Label(loginFrame, text = "Username:", font=('arial', 12), bd=12)
lbl_un.grid(row=0, sticky="e")
lbl_pwd = Label(loginFrame, text = "Password:", font=('arial', 12), bd=12)
lbl_pwd.grid(row=1, sticky="e")
lbl_txt = Label(loginFrame)
lbl_txt.grid(row=2, columnspan=2)


username = Entry(loginFrame, textvariable=USERNAME, font=(12), width=20)
username.grid(row=0, column=1)
password = Entry(loginFrame, textvariable=PASSWORD, show="*", font=(12), width=20)
password.grid(row=1, column=1)


btn_login = Button(loginFrame, text="Login", width=20, command=LoginCheck)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', LoginCheck)

if __name__ == '__main__':
    root.mainloop()