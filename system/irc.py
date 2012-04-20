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

    def __init__(self):
        pass

    def connectionLost(self, reason):
        """
        Called when the connection is lost.

        Params:
            (str) reason: Reason for losing connection
        """
        pass

    @property
    def nickname(self):
        """
        The bot's current nickname.
        """
        return self.factory.nickname

    def signedOn(self):
        """
        Called when the bot has connected to the server and
        signed on.
        """
        pass

    def joined(self, channel):
        """
        Called when the bot joins a channel.

        Params:
            (str) channel: Channel that was joined
        """
        pass

    @run_async
    def privmsg(self, user, channel, msg):
        """
        Called when a message is received.

        Params:
            (str) user:    Userhost of the person that sent the message
            (str) channel: Channel where the message was sent
                (Can also be the nick of the bot in a query)
            (str) msg:     The message content
        """
        pass

    def left(self, channel):
        """
        Called when the bot leaves a channel.

        Params:
            (str) channel: Channel that was left
        """
        pass

    @run_async
    def ctcpQuery(self, user, me, messages):
        """
        Called when the bot recieves a CTCP Query.

        Params:
            (str ) user:     Userhost of whoever sent the query
            (??? ) me:       ???
            (list) messages: ???
        """
        pass

    def modeChanged(self, user, channel, set, modes, args):
        """
        Called when someone changes the mode in a channel.

        Params:
            (str )  user:    Userhost of whoever changed the modes
            (str )  channel: Channel the modes were set in (Could be the bot's name for umodes)
            (bool) set:     If the modes were set or unset
            (str ) modes:   The list of modes set
            (list) args:    The arguments for the modes
        """
        pass

    def kickedFrom(self, channel, kicker, message):
        """
        Called when the bot is kicked from a channel.

        Params:
            (str) channel: Channel the bot was kicked from
            (str) kicker:  Person who kicked the bot
            (str) message: Kick message that was issued
        """
        pass

    def nickChanged(self, nick):
        """
        Called when the bot is forced to change its nick.

        Params:
            (str) nick: New nick
        """
        pass

    def userJoined(self, user, channel):
        """
        Called when someone joins the channel.

        Params:
            (str) user:    Userhost of the person that joined
            (str) channel: Channel the person joined
        """
        pass

    def userLeft(self, user, channel):
        """
        Called when someone leaves the channel.

        Params:
            (str) user:    Userhost of the person that joined
            (str) channel: Channel the person joined
        """
        pass

    def userKicked(self, kickee, channel, kicker, message):
        """
        Called when someone is kicked from the channel.

        Params:
            (str) kickee:  Whoever was kicked
            (str) channel: The channel they were kicked from
            (str) kicker:  The person who kicked them
            (str) message: The kick message
        """
        pass

    def irc_QUIT(self, user, params):
        """
        Called when someone quits IRC.

        Params:
            (str) user:   The hostmask of the user who quit
            (???) params: ???
        """
        pass

    def topicUpdated(self, user, channel, newTopic):
        """
        Called when someone sets the topic (Also on channel join).

        Params:
            (str) user:     Userhost of whoever set the topic
            (str) channel:  Channel the topic was set in
            (str) newTopic: The new topic
        """
        pass

    def irc_NICK(self, prefix, params):
        """
        Called when someone changes the nick

        Params:
            (???) prefix: ???
            (???) params: ???
        """
        pass

    def irc_RPL_WHOREPLY(self, *nargs):
        """
        Called when the server responds to a WHO request.

        Params:
            (???) nargs: ???
        """
        pass

    def irc_RPL_ENDOFWHO(self, *nargs):
        """
        Called when the server finishes responding to a WHO request.

        Params:
            (???) nargs: ???
        """
        pass

class BotFactory(protocol.ClientFactory):
    protocol = Bot

    def __init__(self):
        pass

    def clientConnectionLost(self, connector, reason):
        """
        Called when the bot loses connection.

        Params:
            (Connector) connector: Connector object
            (str)       reason:    Reason for the disconnect
        """
        pass

    def clientConnectionFailed(self, connector, reason):
        """
        Called when the bot fails to connect.

        Params:
            (Connector) connector: Connector object
            (str)       reason:    Reason for the disconnect
        """
        pass
