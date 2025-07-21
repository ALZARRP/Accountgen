import customtkinter as ctk
from password_generator import PasswordGenerator
from updater import AutoUpdater

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.version = "1.0.0"
        #AutoUpdater(self.version).update()

        self.title("Secure Password Generator")
        self.geometry("400x450")

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Secure Password Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.password_length_frame = ctk.CTkFrame(self)
        self.password_length_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.password_length_label = ctk.CTkLabel(self.password_length_frame, text="Password Length:")
        self.password_length_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_length_slider = ctk.CTkSlider(self.password_length_frame, from_=8, to=32, number_of_steps=24)
        self.password_length_slider.set(12)
        self.password_length_slider.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.password_length_value_label = ctk.CTkLabel(self.password_length_frame, text="12")
        self.password_length_value_label.grid(row=0, column=2, padx=10, pady=10)
        self.password_length_slider.configure(command=lambda value: self.password_length_value_label.configure(text=str(int(value))))

        self.checkbox_frame = ctk.CTkFrame(self)
        self.checkbox_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.uppercase_var = ctk.BooleanVar(value=True)
        self.uppercase_checkbox = ctk.CTkCheckBox(self.checkbox_frame, text="Uppercase", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=0, column=0, padx=10, pady=10)

        self.lowercase_var = ctk.BooleanVar(value=True)
        self.lowercase_checkbox = ctk.CTkCheckBox(self.checkbox_frame, text="Lowercase", variable=self.lowercase_var)
        self.lowercase_checkbox.grid(row=0, column=1, padx=10, pady=10)

        self.numbers_var = ctk.BooleanVar(value=True)
        self.numbers_checkbox = ctk.CTkCheckBox(self.checkbox_frame, text="Numbers", variable=self.numbers_var)
        self.numbers_checkbox.grid(row=1, column=0, padx=10, pady=10)

        self.symbols_var = ctk.BooleanVar(value=True)
        self.symbols_checkbox = ctk.CTkCheckBox(self.checkbox_frame, text="Symbols", variable=self.symbols_var)
        self.symbols_checkbox.grid(row=1, column=1, padx=10, pady=10)

        self.generate_button = ctk.CTkButton(self, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, padx=20, pady=10)

        self.password_entry = ctk.CTkEntry(self, width=300)
        self.password_entry.grid(row=4, column=0, padx=20, pady=10)

        self.copy_button = ctk.CTkButton(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=0, padx=20, pady=10)

    def generate_password(self):
        length = int(self.password_length_slider.get())
        use_uppercase = self.uppercase_var.get()
        use_lowercase = self.lowercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        try:
            generator = PasswordGenerator(
                length=length,
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase,
                use_numbers=use_numbers,
                use_symbols=use_symbols
            )
            password = generator.generate()
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, password)
        except ValueError as e:
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, str(e))

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
