from pathlib import Path
from dbcomm import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Toplevel


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/ryan/maven/Hackathon/main/assets")

def login(master):
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def retrieve(*Ar0, Ux0):
        Re0 = []
        for i in Ar0:
            Re0.append(i.get())
            i.set("")
        Ux0(Re0)

    def warning(image, warning_text):
        canvas.create_image(
            141.0,
            152.0,
            image=image
            )
        canvas.create_text(
            canvas.winfo_width() / 2,
            150.0,
            text=warning_text,
            fill="#4a628a",
            font=("SFPro Regular", 11 * -1)
            )
        
    def check_credentials(Re0):
        x = []
        for i in conn_exec("SELECT username FROM users"):
            x.append(i[0])
        if Re0[0] not in x:
            warning(image_image_2, "Username does not exist")
        else:
            y = []
            for i in conn_exec("SELECT password FROM users WHERE username = '{}'".format(Re0[0])):
                y.append(str(i[0]))
            print(y)
            if Re0[1] in y:
                warning(image_image_2, "Login successful")
            else:
                print(Re0[1])
                warning(image_image_2, "Incorrect password")
    login = Toplevel(master)
    login.geometry("280x312")
    login.configure(bg = "#C0CAD1")

    image_image_2 = PhotoImage(
        file=relative_to_assets("login/image_2.png"))
    canvas = Canvas(
        login,
        bg = "#C0CAD1",
        height = 312,
        width = 280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("login/button_1.png"))
    button_1 = Button(
        login,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: retrieve(username, password, Ux0 = check_credentials),
        relief="flat"
    )
    button_1.place(
        x=20.0,
        y=270.0,
        width=242.0,
        height=32.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("login/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        140.0,
        245.0,
        image=entry_image_1
    )
    password = StringVar()
    entry_1 = Entry(
        login,
        textvariable=password,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=30.0,
        y=230.0,
        width=220.0,
        height=28.0
    )

    canvas.create_text(
        20.0,
        216.0,
        anchor="nw",
        text="Password",
        fill="#4A628A",
        font=("SFPro Regular", 10 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("login/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        140.0,
        195.0,
        image=entry_image_2
    )
    username = StringVar()
    entry_2 = Entry(
        login,
        textvariable=username,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=30.0,
        y=180.0,
        width=220.0,
        height=28.0
    )

    canvas.create_text(
        20.0,
        166.0,
        anchor="nw",
        text="Username",
        fill="#4A628A",
        font=("SFPro Regular", 10 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("login/button_2.png"))
    button_2 = Button(
        login,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=10.0,
        y=110.0,
        width=66.0,
        height=22.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("login/image_1.png"))
    image_1 = canvas.create_image(
        140.0,
        55.0,
        image=image_image_1
    )
    canvas.place(x = 0, y = 0)

    login.resizable(False, False)
    login.mainloop()
