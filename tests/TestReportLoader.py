from unittest import TestCase

from modules.ReportLoader import ReportLoader


class ReportConfigurationTestCase(TestCase):

    def test_load_from_file(self):
        rcfg = ReportLoader()
        res = rcfg.load_from_file('example.yaml')

        self.assertTrue(True)

    # Todo: Write real test(s)
    def testTrue(self):
        self.assertTrue(True)
