import tkinter as tk


class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)
            return ComplexNumber(real_part, imag_part)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            divisor = other.real ** 2 + other.imag ** 2
            real_part = (self.real * other.real + self.imag * other.imag) / divisor
            imag_part = (self.imag * other.real - self.real * other.imag) / divisor
            return ComplexNumber(real_part, imag_part)
        else:
            raise TypeError("Unsupported operand type for /")


# Create a Tkinter application
class ComplexOperationsCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Complex Number Operations Calculator")

        self.create_input_widgets()
        self.create_output_widget()

    def create_input_widgets(self):
        self.real_label = tk.Label(self.root, text="Real Part:")
        self.real_label.pack()

        self.real_entry = tk.Entry(self.root)
        self.real_entry.pack()

        self.imag_label = tk.Label(self.root, text="Imaginary Part:")
        self.imag_label.pack()

        self.imag_entry = tk.Entry(self.root)
        self.imag_entry.pack()

        self.operation_label = tk.Label(self.root, text="Operation:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")

        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def create_output_widget(self):
        self.output_label = tk.Label(self.root, text="Result:")
        self.output_label.pack()

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_var)
        self.result_label.pack()

    def calculate(self):
        try:
            real = float(self.real_entry.get())
            imag = float(self.imag_entry.get())

            num1 = ComplexNumber(real, imag)

            if self.operation_var.get() == "+":
                result = num1 + num2
            elif self.operation_var.get() == "-":
                result = num1 - num2
            elif self.operation_var.get() == "*":
                result = num1 * num2
            elif self.operation_var.get() == "/":
                result = num1 / num2

            self.result_var.set(str(result))
        except ValueError:
            self.result_var.set("Invalid input")
        except ZeroDivisionError:
            self.result_var.set("Division by zero")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = ComplexOperationsCalculator(root)
    num2 = ComplexNumber()  # Initialize a default complex number
    root.mainloop()
