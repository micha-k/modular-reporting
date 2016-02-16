import yaml
import datetime

from Log import Log


class ReportLoader:

    def __init__(self):
        self.config = {}
        self.data = {}
        self.date = datetime.datetime.now()

    def load_from_file(self, filename):
        Log.info("Loading report configuration: %s" % filename)

        with open(filename, 'r') as stream:
            return self.load_from_object(yaml.load(stream))

    def load_from_object(self, configuration_object):
        check = self.check_object_requirements(configuration_object)

        if check:
            self.config = configuration_object
            self.load_data()
            return False
        else:
            return False

    def load_data(self):

        for item in self.config['inputs']:
            Log.info("-" * 60)
            Log.info("Loading data source: %s" % item['name'])
            Log.debug("%s" % item)

            if item['type'] == 'file':

                if item['format'] == 'csv-kv':
                    Log.info("Wuerde jetzt die DS laden")




    def check_object_requirements(self, configuration_object):

        for key in configuration_object:
            Log.debug("Loading: %s" % key)

        # ToDo Write me
        return True