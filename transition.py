class Transition: # classe que vamos usar para armazenar as informações lidas no txt
    def __init__(self, currentState, currentSymbol, newState, newSymbol, direction):
        self.currentState = ""
        self.currentSymbol = ""
        self.newState = ""
        self.newSymbol = ""
        self.direction = ""