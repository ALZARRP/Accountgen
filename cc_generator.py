import random
import datetime
import tkinter as tk
from tkinter import ttk

def is_valid(number):
    n_digits = len(number)
    n_sum = 0
    is_second = False
    for i in range(n_digits - 1, -1, -1):
        d = int(number[i])
        if is_second:
            d = d * 2
        n_sum += d // 10
        n_sum += d % 10
        is_second = not is_second
    return (n_sum % 10 == 0)

def generate_card_number(bin_number):
    card_number = bin_number
    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))

    sum_ = 0
    is_second = False
    for i in range(len(card_number) - 1, -1, -1):
        d = int(card_number[i])
        if is_second:
            d *= 2
        sum_ += d // 10
        sum_ += d % 10
        is_second = not is_second

    last_digit = (sum_ * 9) % 10
    card_number += str(last_digit)
    return card_number

def generate_expiration_date():
    month = random.randint(1, 12)
    year = datetime.datetime.now().year + random.randint(2, 5)
    return f"{month:02d}/{year}"

def generate_cvv():
    return str(random.randint(100, 999))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Credit Card Generator")
        self.geometry("400x500")
        self.configure(bg="#2E2E2E")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#2E2E2E", foreground="white", padding=5)
        style.configure("TEntry", padding=5)
        style.configure("TCheckbutton", background="#2E2E2E", foreground="white", padding=5)
        style.map("TCheckbutton", background=[("active", "#4A4A4A")])
        style.configure("TButton", background="#4A4A4A", foreground="white", padding=5)
        style.map("TButton", background=[("active", "#6E6E6E")])


        self.bin_label = ttk.Label(self, text="BIN:")
        self.bin_label.pack(pady=(10,0))
        self.bin_entry = ttk.Entry(self)
        self.bin_entry.pack(pady=5)

        self.count_label = ttk.Label(self, text="Count:")
        self.count_label.pack(pady=(10,0))
        self.count_entry = ttk.Entry(self)
        self.count_entry.pack(pady=5)
        self.count_entry.insert(0, "10")

        self.exp_var = tk.BooleanVar()
        self.exp_check = ttk.Checkbutton(self, text="Include Expiration Date", variable=self.exp_var)
        self.exp_check.pack(pady=5)

        self.cvv_var = tk.BooleanVar()
        self.cvv_check = ttk.Checkbutton(self, text="Include CVV", variable=self.cvv_var)
        self.cvv_check.pack(pady=5)

        self.generate_button = ttk.Button(self, text="Generate", command=self.generate)
        self.generate_button.pack(pady=10)

        self.output_text = tk.Text(self, bg="#4A4A4A", fg="white", insertbackground="white")
        self.output_text.pack(pady=5, padx=10, fill="both", expand=True)

    def generate(self):
        self.output_text.delete("1.0", tk.END)
        bin_number = self.bin_entry.get()
        if not bin_number:
            bins = ["4", "5", "37"]
            bin_number = random.choice(bins)

        count = int(self.count_entry.get())

        for _ in range(count):
            card_number = generate_card_number(bin_number)
            self.output_text.insert(tk.END, f"Card Number: {card_number}")
            if self.exp_var.get():
                self.output_text.insert(tk.END, f" | Expiration Date: {generate_expiration_date()}")
            if self.cvv_var.get():
                self.output_text.insert(tk.END, f" | CVV: {generate_cvv()}")
            self.output_text.insert(tk.END, "\n")

if __name__ == '__main__':
    app = App()
    app.mainloop()
