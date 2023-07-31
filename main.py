import random

word_list = [
    "guitar",
    "spirit",
    "college",
    "monster",
    "puzzle",
    "bicycle",
    "bottles",
    "morning",
    "sunset",
    "sunrise",
    "turtles",
    "chicken",
    "waffles",
    "weather",
    "wizards",
    "friends",
    "breathe",
    "capable",
    "wonders",
    "freedom",
    "rockets",
    "baskets",
    "dancing",
    "circles",
    "pillows",
    "flavors",
    "feather",
    "rainbow",
    "smiling",
    "monster",
    "whisper",
    "blossom",
    "journey",
    "scratch",
    "sailing",
    "silence",
    "society",
    "welfare",
    "enchant",
    "erasers",
    "letters",
    "eclipse",
    "blazing",
    "singing",
    "fishing",
    "feeling",
    "freeway",
    "gateway",
    "grizzly"
]


def print_current_word():
    print(f"Complete It:",end='')
    for j in range(len(selected_word)):
        print(user_word[j], end='')
    print()


def check_win(required_str, user_str_list):
    for j in range(len(required_str)):
        if required_str[j] != user_str_list[j]:
            return False
    return True


def print_hangman(try_count):
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
        print("""
        =========
            |
            |
          (x_x)
          /| |\\
          /   \\
        """)


selected_word = random.choice(word_list)
# selected_word = input()
tries = 7
print(f"Required Word is {selected_word}")
user_word = []
for i in range(len(selected_word)):
    if i == 0:
        user_word.append(selected_word[0])
    else:
        user_word.append("_")

while tries != -1:
    print(f"No of tries left are {tries}")
    print_current_word()
    print_hangman(tries)
    index = 0
    user_input = input("Input the letter:").lower()
    while index != -1:
        index = selected_word.find(user_input, index + 1, len(selected_word))
        if index != -1:
            found = True
            user_word[index] = selected_word[index]
        else:
            found = False
    if check_win(selected_word, user_word):
        print("Congratulations! You saved Dude")
        break
    tries = tries - 1
    if tries == 0:
        print("Out of Lives.Dude Hanged")
        print_hangman(tries)
        break
