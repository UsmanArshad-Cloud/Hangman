import random


class Helpers:

    @staticmethod
    def choose_random_from_list(input_list):
        return random.choice(input_list)

    @staticmethod
    def check_win(required_str, user_str_list):
        for j in range(len(required_str)):
            if required_str[j].lower() != user_str_list[j].lower():
                return False
        return True

    @staticmethod
    def select_word_from_file(topic):
        with open(f'{topic}.txt', 'r') as f:
            words = f.read().split('\n')
            return Helpers.choose_random_from_list(words)
