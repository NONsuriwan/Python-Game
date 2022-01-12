import random

def get_word():
    word = random.choice(word_list)
    return word.upper()
word_list = [
    'ware','soup','mountain','extend','brown','expert','tounge','human','backpack','crush','dentist','market','knee',
    'smite','windy','coin','throw','silence','buff','downfall','climb','lying','weather','snob','kick','match',
    'quaker','fireman','excite','mend','allergen','summer','coat','emerald','coherent','mimic','multiple','square',
    'funded','funnel','sailing','dream','mutation','stick','mystic','film','guide','strain','bishop',]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("มาเล่นHangmanกันเถอะ!")
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries > 0:
        guess = input("ลองเดาคำมาซัก 1 คำดูสิ: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("คุณได้ใช้",guess,"ไปแล้ว")
            elif guess not in word:
                print("ตัว",guess, "ไม่มีอยู่ในคำศัพท์")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess," เก่งมากคุณทายถูก!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("คุณได้ใช้",guess,"ไปแล้ว")
            elif guess != word:
                print("ตัว",guess, "ไม่มีอยู่ในคำศัพท์")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("ยินดีด้วย!คุณทำได้!")
    else:
        print("แย่จัง คุณหมดโอกาสเดาแล้ว คำที่ถูกคือ " + word + " ไว้มาลองครั้งหน้านะ!")

def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("เล่นอีกครั้งไหม? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()