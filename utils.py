import os

class Transition:
    def __init__(self, currentState, currentSymbol, newState, newSymbol, direction):
        self.currentState = currentState
        self.currentSymbol = currentSymbol
        self.newState = newState
        self.newSymbol = newSymbol
        self.direction = direction

def load_transitions(file_path):
    transitions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) == 5:
                transition = Transition(parts[0], parts[1], parts[2], parts[3], parts[4])
                transitions.append(transition)
    return transitions

def list_txt_files(directory='.'):
    """Retorna uma lista de arquivos .txt no diretório especificado."""
    return [f for f in os.listdir(directory) if f.endswith('.txt')]
