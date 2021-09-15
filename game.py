from displays import stages
import os

max_mistakes = 15

def clear_console():
    command = 'clear'
    if os.name in ('ns', 'dos'):
        command = 'cls'
    os.system(command)


class Game:
    def __init__(self):
        self.width = 50
        self.height = 18
        self.view = 0
        self.mistakesMade = 0
        self.word = 'hallo'
        self.letter_index = -1

    def change_view(self, view=0):
        self.view = view
        self.draw_view(view)

    def generate_placeholder(self):
        placeholder = ''
        for i in range(len(self.word)):
            if i < self.letter_index:
                placeholder += self.word[i]
            else:
                placeholder += '_'
        return placeholder

    def draw_view(self, view):
        print(f"   Fouten gemaakt: {self.mistakesMade} | Woord: {self.generate_placeholder()}")
        print(" ")
        for line in stages[view]:
            print(line)
        print(" ")
        print("   Vul een woord in: ", end="")
        word = input('')
        if word.lower() != self.word:
            self.mistakesMade += 1
            if self.mistakesMade == max_mistakes:
                self.end_game()
            else:
                self.change_view(self.view + 1)
        else:
            self.end_game(True)


    def end_game(self, win = False):
        clear_console()
        if win:
            print('Je hebt gewonnen!')
        else:
            print('Je hebt verloren!')

    def launch(self):
        clear_console()
        self.draw_view(self.view)
