import displays
import random


class Game:
    def __init__(self, word):
        self.tries = 0
        self.word = word.upper()
        self.guessed = []

    def start_game(self):
        self.clear_screen()
        print('Welcome to Hangman, this game is made by Maiky Perlee')
        print("I've created this game for school as part of the Python Achievements\n")
        print('Please enter Y to start the game')
        if input('').lower() == 'y':
            self.refresh(True, None, None)
        else:
            exit()

    def refresh(self, initial_start, incorrect_last, last_letter):
        if len(self.guessed) == len(self.word):
            self.end_game(True)
            return

        if self.tries == (len(displays.stages) - 1):
            self.end_game(False)
            return

        self.clear_screen()
        self.draw_screen()
        if not initial_start:
            if incorrect_last:
                print(f"You entered {last_letter}, this is unfortunately incorrect!")
            else:
                print(f"You entered {last_letter}, this is correct!")

        self.draw(displays.stages[self.tries])
        print('Guess a letter: ', '')
        try:
            letter = input('').upper()
            result = self.test_input(letter)
            if not result:
                self.tries += 1
                self.refresh(False, True, letter)
            else:
                self.refresh(False, False, letter)
        except KeyboardInterrupt:
            exit()

    def test_input(self, text) -> bool:
        if text in self.guessed:
            return False
        if text == self.word:
            for i in range(len(self.word)):
                if i in self.guessed:
                    continue
                else:
                    self.guessed.append(i)
                    return True
        elif text in self.word:
            found = 0
            for i in range(len(self.word)):
                if self.word[i] == text:
                    self.guessed.append(i)
                    found += 1
            if found == 0:
                return False
            return True
        return False

    def end_game(self, win: bool):
        if win:
            self.clear_screen()
            print("Congratulations! You've won!")
            print(f"You did this with {self.tries} tries, well done!")
            print("If you liked this small game please check out my GitHub I might've already made some new small "
                  "games! (https://github.com/Maiky1304)")
            print(' ')
            self.prompt_restart()
        else:
            self.clear_screen()
            print("Oh no! You've lost :(")
            print(f"The correct word was: {self.word}")
            print("If you liked this small game please check out my GitHub I might've already made some new small "
                  "games! (https://github.com/Maiky1304)")
            print(' ')
            self.prompt_restart()

    @staticmethod
    def prompt_restart():
        print('Use Y/N to restart/or exit the game')
        if input('').lower() == 'y':
            launch_app()
        else:
            exit()

    @staticmethod
    def draw(array):
        for line in array:
            print(line)

    def draw_screen(self):
        print(' ')
        print(f'  Tries {self.tries}/10  |  Word: {self.placeholder()}')

    @staticmethod
    def clear_screen():
        print(1000 * "\n")

    def placeholder(self):
        placeholder = ''
        for i in range(len(self.word)):
            if i in self.guessed:
                placeholder += self.word[i]
            else:
                placeholder += '_'
        return placeholder


def launch_app():
    game = Game(generate_word())
    game.start_game()


def generate_word() -> str:
    word_list = open('words.txt', 'r')
    word_array = []
    for line in word_list:
        word_array.append(line.strip())
    return word_array[random.randint(0, len(word_array))]


if __name__ == '__main__':
    launch_app()
