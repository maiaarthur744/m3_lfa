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
    initial_state = ""
    final_state = ""

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            parts = line.strip().split(', ')
            if len(parts) == 5:
                transition = Transition(parts[0], parts[1], parts[2], parts[3], parts[4])
                transitions.append(transition)
        if lines:
            last_line = lines[-1].strip().split(', ')
            if len(last_line) == 2:
                initial_state, final_state = last_line

    return transitions, initial_state, final_state

def list_txt_files(directory='.'):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

