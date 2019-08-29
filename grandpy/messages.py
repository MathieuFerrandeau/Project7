"""Manage the display of messages"""
import random
from config import ADDRESS_MSG, SUMMARY_MSG, FAILURE_MSG

def return_failure():
    """Display failure messages"""
    message = random.choice(FAILURE_MSG)
    return message


def return_address(address):
    """Display address messages"""
    random_msg = random.choice(ADDRESS_MSG)
    message = "{} -{}".format(random_msg, address)
    return message


def return_story(summary):
    """Display summary messages"""
    random_msg = random.choice(SUMMARY_MSG)
    message = "{} {}...".format(random_msg, summary)
    return message
