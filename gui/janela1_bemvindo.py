import tkinter as tk
from PIL import Image, ImageTk

# === JANELA PRINCIPAL ===
janela1 = tk.Tk()
janela1.title("Primeira Janela")
janela1.geometry("500x400")
janela1.configure(bg="white")  # fundo branco

# Rodar a janela
janela1.mainloop()