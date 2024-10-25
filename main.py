import customtkinter as ctk
import pyautogui
from time import sleep
from tkinter import messagebox

ctk.set_appearance_mode("system")  # default


def button_click():
    try:
        avs = "Esse Protótipo é experimental! \n"
        avs += "Ainda está sendo Desenvolvido!"
        messagebox.showwarning("Atenção", avs)

        pyautogui.PAUSE = 0.5
        print(pyautogui.position())
        print(pyautogui.size())

        sleep(5)
        pyautogui.moveTo(x=1762, y=18, duration=1)

        sleep(1)
        pyautogui.click(x=1762, y=18)

        sleep(1)
        pyautogui.moveTo(x=48, y=404, duration=1)

        sleep(1)
        pyautogui.click(x=48, y=404, clicks=2, interval=0.3, button='left')

        sleep(1)
        pyautogui.moveTo(x=1762, y=18, duration=1)

        sleep(1)
        pyautogui.click(x=1762, y=18)

        msg = "Esse Protótipo é experimental! \n"
        msg += "Ainda está sendo Desenvolvido!"
        messagebox.showinfo("Atenção", msg)
    except:
        pass


class Robo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('ico.ico')
        self.geometry("300x150")
        self.title("BR Robotcs")
        self.resizable(False, False)

        # Botão
        self.button = ctk.CTkButton(self, text="Iniciar", width=100, command=button_click)
        self.button.place(relx=0.50, rely=0.70)

        # Label
        self.label = ctk.CTkLabel(self, text="Protótipo de App para automação",
                                  font=("Century Gothic bold", 14))
        self.label.pack()


app = Robo()
app.mainloop()
