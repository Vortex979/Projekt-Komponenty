from tkinter import *
from tkinter import messagebox


class TooLongExpressionException(Exception):
    pass


class Calculator(object):

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1360x560")
        self.window.title("Kalkulator")
        self.window_setup()
        self.expression = ""
        self.previous_expression = ""
        self.equation = ""
        mainloop()

    def window_setup(self):
        self.entry_box = Text(width=31, height=2, spacing1=10, font=("Helvetica", 60), state="disabled")
        self.entry_box.grid(row=0, column=0, columnspan=5, sticky=W)

        self.button_1 = self.make_button("1", 1, 0, lambda x="1": self.character_button_click(x))
        self.button_2 = self.make_button("2", 1, 1, lambda x="2": self.character_button_click(x))
        self.button_3 = self.make_button("3", 1, 2, lambda x="3": self.character_button_click(x))
        self.button_delete = self.make_button("del", 1, 3, self.delete_button_click)
        self.button_clear = self.make_button("clear", 1, 4, self.clear_button_click)

        self.button_4 = self.make_button("4", 2, 0, lambda x="4": self.character_button_click(x))
        self.button_5 = self.make_button("5", 2, 1, lambda x="5": self.character_button_click(x))
        self.button_6 = self.make_button("6", 2, 2, lambda x="6": self.character_button_click(x))
        self.button_plus = self.make_button("+", 2, 3, lambda x="+": self.character_button_click(x))
        self.button_minus = self.make_button("-", 2, 4, lambda x="-": self.character_button_click(x))

        self.button_7 = self.make_button("7", 3, 0, lambda x="7": self.character_button_click(x))
        self.button_8 = self.make_button("8", 3, 1, lambda x="8": self.character_button_click(x))
        self.button_9 = self.make_button("9", 3, 2, lambda x="9": self.character_button_click(x))
        self.button_multiplication = self.make_button("*", 3, 3, lambda x="*": self.character_button_click(x))
        self.button_division = self.make_button("/", 3, 4, lambda x="/": self.character_button_click(x))

        self.button_comma = self.make_button(".", 4, 0, lambda x=".": self.character_button_click(x))
        self.button_zero = self.make_button("0", 4, 1, lambda x="0": self.character_button_click(x))
        self.button_equation = self.make_button("=", 4, 2, self.equation_button_click)
        self.button_bracket_left = self.make_button("(", 4, 3, lambda x="(": self.character_button_click(x))
        self.button_bracket_right = self.make_button(")", 4, 4, lambda x=")": self.character_button_click(x))


    @staticmethod
    def make_button(button_text, button_row, button_column, button_action):
        button = Button(width=10, height=1, bg="white", fg="black", text=button_text, font=("Helvetica", 34))
        button.grid(row=button_row, column=button_column, sticky=W)
        button["command"] = button_action
        return button_action

    def character_button_click(self, text):
        try:
            if len(self.expression) == 25:
                raise TooLongExpressionException
            self.expression += text
            self.modify_entry_box(self.expression)
        except TooLongExpressionException:
            message_box = messagebox.showwarning("Błąd", "Twoje równanie jest za długie!")
        # except:
        #     message_box = messagebox.showerror("Błąd", "Twoje równanie jest za długie!")

    def equation_button_click(self):  # dodać zabezpiecznie przed pustymi stringami
        try:
            self.equation = eval(self.expression)
            if str(self.equation) == "()":
                raise SyntaxError

            self.previous_expression = self.expression
            self.modify_entry_box(self.previous_expression)

            self.entry_box["state"] = "normal"
            self.entry_box.insert("end", "\n" + str(self.equation))
            self.entry_box["state"] = "disabled"
        except SyntaxError:
            self.equation_error_message_box("Źle podane równanie, lub jego brak.")
        except ZeroDivisionError:
            self.equation_error_message_box("Dzielenie przez zero nie jest dozwolone.")
        # except:  # to na potem
        #     self.equation_error_message_box("Błąd.")
        finally:
            self.expression = ""

    def delete_button_click(self):
        self.expression = self.expression[:-1]
        self.modify_entry_box(self.expression)

    def clear_button_click(self):
        self.expression = ""
        self.modify_entry_box(self.expression)

    def modify_entry_box(self, text):
        self.entry_box["state"] = "normal"
        self.entry_box.delete(0.0, "end")
        self.entry_box.insert("end", text)
        self.entry_box["state"] = "disabled"

    def equation_error_message_box(self, message):
        self.entry_box["state"] = "normal"
        self.entry_box.delete(0.0, "end")
        self.entry_box["state"] = "disabled"
        message_box = messagebox.showerror("Błąd", message)


def main():
    Calc = Calculator()
    pass


main()
