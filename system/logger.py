# coding=utf-8

import datetime, sys

class Logger(object):

    """
    Output styler and logger.

    This is to be used for ALL OUTPUT. ALL OF IT.

    It styles output in the corresponding format.
    """

    def __init__(self, simpleoutput=True, timestamps=True, sessionoutput=True):
        self.simpleoutput = simpleoutput
        self.timestamps = timestamps

        self.files = {
            "console": "logs/console.log",
            "info": "logs/info.log",
            "warn": "logs/warn.log",
            "error": "logs/error.log",
            "critical": "logs/critical.log",
            "debug": "logs/debug.log",
        }

        if sessionoutput:
            for element in self.files.values():
                self._writeToFile("=== Session started: %s" % datetime.datetime.now().strftime(" %d/%b/%Y %H:%M:%S ===")
                    , element)

    def _writeToFile(self, data, filename):
        """
            Writes to a file, adds a newline and flushes.
        """
        fileobj = open(filename, "a")
        fileobj.write(data)
        fileobj.write("\n")
        fileobj.flush()
        fileobj.close()

    def _sessionStart(self):
        for element in self.files.values():
            self._writeToFile("=== Session started: %s\n\n" % datetime.datetime.now().strftime(" %d/%b/%Y %H:%M:%S ===")
                , element)

    def _sessionEnd(self):
        for element in self.files.values():
            self._writeToFile("=== Session finished: %s\n\n" % datetime.datetime.now().strftime(" %d/%b/%Y %H:%M:%S ===")
                , element)

    def info(self, message):
        """
            Info-level logging
        """

        timestamp = datetime.datetime.now().strftime("| %d %b %Y | %H:%M:%S |")

        if self.simpleoutput:
            identifier = " "
        else:
            identifier = " INFO     "
        if self.timestamps:
            data = "%s%s| %s" % ( timestamp, identifier, message )
            self._writeToFile(data, self.files["console"])
            self._writeToFile(data, self.files["info"])
        else:
            data = "|%s| %s" % ( identifier, message )
            self._writeToFile(timestamp + data, self.files["console"])
            self._writeToFile(timestamp + data, self.files["info"])

        print data


    def warn(self, message):
        """
            Warn-level logging
        """

        timestamp = datetime.datetime.now().strftime("| %d %b %Y | %H:%M:%S |")

        if self.simpleoutput:
            identifier = "-"
        else:
            identifier = " WARNING  "
        if self.timestamps:
            data = "%s%s| %s" % ( timestamp, identifier, message )
            self._writeToFile(data, self.files["console"])
            self._writeToFile(data, self.files["warn"])
        else:
            data = "|%s| %s" % ( identifier, message )
            self._writeToFile(timestamp + data, self.files["console"])
            self._writeToFile(timestamp + data, self.files["warn"])

        print data

    def error(self, message):
        """
            Error-level logging
        """

        timestamp = datetime.datetime.now().strftime("| %d %b %Y | %H:%M:%S |")

        if self.simpleoutput:
            identifier = "*"
        else:
            identifier = " ERROR    "
        if self.timestamps:
            data = "%s%s| %s" % ( timestamp, identifier, message )
            self._writeToFile(data, self.files["console"])
            self._writeToFile(data, self.files["error"])
        else:
            data = "|%s| %s" % ( identifier, message )
            self._writeToFile(timestamp + data, self.files["console"])
            self._writeToFile(timestamp + data, self.files["error"])

        print data

    def critical(self, message):
        """
            Critical-level logging
        """

        timestamp = datetime.datetime.now().strftime("| %d %b %Y | %H:%M:%S |")

        if self.simpleoutput:
            identifier = "!"
        else:
            identifier = " CRITICAL "
        if self.timestamps:
            data = "%s%s| %s" % ( timestamp, identifier, message )
            self._writeToFile(data, self.files["console"])
            self._writeToFile(data, self.files["critical"])
        else:
            data = "|%s| %s" % ( identifier, message )
            self._writeToFile(timestamp + data, self.files["console"])
            self._writeToFile(timestamp + data, self.files["critical"])

        print data

    def debug(self, message):
        """
            Debug-level logging
        """

        timestamp = datetime.datetime.now().strftime("| %d %b %Y | %H:%M:%S |")

        if self.simpleoutput:
            identifier = "?"
        else:
            identifier = " DEBUG    "
        if self.timestamps:
            data = "%s%s| %s" % ( timestamp, identifier, message )
            self._writeToFile(data, self.files["console"])
            self._writeToFile(data, self.files["debug"])
        else:
            data = "|%s| %s" % ( identifier, message )
            self._writeToFile(timestamp + data, self.files["console"])
            self._writeToFile(timestamp + data, self.files["debug"])

        print data