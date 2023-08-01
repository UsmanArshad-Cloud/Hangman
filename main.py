import Helpers
from Printers import *
from Helpers import *

tries = 7
user_word = []
Printers.print_rules()
word_topics = ['Fruits', 'Vegetables', 'Animals']
selected_topic = Helpers.choose_random_from_list(word_topics)  # Choose a topic of the Word
selected_word = Helpers.select_word_from_file(selected_topic)  # Choose a word from that topic file
print(f"Hint:Your Word is related to {selected_topic}")
print(f"Required Word is {selected_word}")
user_word.append(selected_word[0])  # Give First Letter of the Required Word as a hint
for i in range(len(selected_word) - 1):
    user_word.append("_")  # Keep other letters of the required word hidden
while tries != -1:  # Main Game Loop
    print(f"No of tries left are {tries}")
    Printers.print_current_word(user_word)
    Printers.print_hangman(tries, selected_word)
    index = 0
    tries = tries - 1  # Decrement the no of tries
    user_input = input("Input the letter/Word:").lower()  # Get User Input
    if len(user_input) > 1:  # If the user enters the whole word
        check = Helpers.check_win(selected_word, user_input)
        print("Congratulations! You saved Dude") if check else Printers.print_hangman(0, selected_word)
        break
    while index != -1:  # else check letter by letter
        index = selected_word.find(user_input, index + 1, len(selected_word))
        if index != -1:
            user_word[index] = selected_word[index]
    if Helpers.check_win(selected_word, user_word):  # Check if the user wins
        print("Congratulations! You saved Dude")
        break
