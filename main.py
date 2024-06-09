from transition import *

t1 = Transition("test", "test", "test", "test", "test")


# def analyseRegularExpression(self):
#     last_symbol = self.get_last_symbol(self.AField)
#     if last_symbol != '$':
#         self.AField.insert("end", '$')
#
#     symbol = ""
#     state = -1
#     matrix = [[-1]]
#     final_states = [0]
#
#     matrix = [[7, 1, 12, 5, 12],     # E0 - 0
#               [12, 12, 2, 12, 12],   # E1 - 1
#               [12, 3, 12, 12, 12],   # E2 - 2
#               [12, 12, 4, 12, 12],   # E3 - 3
#               [12, 1, 12, 5, 12],    # E4 - 4
#               [12, 12, 12, 6, 12],   # E5 - 5 - FINAL
#               [12, 12, 12, 5, 12],   # E6 - 6
#               [0, 9, 12, 12, 12],    # E7 - 7
#               [12, 9, 12, 12, 12],   # E8 - 8
#               [12, 12, 10, 12, 12],  # E9 - 9
#               [12, 11, 12, 6, 12],   # E10 - 10 - FINAL
#               [12, 12, 8, 12, 12],   # E11 - 11
#               [12, 12, 12, 12, 12]]  # ERRO
#
#     final_states = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
#     state = 0
#
#     arithmeticOperators = ['+', '-', '*', '/']
#     control_characters = ''.join(chr(i) for i in range(33))
#     alphabet = ['a', 'b', 'c', 'd']
#     currentSentence = ""
#     output = ""
#     index = "1.0"
#
#     symbol = self.AField.get(index)
#
#     while symbol != "$":
#         if symbol in arithmeticOperators:
#             if currentSentence != "":
#                 output = self.classifyExpression(
#                     currentSentence, final_states, state, output, alphabet)
#                 currentSentence = ""
#                 state = 0
#             output = output + "Operador aritmético: " + symbol + '\n'
#         elif symbol in control_characters:
#             if currentSentence != "":
#                 output = self.classifyExpression(
#                     currentSentence, final_states, state, output, alphabet)
#                 currentSentence = ""
#                 state = 0
#         elif symbol in alphabet:
#             currentSentence += symbol
#             state = matrix[state][alphabet.index(symbol)]
#         else:
#             currentSentence += symbol
#
#         index = self.AField.index(f"{index}+1c")
#         symbol = self.AField.get(index)
#
#     if currentSentence != "":
#         output = self.classifyExpression(
#             currentSentence, final_states, state, output, alphabet)
#
#     self.showOutput(output)
#
#
# def classifyExpression(self, currentSentence, final_states, state, output, alphabet):
#     if currentSentence[0] not in alphabet:
#         output = output + \
#             "ERRO: símbolo(s) inválido(s): " + currentSentence + '\n'
#         return output
#
#     elif any(char not in alphabet for char in currentSentence):
#         output = output + "ERRO: sentença inválida: " + currentSentence + '\n'
#         return output
#
#     elif final_states[state] == 1:
#         output = output + "Sentença válida: " + currentSentence + '\n'
#         return output
#
#     else:
#         output = output + "ERRO: sentença inválida: " + currentSentence + '\n'
#         return output
#
#
# def get_last_symbol(self, textField):
#     text_content = textField.get("1.0", "end-1c")
#
#     if text_content:
#         last_symbol = text_content[-1]
#         return last_symbol
#     else:
#         return None
