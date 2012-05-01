# coding=utf-8
import traceback, os
from system.logger import Logger

if not os.path.exists("logs"):
    os.mkdir("logs")

log_handler = Logger(simpleoutput=False)

log_handler.info("Information")
log_handler.warn("Warning")
log_handler.error("Error")
log_handler.critical("Critical")
log_handler.debug("Debug")

try:
    raise Exception("Derp")
except Exception:
    for element in traceback.format_exc().split("\n"):
        if len(element.strip()) > 0:
            log_handler.error(element)
finally:
    log_handler._sessionEnd()