from random import choice


class Hangman:
    __words = ["python", "java", "kotlin", "javascript"]

    def __init__(self):
        self.__word = self.set_word()

    @property
    def get_word(self):
        return self.__word

    def set_word(self):
        return choice(self.__words)

    def word_display(self, used_letters):
        return ' '.join('_' if i not in used_letters else i for i in self.__word)

class Player:
    __dictionary = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.__used_letters = []
        self.__quan_lives = 5

    def get_quan_lives(self):
        return self.__quan_lives
    
    def get_used_letters(self):
        return self.__used_letters
    
    def setter(self):
        self.__quan_lives -= 1

    def guess(self, letter):
        if letter.lower() not in self.__dictionary:
            return False
        self.__used_letters.append(letter)
        return True


hangman = Hangman()
player = Player()

print(f'In word {len(hangman.get_word)} letters')


def play_game():
    while True:
        correct_letter = False

        while not correct_letter:
            letter = input('Input letter: ')
            user_input = player.guess(letter)
            if user_input is True:
                correct_letter = True

        if letter in hangman.get_word:
            print(hangman.word_display(player.get_used_letters()))
            if all(letter in list(player.get_used_letters()) for letter in hangman.get_word):
                print('Player win. Good job, bro')
                break

        else:
            player.setter()
            print(f'You guessed wrong, try again. Your live {player.get_quan_lives()}')

            if player.get_quan_lives() == 0:
                print(f'Gameover. Hangman win. Word was {hangman.get_word}')
                break
            

if __name__ == '__main__':
    play_game()