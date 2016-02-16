# -*- coding: utf-8 -*-

import datetime

from Config import config


class Logger:

    def __init__(self):
        self._colors = {"green": "\033[1;32m",
                        "red": "\033[1;31m",
                        "yellow": "\033[1;33m",
                        "blue": "\033[1;34m",
                        "COLOR_END": "\033[1;m"}

        self._loglevel = config.get(section="logging",
                                    item="loglevel",
                                    default="INFO")

    def success(self, message):
        if self._loglevel in ("INFO", "DEBUG"):
            self._log(message=message, color="green", severity="INFO")

    def debug(self, message):
        if self._loglevel in "DEBUG":
            self._log(message=message, color="blue", severity="DEBUG")

    def info(self, message):
        if self._loglevel in ("INFO", "DEBUG"):
            self._log(message=message, color=None, severity="INFO")

    def error(self, message):
        if self._loglevel in ("ERROR", "INFO", "DEBUG"):
            self._log(message=message, color="yellow", severity="ERROR")

    def fatal(self, message):
        if self._loglevel in ("FATAL", "ERROR", "INFO", "DEBUG"):
            self._log(message=message, color="red", severity="FATAL")

    def _log(self, message, color=None, severity="INFO"):
        output = "%s [%s] %s" % (datetime.datetime.now().isoformat(),
                                 severity, message)

        if color is None:
            print output
        else:
            print "%s%s%s" % (self._colors.get(color), output,
                              self._colors["COLOR_END"])

Log = Logger()
