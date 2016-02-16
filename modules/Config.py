# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser, NoSectionError, NoOptionError


class ConfigurationSet:

    def __init__(self, filename):
        self.config = ConfigParser()
        self.config.readfp(open(filename))

    def get(self, item, section, default=None):
        try:
            result = self.config.get(section=section, option=item)
        except NoOptionError:
            result = default
        except NoSectionError:
            result = default

        return result

config = ConfigurationSet('settings.conf')
