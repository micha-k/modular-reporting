from Log import Log
from Config import config

class DataFileReader:

    def __init__(self, filename):
        Log.info("Initializing Data File Reader: %s" % filename)
        self.filename = filename
        self.lines = []

        self.read_lines()

    def read_lines(self):
        try:
            with open(self.filename, 'r') as f:
                self.lines = f.read().splitlines()
                Log.info("File read: %s" % self.filename)
        except IOError:
                Log.error("File not readable: %s" % self.filename)

    def get_csv_kv(self):
        values = {}

        for line in self.lines:
            p = line.split(config.get(item="csvseparator",
                                      section="format",
                                      default=";"))

            if len(p) == 2:
                Log.debug("Extracted k/v pair: %s => %s"
                          % (p[0].strip(), p[1].strip()))
                values[p[0].strip()] = p[1].strip()
            else:
                Log.error("Unable to parse k/v pair: %s" % line)

        return values
