import yaml
import datetime

from Log import Log
from DataFileReader import DataFileReader


class ReportLoader:

    def __init__(self):
        self.config = {}
        self.data = {}
        self.date = datetime.datetime.now()

    def load_from_file(self, filename):
        Log.info("Loading report configuration: %s" % filename)

        try:
            with open(filename, 'r') as stream:
                return self.load_from_object(yaml.load(stream))
        except IOError:
            Log.fatal("Unable to load report")
            return False;

    def load_from_object(self, configuration_object):
        if self.check_object_requirements(configuration_object):
            self.config = configuration_object
            self.init_periods()
            self.load_data()

            return True
        else:
            return False

    def init_periods(self):
        Log.info("Initialize periods: %s" % self.config['meta']['periods'])

        for period in self.config['meta']['periods'].iterkeys():
            self.data[period] = {}

    def load_data(self):

        for item in self.config['inputs']:
            Log.info("-" * 60)
            Log.info("Loading input: %s" % item['name'])
            Log.debug("%s" % item)

            if item['type'] == 'file':
                dfr = DataFileReader(item['path'])

                if item['format'] == 'csv-kv':
                    self.data[item['period']].update(dfr.get_csv_kv())
                    Log.debug("Updated dataset: %s" % item['period'])
            else:
                Log.info("Not loading any data")
                pass

    def check_object_requirements(self, configuration_object):
        check = True
        mandatory = ("meta", "inputs")

        for key in configuration_object:
            Log.debug("Loading: %s" % key)

        for key in mandatory:
            if key not in configuration_object:
                Log.debug("Missing mandatory key: %s" % key)
                check = False

        return check
