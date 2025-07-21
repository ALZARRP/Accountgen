import customtkinter as ctk
from json import load
from generator import Generator
import asyncio
from threading import Thread

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Multi-Account Generator")
        self.geometry("600x450")

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Multi-Account Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.service_frame = ctk.CTkFrame(self)
        self.service_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.service_label = ctk.CTkLabel(self.service_frame, text="Service:")
        self.service_label.grid(row=0, column=0, padx=10, pady=10)

        self.config = load(open('config.json'))
        self.service_dropdown = ctk.CTkComboBox(self.service_frame, values=self.config["services"])
        self.service_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.amount_frame = ctk.CTkFrame(self)
        self.amount_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.amount_label = ctk.CTkLabel(self.amount_frame, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = ctk.CTkEntry(self.amount_frame)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.generate_button = ctk.CTkButton(self, text="Generate Accounts", command=self.start_generator)
        self.generate_button.grid(row=2, column=0, padx=20, pady=10)

        self.output_textbox = ctk.CTkTextbox(self, width=560, height=200)
        self.output_textbox.grid(row=3, column=0, padx=20, pady=10)

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.progress_bar.set(0)

        self.generator = Generator(self)

    def start_generator(self):
        service = self.service_dropdown.get()
        amount = int(self.amount_entry.get())
        self.output_textbox.delete("1.0", "end")
        self.progress_bar.start()

        def run_async_loop():
            asyncio.run(self.generator.run(service, amount))
            self.stop_generator()

        thread = Thread(target=run_async_loop)
        thread.start()

    def update_output(self, text):
        self.output_textbox.insert("end", text)
        self.output_textbox.see("end")

    def stop_generator(self):
        self.progress_bar.stop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
