# coding=utf-8
# coding=utf-8
import os, random, time, math, traceback
import thread, string

from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory
from twisted.words.protocols import irc

from constants import *
from decorators import run_async

from depends import jsonapi

class Bot(irc.IRCClient):

    # Special IRC chars
    col = "" # Colour code
    bold = "" # Bold code
    under = "" # Underline code
    ital = "" # Italics code
    reverse = "" # Reverse code
    ctcp = "\1" # CTCP code, as if we'll ever need this

    def __init__(self):
        pass

    def connectionLost(self, reason):
        pass

    @property
    def nickname(self):
        return self.factory.nickname

    def signedOn(self):
        pass

    def joined(self, channel):
        pass

    @run_async
    def privmsg(self, user, channel, msg):
        pass

    def left(self, channel):
        pass

    @run_async
    def ctcpQuery(self, user, me, messages):
        pass

    def modeChanged(self, user, channel, set, modes, args):
        pass

    def kickedFrom(self, channel, kicker, message):
        pass

    def nickChanged(self, nick):
        pass

    def userJoined(self, user, channel):
        pass

    def userLeft(self, user, channel):
        pass

    def userKicked(self, kickee, channel, kicker, message):
        pass

    def irc_QUIT(self, user, params):
        pass

    def topicUpdated(self, user, channel, newTopic):
        pass

    def irc_NICK(self, prefix, params):
        # Someone changed their nick.
        pass

    def irc_RPL_WHOREPLY(self, *nargs):
        pass

    def irc_RPL_ENDOFWHO(self, *nargs):
        pass

class BotFactory(protocol.ClientFactory):
    protocol = Bot

    def __init__(self):
        pass

    def clientConnectionLost(self, connector, reason):
        pass

    def clientConnectionFailed(self, connector, reason):
        pass
