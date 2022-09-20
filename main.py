from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password == "secret":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="red")

        message = text1.get(1.0,END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message + b'=')
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="ubuntu", fg="white", bg="grey").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END,decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Entrez le mot de passe")

    elif password != "secret":
        messagebox.showerror("encryption", "Mot de passe invalide")

def encrypt():
    password=code.get()
    if password == "secret":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="SteelBlue")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="ubuntu",fg="white",bg="grey").place(x=10,y=0)
        text2=Text(screen1,font="Roboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password == "":
        messagebox.showerror("encryption","Entrez le mot de passe")

    elif password != "secret":
        messagebox.showerror("encryption","Mot de passe invalide")

def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("500x420")
    image_icon = PhotoImage(file="logo.png")
    screen.iconphoto(False,image_icon)

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Entrez votre texte à encrypter et décrypter",fg="black",font=('ubuntu',14)).place(x=10,y=10)
    text1=Text(font="roboto 18",bg="gray82",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=480,height=100)

    Label(text="Entrez la clé secrète pour encrypter et décrypter",fg="black",font=("ubuntu",14)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=37,bd=0,bg="gray82",font=("roboto",18),show="*").place(x=10,y=200,height=50)
    screen.title("EncryptApp")

    Button(text="ENCRYPT",height="2",width=23,bg="SteelBlue",fg="white",bd=0,command=encrypt).place(x=10,y=280)
    Button(text="DECRYPT",height="2",width=23,bg="red",fg="white",bd=0,command=decrypt).place(x=325,y=280)
    Button(text="RESET",height=2,width=68,bg="SlateGray",fg="white",bd=0,command=reset).place(x=10,y=350)
    screen.mainloop()
main_screen()