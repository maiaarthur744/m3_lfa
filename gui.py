import tkinter as tk
from tkinter import messagebox, Listbox
import utils

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1200x1000")
        self.window.title("Turing Machine")

        self.labelA = tk.Label(self.window, text="Arquivos .txt no diretório", font=("Arial", 18))
        self.labelA.pack(padx=20, pady=10)

        self.AField = tk.Text(self.window, height=10, font=("Arial", 18))
        self.AField.pack(padx=10, pady=20)
        self.AField.config(state='disabled')

        self.listFiles()

        self.labelB = tk.Label(self.window, text="Selecionar arquivo", font=("Arial", 18))
        self.labelB.pack(padx=20, pady=10)

        self.fileList = Listbox(self.window, font=("Arial", 18))
        self.fileList.pack(padx=10, pady=20)
        self.populateFileList()

        self.selectButton = tk.Button(self.window, text="Selecionar", font=("Arial", 15), command=self.selectFile)
        self.selectButton.pack(padx=10, pady=10)

        self.window.mainloop()

    def listFiles(self):
        txt_files = utils.list_txt_files()
        self.AField.config(state='normal')
        self.AField.delete("1.0", "end")
        for file in txt_files:
            self.AField.insert("end", file + '\n')
        self.AField.config(state='disabled')

    def populateFileList(self):
        txt_files = utils.list_txt_files()
        for file in txt_files:
            self.fileList.insert("end", file)

    def selectFile(self):
        try:
            selected_file = self.fileList.get(self.fileList.curselection())
            self.showSelectedFile(selected_file)
        except tk.TclError:
            messagebox.showwarning("Nenhuma seleção", "Por favor, selecione um arquivo da lista.")

    def showSelectedFile(self, filename):
        messagebox.showinfo("Arquivo Selecionado", f"Você selecionou o arquivo: {filename}")

# Criação da interface gráfica
if __name__ == "__main__":
    gui = GUI()
