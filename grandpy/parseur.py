"""Parseur module"""
import re


class Parseur:
    """Parseur classe"""
    def __init__(self, stop_words):
        """init stop_words"""
        self.stop_words = stop_words

    def get_relevant_word(self, input_user):
        """parse the user input to return the main keywords"""
        input_user = re.sub(r"\W+", " ", input_user).lower()
        input_user = input_user.split(" ")

        parsed_input = []
        for word in self.stop_words:
            if word in input_user:
                input_user.remove(word)
            parsed_input = ' '.join(input_user)

        parsed_input = parsed_input.strip()
        return parsed_input
