#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from modules.Log import Log


class ModularReporting:

    def __init__(self):
        pass

    def start(self, args):
        if len(args) < 3:
            self.display_help()
        else:
            Log.info("Startup Modular Reporting")

            commands = args[1]
            file = args[2]

            Log.debug("Command: %s" % commands)
            Log.debug("File: %s" % file)

            p = commands.split(",")

            if "collect" in p:
                Log.info("====================================")
                Log.info(" Next Stage: collecting report data")
                Log.info("====================================")

            if "generate" in p:
                Log.info("===============================")
                Log.info(" Next Stage: generate data set")
                Log.info("===============================")

            if "render" in p:
                Log.info("===========================")
                Log.info(" Next Stage: render report")
                Log.info("===========================")

    def display_help(self):
        print """
    Usage: ./mreporting.py <command(s)> <file>

    ./mreporting.py collect : Collection reporting data
    ./mreporting.py generate : Collection reporting data and generating global data set
    ./mreporting.py render : Render dataset as configured

    Commands may be chained:   collect,generate,render
    """

if __name__ == "__main__":
    mr = ModularReporting()
    mr.start(sys.argv)