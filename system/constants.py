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