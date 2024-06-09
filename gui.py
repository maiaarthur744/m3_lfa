import tkinter as tk

#  código da m2 pra usar meio como base 

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1200x1000")
        self.window.title("Turing Machine")

        self.labelA = tk.Label(self.window, text="Campo A", font=("Arial", 18))
        self.labelA.pack(padx=20, pady=10)

        self.AField = tk.Text(self.window, height=10, font=("Arial", 18))
        self.AField.pack(padx=10, pady=20)

        self.buttonFrame = tk.Frame(self.window)

        self.analyseButton = tk.Button(self.buttonFrame, text="analisar", font=("Arial", 15), command=self.analyseRegularExpression)
        self.analyseButton.grid(row=0, column=0, padx=10)

        self.clearButton = tk.Button(self.buttonFrame, text="limpar", font=("Arial", 15), command=self.clearText)
        self.clearButton.grid(row=0, column=1)

        self.buttonFrame.pack()

        self.labelB = tk.Label(self.window, text="Campo B - Tokens", font=("Arial", 18))
        self.labelB.pack(padx=20, pady=10)

        self.BField = tk.Text(self.window, height=10, font=("Arial", 18), state='disabled')
        self.BField.pack(padx=10, pady=20)

        self.window.mainloop()

    def clearText(self):
        self.AField.delete("1.0", "end")
        self.BField.delete("1.0", "end")
        self.BField.config(state='disabled')

    def showOutput(self, output):
        self.BField.config(state='normal')
        self.BField.insert("1.0", output)
