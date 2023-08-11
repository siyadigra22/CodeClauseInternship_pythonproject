import tkinter as tk
from password_generator import PasswordGenerator

class PasswordGeneratorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.pwo = PasswordGenerator()

        self.label = tk.Label(root, text="Generated Password:")
        self.label.pack()

        self.password_label = tk.Label(root, text="")
        self.password_label.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        generated_password = self.pwo.generate()
        self.password_label.config(text=generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()