import pyttsx3
from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(background='#8dafd6')
window.geometry('500x600')
window.title('The English text reader')

# ایجاد یک شی speaker به صورت سراسری
speaker = pyttsx3.init()

def read():
    e1_text = e1.get()
    e2_text = e2.get()

    # بررسی وجود متن و سرعت خواندن
    if not e1_text or not e2_text:
        messagebox.showerror("Error", "Please enter text and reading speed.")
        return

    try:
        speed = int(e2_text)
        if speed < 100 or speed > 300:  # محدوده مجاز سرعت
            messagebox.showerror("Error", "Please enter a reading speed between 100 and 300.")
            return
        speaker.setProperty('rate', speed)  # تنظیم سرعت قبل از خواندن
    except ValueError:
        messagebox.showerror("Error", "Please enter the reading speed as a number.")
        return

    speaker.say(e1_text)
    speaker.runAndWait()


l1 = Label(
    master=window,
    text='The English text reader',
    foreground='#FFFF00',
    background='#0a0aff',
    font='calibri 28 bold'
)
l1.pack(pady=5)

l2 = Label(
    master=window,
    text='Please enter your word or sentence here',
    font='calibri 20 bold',
    foreground='black',
    background='#32CD32'
)
l2.pack()

e1 = Entry(
    master=window,
    font='calibri 30 bold',
    background='#00FA9A',
    foreground='#1128c1',
    relief='ridge',
    bd=8,
) 
e1.pack(pady=15)

l3 = Label(
    master=window,
    text='Please enter your reading speed (100-300)',
    font='calibri 20 bold',
    foreground='black',
    background='#32CD32'
)
l3.pack(pady=20)

e2 = Entry(
    master=window,
    font='calibri 30 italic bold',
    background='#00FA9A',
    foreground='black',
    relief='groove',
    bd=8
)
e2.pack()


b1 = Button(
    master=window,
    text='Read',
    font='calibri 50 bold',
    foreground='blue',
    background='gray',
    activebackground='lightgreen',
    activeforeground='black',
    width=5,
    height=10,
    command=read
)
b1.pack(pady=50)


window.mainloop()
