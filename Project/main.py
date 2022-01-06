from tkinter import *
from tkinter import messagebox


class Calculator(object):

    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x200")
        self.window.title("Kalkulator")
        self.window_setup()
        self.expression = ""
        mainloop()

    def window_setup(self):
        # self.entry_box = Entry(width=53, justify="right", state="disabled")  # zastanowić się czy disbled ma być
        # self.entry_box.grid(row=0, column=0, columnspan=4, sticky=W)

        self.entry_box = Text(width=55, height=2)
        self.entry_box.grid(row=0, column=0, columnspan=4, sticky=W)

        # self.equation_box = Entry(width=53, justify="right")
        # self.equation_box.grid(row=1, column=0, columnspan=4, sticky=W)

        self.button_1 = self.make_button("1", 1, 0, lambda x="1": self.character_button_click(x))
        self.button_2 = self.make_button("2", 1, 1, lambda x="2": self.character_button_click(x))
        self.button_3 = self.make_button("3", 1, 2, lambda x="3": self.character_button_click(x))
        self.button_plus = self.make_button("+", 1, 3, lambda x="+": self.character_button_click(x))

        self.button_4 = self.make_button("4", 2, 0, lambda x="4": self.character_button_click(x))
        self.button_5 = self.make_button("5", 2, 1, lambda x="5": self.character_button_click(x))
        self.button_6 = self.make_button("6", 2, 2, lambda x="6": self.character_button_click(x))
        self.button_minus = self.make_button("-", 2, 3, lambda x="-": self.character_button_click(x))

        self.button_7 = self.make_button("7", 3, 0, lambda x="7": self.character_button_click(x))
        self.button_8 = self.make_button("8", 3, 1, lambda x="8": self.character_button_click(x))
        self.button_9 = self.make_button("9", 3, 2, lambda x="9": self.character_button_click(x))
        self.button_multiplication = self.make_button("*", 3, 3, lambda x="*": self.character_button_click(x))

        self.button_comma = self.make_button(".", 4, 0, lambda x=".": self.character_button_click(x))
        self.button_zero = self.make_button("0", 4, 1, lambda x="0": self.character_button_click(x))
        self.button_equation = self.make_button("=", 4, 2, lambda x="=": self.equation_button_click(x))
        self.button_division = self.make_button("/", 4, 3, lambda x="/": self.character_button_click(x))


    @staticmethod
    def make_button(button_text, button_row, button_column, button_action):
        button = Button(width=20, height=2, bg="white", fg="black", text=button_text)
        button.grid(row=button_row, column=button_column, sticky=W)
        button["command"] = button_action
        return button_action

    def character_button_click(self, text):
        self.expression += text
        self.entry_box["state"] = "normal"  # zastanowić się nad tym
        self.entry_box.delete(0.0, "end")
        self.entry_box.insert("end", self.expression)
        self.entry_box["state"] = "disabled"

    def equation_button_click(self):
        pass

def main():
    Calc = Calculator()
    pass


main()
