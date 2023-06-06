import serial
import time
import tkinter
from tkinter import ttk
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

ser = serial.Serial('/dev/ttyS0', 9600)


# time.sleep(3)

def button_on():
    ser.write(bytes('2', 'UTF-8'))


def button_off():
    ser.write(bytes('1', 'UTF-8'))


def aboutprogram():
    about_win = tkinter.Toplevel(win)
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    about_win.resizable(0, 0)
    sx = (ws / 2) - (400 / 2)
    sy = (hs / 2) - (300 / 2)
    about_win.geometry('%dx%d+%d+%d' % (400, 300, sx, sy))
    about_win.resizable(0, 0)
    about_win.title("IoT")

    comp = tkinter.Label(about_win, text="Ultrasonic Security System")
    comp.pack(pady=25, side=tkinter.RIGHT)
    comp.configure(font=("Courier", 12))
    comp.place(x=3, y=4)


def quit_window(icon, item):
    icon.stop()
    win.destroy()


def show_window(icon, item):
    icon.stop()
    win.after(0, win.deiconify())


def hide_window():
    win.withdraw()
    image = Image.open("favicon.ico")
    menu = (item('Open', show_window), item('Exit', quit_window))
    icon = pystray.Icon("name", image, "Light", menu)
    icon.run()


win = tkinter.Tk()
# win.geometry("800x600")
win.title("Led")  # Manu ledlight
# win.iconbitmap(default=resource_path("icon.ico"))
win.resizable(0, 0)
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
sx = (ws / 2) - (166 / 2)
sy = (hs / 2) - (166 / 2)
win.geometry('%dx%d+%d+%d' % (166, 166, sx, sy))
win.protocol('WM_DELETE_WINDOW', hide_window)

button_on = tkinter.Button(win,
                           text="Switch ON",
                           command=button_on,
                           height=1,
                           fg="black",
                           width=6,
                           bd=1,
                           )
button_on.pack(side='top', ipadx=5, padx=5, pady=5)
button_on.place(x=2, y=2)

button_off = tkinter.Button(win,
                            text="Switch OFF",
                            command=button_off,
                            height=1,
                            fg="black",
                            width=6,
                            bd=1,
                            )
button_off.pack(side='top', ipadx=5, padx=5, pady=5)
button_off.place(x=90, y=2)

separator = ttk.Separator(win, orient='horizontal')
separator.place(relx=0, rely=0.22, relwidth=1, relheight=1)

aboutprogram = tkinter.Button(win,
                              text="About",
                              command=aboutprogram,
                              height=1,
                              fg="black",
                              width=15,
                              bd=1,
                              )
aboutprogram.pack(side='top', ipadx=5, padx=5, pady=5)
aboutprogram.place(x=15, y=127)

# win.state("zoomed")
win.mainloop()
