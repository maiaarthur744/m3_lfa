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
            self.loadTuringMachine(selected_file)
        except tk.TclError:
            messagebox.showwarning("Nenhuma arquivo selecionado", "Por favor, selecione um arquivo da lista.")

    def loadTuringMachine(self, filename):
        self.transitions = utils.load_transitions(filename)
        self.clearWindow()

        self.labelC = tk.Label(self.window, text="Transições lidas do arquivo", font=("Arial", 18))
        self.labelC.pack(padx=20, pady=10)

        self.transitionField = tk.Text(self.window, height=10, font=("Arial", 18))
        self.transitionField.pack(padx=10, pady=20)
        self.transitionField.insert("1.0", "\n".join([f"{t.currentState}, {t.currentSymbol}, {t.newState}, {t.newSymbol}, {t.direction}" for t in self.transitions]))
        self.transitionField.config(state='disabled')

        self.labelD = tk.Label(self.window, text="Por favor informe a sentença que deseja reconhecer", font=("Arial", 18))
        self.labelD.pack(padx=20, pady=10)

        self.sentenceField = tk.Text(self.window, height= 5, font=("Arial", 18))
        self.sentenceField.pack(padx=10, pady=10)
        
        self.startButton = tk.Button(self.window, text="Iniciar", font=("Arial", 15), command=self.onButtonClick)
        self.startButton.pack(padx=10, pady=10)

    def onButtonClick(self):
        self.readSentence()
        self.startTuringMachine()

    def readSentence(self):
        self.sentence = self.sentenceField.get("1.0", "end-1c")

    def clearWindow(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def startTuringMachine(self):
        self.clearWindow()

        self.labelSteps = tk.Label(self.window, text="Passos da Execução\nSentença lida: " + self.sentence, font=("Arial", 18))
        self.labelSteps.pack(padx=20, pady=10)

        self.stepsField = tk.Text(self.window, height=20, font=("Arial", 18))
        self.stepsField.pack(padx=10, pady=20)

        self.resultLabel = tk.Label(self.window, text="", font=("Arial", 18)) # o que isso faz?
        self.resultLabel.pack(padx=20, pady=10)

        self.runTuringMachine()

    def runTuringMachine(self):
        currentState = '$'  # Estado inicial
        tape = list(self.sentence)
        head = 0
        step = 0

        while True:
            currentSymbol = tape[head] if head < len(tape) else ' '
            transition = next((t for t in self.transitions if t.currentState == currentState and t.currentSymbol == currentSymbol), None)

            if not transition:
                self.stepsField.insert("end", f"Passo {step}: {currentState}, Símbolo lido: {currentSymbol}, Fita: {''.join(tape)}\n")
                break

            tape[head] = transition.newSymbol
            currentState = transition.newState
            if transition.direction == 'D':
                head += 1
                if head >= len(tape):
                    tape.append(' ')
            elif transition.direction == 'E':
                head -= 1
                if head < 0:
                    tape.insert(0, ' ')
                    head = 0

            self.stepsField.insert("end", f"Passo {step}: {currentState}, Símbolo lido: {currentSymbol}, Fita: {''.join(tape)}\n")
            step += 1

        if currentState == 'x':  # Estado final de aceitação
            self.resultLabel.config(text="Sentença Aceita!")
        else:
            self.resultLabel.config(text="Sentença Rejeitada!")

# Criação da interface gráfica
if __name__ == "__main__":
    gui = GUI()
