from unittest import TestCase

from modules.Config import config


class ConfigTestCase(TestCase):

    def testConfig(self):
        self.assertEqual("1", config.get(item='version',
                                         section='config',
                                         default='not existent'))

        self.assertEqual("x", config.get(item='version',
                                         section='config-not',
                                         default='x'))

        self.assertEqual("x", config.get(item='version-not',
                                         section='config',
                                         default='x'))

        self.assertFalse(config.get(item='version-not',
                                    section='config-not'))

