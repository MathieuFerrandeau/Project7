import random
from config import *

def return_failure():
    message = random.choice(FAILURE_MGS)
    return message


def return_address(address):
    random_msg = random.choice(ADRESS_MGS)
    message = "{} -{}".format(random_msg, address)
    return message


def return_story(summary):
    random_msg = random.choice(SUMMARY_MGS)
    message = "{} {}...".format(random_msg, summary)
    return message