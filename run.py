# coding=utf-8
import traceback, os, sys
from system.logger import Logger
from system.constants import *
from system.irc import *

sys.path.append("depends")

if not os.path.exists("logs"):
    os.mkdir("logs")

from system.yaml_loader import yaml_loader

config = yaml_loader()
data = config.load("config/config.yml")
irc_settings =     data["irc"]
logging_settings = data["logging"]
jsonapi_settings = data["jsonapi"]

del data, config

log_handler = Logger(logging_settings["simple"], logging_settings["timestamps"], logging_settings["debug"])

log_handler._sessionStart()

log_handler.info("Starting up...")

try:
    log_handler.debug("Creating factory..")
    factory = BotFactory(irc_settings["nick"], irc_settings["channels"], jsonapi_settings, log_handler)
    log_handler.debug("Setting up reactor..")
    reactor.connectTCP(irc_settings["server"], irc_settings["port"], factory, irc_settings["timeout"])
    log_handler.debug("Running reactor..")
    reactor.run()
except Exception:
    for element in traceback.format_exc().split("\n"):
        if len(element.strip()) > 0:
            log_handler.error(element)
finally:
    log_handler.info("Shutting down...")
    log_handler.debug("Finishing execution..")
    log_handler._sessionEnd()