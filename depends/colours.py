# coding=utf-8
import string, sys

from system.constants import *

def colstrip(message):
    """
        Remove IRC colour codes from a message
    """
    if not message.strip(" ").strip("\n") == "":
        done = string.replace(message, irc_chars["col"] + "0", "")
        done = string.replace(done, irc_chars["col"] + "10", "")
        done = string.replace(done, irc_chars["col"] + "11", "")
        done = string.replace(done, irc_chars["col"] + "12", "")
        done = string.replace(done, irc_chars["col"] + "13", "")
        done = string.replace(done, irc_chars["col"] + "14", "")
        done = string.replace(done, irc_chars["col"] + "15", "")
        done = string.replace(done, irc_chars["col"] + "1", "")
        done = string.replace(done, irc_chars["col"] + "2", "")
        done = string.replace(done, irc_chars["col"] + "3", "")
        done = string.replace(done, irc_chars["col"] + "4", "")
        done = string.replace(done, irc_chars["col"] + "5", "")
        done = string.replace(done, irc_chars["col"] + "6", "")
        done = string.replace(done, irc_chars["col"] + "7", "")
        done = string.replace(done, irc_chars["col"] + "8", "")
        done = string.replace(done, irc_chars["col"] + "9", "")
        done = string.replace(done, irc_chars["col"], "")
        return done
    return ""

try:
    from colorama import Fore, Back, Style, init
except ImportError:
    def colprint(message):
        """
            Prints a message to the console in black-and-white as colorama is not installed
        """
        print colstrip(message)
else:

    init()

    def colprint(message):
        """
            Prints a message to the console in glorious colour
        """
        if not message.strip(" ").strip("\n") == "":
            message = (" " + message)

            done = string.replace(message, irc_chars["col"] + "00", Fore.WHITE + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "01", Fore.BLACK + Back.WHITE + Style.NORMAL)
            done = string.replace(done, irc_chars["col"] + "02", Fore.BLUE + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "03", Fore.GREEN + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "04", Fore.RED + Back.RESET + Style.NORMAL)
            done = string.replace(done, irc_chars["col"] + "05", Fore.RED + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "06", Fore.MAGENTA + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "07", Fore.YELLOW + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "08", Fore.YELLOW + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "09", Fore.GREEN + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "10", Fore.CYAN + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "11", Fore.CYAN + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "12", Fore.BLUE + Back.RESET)
            done = string.replace(done, irc_chars["col"] + "13", Fore.MAGENTA + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "14", Fore.WHITE + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "15", Fore.WHITE + Back.RESET + Style.NORMAL)
            done = string.replace(done, irc_chars["col"] + "0", Fore.WHITE + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "1", Fore.BLACK + Back.WHITE + Style.NORMAL)
            done = string.replace(done, irc_chars["col"] + "2", Fore.BLUE + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "3", Fore.GREEN + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "4", Fore.RED + Back.RESET + Style.NORMAL)
            done = string.replace(done, irc_chars["col"] + "5", Fore.RED + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "6", Fore.MAGENTA + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "7", Fore.YELLOW + Back.RESET + Style.DIM)
            done = string.replace(done, irc_chars["col"] + "8", Fore.YELLOW + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"] + "9", Fore.GREEN + Back.RESET + Style.BRIGHT)
            done = string.replace(done, irc_chars["col"], Fore.RESET + Back.RESET + Style.RESET_ALL)
            done = string.replace(done, "  ", " ")
            done = string.replace(done, "\t", "")
            done = done.lstrip()
            print(done + Fore.RESET + Back.RESET + Style.RESET_ALL)
