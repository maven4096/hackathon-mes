from pathlib import Path
from dbcomm import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/ryan/maven/Hackathon/main/assets")

def signup(master):
    
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
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
    def retrieve(*Ar0, Ux0, image):
        Re0 = []
        for i in Ar0:
            if i.get() == "":
                break
            else:
                Re0.append(i.get())
                i.set("")
        Ux0(Re0, image)
    def confirm_pass(Re0, image):    
        if Re0[1] == Re0[2]:
            warning(image, "Account created successfully")
            x = []
            for i in conn_exec("SELECT username FROM users"):
                x.append(i[0])
            if Re0[0] in x:
                warning(image, "Username already exists")
            else:
                conn_exec("INSERT INTO users VALUES('{}', '{}')".format(Re0[0], str(Re0[1])))           
                signup.destroy()
        else:
            warning(image, "Passwords do not match")
    signup = Toplevel(master)
    signup.geometry("280x362")
    signup.configure(bg = "#7ab2d3")
    image_image_1 = PhotoImage(file=relative_to_assets("signup/image_1.png"))
    canvas = Canvas(
        signup,
        bg = "#C0CAD1",
        height = 362,
        width = 280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("signup/button_1.png"))
    button_1 = Button(
        signup,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: retrieve(username, password, conf_pass, Ux0=confirm_pass, image=image_image_1),
        relief="flat"
    )
    button_1.place(
        x=20.0,
        y=320.0,
        width=242.0,
        height=32.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("signup/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        140.0,
        295.0,
        image=entry_image_1
    )
    conf_pass = StringVar()
    entry_1 = Entry(
        signup,
        textvariable=conf_pass,
        bd=0,
        bg="#D9D9D9",
        fg="#4a628a",
        highlightthickness=0
    )
    entry_1.place(
        x=30.0,
        y=280.0,
        width=220.0,
        height=28.0
    )

    canvas.create_text(
        20.0,
        266.0,
        anchor="nw",
        text="Confirm Password",
        fill="#4a628a",
        font=("SFPro Regular", 10 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("signup/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        140.0,
        245.0,
        image=entry_image_2
    )
    password = StringVar()
    entry_2 = Entry(
        signup,
        textvariable=password,
        bd=0,
        bg="#D9D9D9",
        fg="#4a628a",
        highlightthickness=0
    )
    entry_2.place(
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
        fill="#4a628a",
        font=("SFPro Regular", 10 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("signup/entry_3.png"))
    entry_bg_3 = canvas.create_image(
        140.0,
        195.0,
        image=entry_image_3
    )
    username = StringVar()
    entry_3 = Entry(
        signup,
        textvariable=username,
        bd=0,
        bg="#D9D9D9",
        fg="#4a628a",
        highlightthickness=0
    )
    entry_3.place(
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
        fill="#4a628a",
        font=("SFPro Regular", 10 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("signup/image_1.png"))



    button_image_2 = PhotoImage(
        file=relative_to_assets("signup/button_2.png"))
    button_2 = Button(
        signup,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: signup.destroy(),
        relief="flat"
    )
    button_2.place(
        x=10.0,
        y=110.00000000000001,
        width=66.0,
        height=22.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("signup/image_2.png"))
    image_2 = canvas.create_image(
        140.0,
        55.000000000000014,
        image=image_image_2
    )

    canvas.create_text(
        69.0,
        30.0,
        anchor="nw",
        text="Signup",
        fill="#4a628a",
        font=("SFPro Regular", 48 * -1)
    )
    signup.resizable(False, False)
    signup.mainloop()
