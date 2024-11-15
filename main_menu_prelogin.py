from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/ryan/maven/Hackathon/main/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1031x581")
window.configure(bg = "#7AB2D3")


canvas = Canvas(
    window,
    bg = "#7AB2D3",
    height = 581,
    width = 1031,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=18.75,
    y=506.25,
    width=281.25,
    height=56.25
)

button_image_2 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=18.75,
    y=431.25,
    width=281.25,
    height=56.25
)

button_image_3 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=18.75,
    y=356.25,
    width=281.25,
    height=56.25
)

button_image_4 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=18.75,
    y=281.25,
    width=281.25,
    height=56.25
)

button_image_5 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=18.75,
    y=206.25,
    width=281.25,
    height=56.25
)

image_image_1 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/image_1.png"))
image_1 = canvas.create_image(
    514.75,
    102.75,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/image_2.png"))
image_2 = canvas.create_image(
    664.75,
    384.25,
    image=image_image_2
)

button_image_6 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=843.75,
    y=318.75,
    width=121.875,
    height=121.875
)

button_image_7 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=684.375,
    y=318.75,
    width=121.875,
    height=121.875
)

button_image_8 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=525.0,
    y=318.75,
    width=121.875,
    height=121.875
)

button_image_9 = PhotoImage(
    file=relative_to_assets("main_menu_prelogin/button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=365.625,
    y=318.75,
    width=121.875,
    height=121.875
)
window.resizable(False, False)
window.mainloop()
