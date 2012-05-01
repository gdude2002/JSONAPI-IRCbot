# coding=utf-8

"""
Contains variables that
are designed to never change.
"""

__author__ = "Gareth Coles"
__version__= "0.0.1"

irc_chars = {
    # Colour code: (code) (fg ##),(bg ##)
    "col":        ""  ,
    "color":      ""  ,
    "colour":     ""  ,

    # Bold code
    "bold":       ""  ,
    "strong":     ""  ,
    "heavy":      ""  ,

    # Underline code
    "under":      ""  ,
    "underline":  ""  ,
    "underscore": ""  ,

    # Italic code
    "ital":       ""  ,
    "italics":    ""  ,
    "em":         ""  ,
    "emphasis":   ""  ,

    # Reverse/blackout code
    "reverse":    ""  ,
    "blackout":   ""  ,

    # CTCP code
    "ctcp":       "\1",

    # "Reset"/normalize code
    "normal":     ""  ,
    "reset":      ""  ,
    "normalize":  ""
}

irc_cols = {
    "white": irc_chars["col"] + "0",
    "black": irc_chars["col"] + "1",
    "darkblue": irc_chars["col"] + "2",
    "dargreen": irc_chars["col"] + "3",
    "red": irc_chars["col"] + "4",
    "darkred": irc_chars["col"] + "5",
    "purple": irc_chars["col"] + "6",
    "orange": irc_chars["col"] + "7",
    "yellow": irc_chars["col"] + "8",
    "green": irc_chars["col"] + "9",
    "teal": irc_chars["col"] + "10",
    "cyan": irc_chars["col"] + "11",
    "blue": irc_chars["col"] + "12",
    "magenta": irc_chars["col"] + "13",
    "darkgrey": irc_chars["col"] + "14",
    "grey": irc_chars["col"] + "15"
}

mc_chars = {
    "bold": "&l",
    "strike": "&m",
    "underline": "&n",
    "italic": "&o",

    "reset": "&r",

    "random": "&k"
}

mc_cols = {
    "black": "&0",
    "darkblue": "&1",
    "darkgreen": "&2",
    "teal": "&3",
    "darkred": "&4",
    "purple": "&5",
    "gold": "&6",
    "grey": "&7",
    "darkgrey": "&8",
    "blue": "&9",
    "green": "&a",
    "cyan": "&b",
    "red": "&c",
    "pink": "&d",
    "yellow": "&e",
    "white": "&f"
}