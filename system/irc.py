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
        self.log_handler.debug("Bot instance created.")

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
        self.log_handler.info("Signed on.")
        for channel in self.channels_to_join:
            self.join(channel)

    def joined(self, channel):
        """
        Called when the bot joins a channel.

        Params:
            (str) channel: Channel that was joined
        """
        self.log_handler.info("Channel joined: %s" % channel)

    def privmsg(self, user, channel, msg):
        """
        Called when a message is received.

        Params:
            (str) user:    Userhost of the person that sent the message
            (str) channel: Channel where the message was sent
                (Can also be the nick of the bot in a query)
            (str) msg:     The message content
        """
        self.log_handler.info("%s | <%s> %s" % (channel, user, msg))

    def left(self, channel):
        """
        Called when the bot leaves a channel.

        Params:
            (str) channel: Channel that was left
        """
        self.log_handler.info("Channel parted: %s" % channel)

    def ctcpUnknownQuery(self, user, channel, tag, data):
        """
        Called when the bot recieves a CTCP Query.

        Params:
            (str ) user:     Userhost of whoever sent the query
            (??? ) me:       ???
            (list) messages: ???
        """
        self.log_handler.info("%s | [%s %s] %s" % (channel, user, tag, data))

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

        parsed_args = []

        for element in args:
            if element:
                parsed_args.append(element)
            else:
                parsed_args.append("")

        args = parsed_args
        del parsed_args

        if set:
            if channel == self.nickname:
                self.log_handler.info("%s | %s set mode +%s %s" % (channel, user, modes, " ".join(args)))
            else:
                self.log_handler.info("%s | %s set mode +%s %s" % (channel, user, modes, " ".join(args)))
        else:
            if channel == self.nickname:
                self.log_handler.info("%s | %s set mode -%s %s" % (channel, user, modes, " ".join(args)))
            else:
                self.log_handler.info("%s | %s set mode -%s %s" % (channel, user, modes, " ".join(args)))

    def kickedFrom(self, channel, kicker, message):
        """
        Called when the bot is kicked from a channel.

        Params:
            (str) channel: Channel the bot was kicked from
            (str) kicker:  Person who kicked the bot
            (str) message: Kick message that was issued
        """
        self.log_handler.info("%s | kicked by %s (%s)" % (channel, kicker, message))

    def nickChanged(self, nick):
        """
        Called when the bot is forced to change its nick.

        Params:
            (str) nick: New nick
        """
        self.log_handler.info("Nick changed to %s." % nick)

    def userJoined(self, user, channel):
        """
        Called when someone joins the channel.

        Params:
            (str) user:    Userhost of the person that joined
            (str) channel: Channel the person joined
        """
        self.log_handler.info("%s | %s joined." % (channel, user))

    def userLeft(self, user, channel):
        """
        Called when someone leaves the channel.

        Params:
            (str) user:    Userhost of the person that left
            (str) channel: Channel the person left
        """
        self.log_handler.info("%s | %s left." % (channel, user))

    def userKicked(self, kickee, channel, kicker, message):
        """
        Called when someone is kicked from the channel.

        Params:
            (str) kickee:  Whoever was kicked
            (str) channel: The channel they were kicked from
            (str) kicker:  The person who kicked them
            (str) message: The kick message
        """
        self.log_handler.info("%s | %s was kicked by %s (%s)." % (channel, kickee, kicker, message))

    def userQuit(self, user, message):
        """
        Called when someone quits IRC.

        Params:
            (str) user:    The hostmask of the user who quit
            (???) message: The user's quit message
        """
        self.log_handler.info("%s quit (%s)." % (user, message))

    def topicUpdated(self, user, channel, newTopic):
        """
        Called when someone sets the topic (Also on channel join).

        Params:
            (str) user:     Userhost of whoever set the topic
            (str) channel:  Channel the topic was set in
            (str) newTopic: The new topic
        """
        self.log_handler.info("%s | %s set topic to \"%s\"" % (channel, user, newTopic))

    def userRenamed(self, oldname, newname):
        """
        Called when someone changes the nick

        Params:
            (???) oldname: User's old nick
            (???) newname: User's new nick
        """
        self.log_handler.info("%s is now known as %s." % (oldname, newname))

class BotFactory(protocol.ClientFactory):

    def __init__(self, nickname, channels, jsonapi_settings, log_handler):
        self.nickname = nickname
        self.jsonapi_settings = jsonapi_settings
        self.log_handler = log_handler
        self.log_handler.debug("Creating protocol instance")
        self.protocol = Bot

        self.protocol.log_handler = log_handler
        self.protocol.jsonapi_settings = jsonapi_settings
        self.protocol.channels_to_join = channels

    def clientConnectionLost(self, connector, reason):
        """
        Called when the bot loses connection.

        Params:
            (Connector) connector: Connector object
            (str)       reason:    Reason for the disconnect
        """
        reason_string = str(reason).split(": ")[3]
        self.log_handler.warn("Connection lost: %s." % reason_string)

    def clientConnectionFailed(self, connector, reason):
        """
        Called when the bot fails to connect.

        Params:
            (Connector) connector: Connector object
            (str)       reason:    Reason for the disconnect
        """
        reason_string = str(reason).split(": ")[3]
        self.log_handler.warn("Connection failed: %s." % reason_string)
