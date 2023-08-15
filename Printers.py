class Printers:
    @staticmethod
    def print_rules():
        print("""
    Welcome to Hangman Game!!!
    1-You only have 7 tries to guess the full word
    2-If you feel like you know the answer you can type full word
    3-But if the guessed word was wrong Your guy will be dead(x_x)!!!
        """)

    @staticmethod
    def print_current_word(user_word):
        print(f"Complete The Word:", end='')
        for j in range(len(user_word)):
            print(user_word[j], end='')
        print()

    @staticmethod
    def print_hangman(try_count, selected_word):
        if try_count == 7:
            print("""
            =========
                |
                |    ('-')
                ()   /| |\\
                     /  \\
            """)
        elif try_count == 6:
            print("""
            =========
                |
                |
              ('_')
            """)
        elif try_count == 5:
            print("""
            =========
                |
                |
              ('_')
              |   |
            """)
        elif try_count == 4:
            print("""
            =========
                |
                |
              ('_')
             /|   |
            """)
        elif try_count == 3:
            print("""
            =========
                |
                |
              ('_')
              /| |\\
            """)
        elif try_count == 2:
            print("""
            =========
                |
                |
              ('_')
              /| |\\
              /
            """)
        elif try_count == 1:
            print("""
            =========
                |
                |
              ('_')
              /| |\\
              /   \\
            """)
        else:
            print(f"""
    Correct Word was {selected_word}
    Out of Lives Dude Hanged
            =========
                |
                |
              (x_x)
              /| |\\
              /   \\
            """)
