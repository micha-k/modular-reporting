from unittest import TestCase

from modules.ReportLoader import ReportLoader


class ReportConfigurationTestCase(TestCase):

    def test_load_from_file(self):
        rcfg1 = ReportLoader()
        rcfg2 = ReportLoader()

        res1 = rcfg1.load_from_file('example.yaml')
        res2 = rcfg2.load_from_file('NOT_EXISTING')

        self.assertTrue(res1)
        self.assertFalse(res2)

    def test_load_from_object(self):
        rcfg = ReportLoader()

        obj_ok = {'inputs': [ {'name': 'test_input1', 'type': 'test'}],
                  'meta': {'periods': {'today': 'foo', 'yesterday': 'bar'}}}
        obj_nok = {'inputs': ['foo', 'bar', 'narf'],
                   'meta2': ['foo', 'bar', 'narf']}

        self.assertTrue(rcfg.load_from_object(obj_ok))
        self.assertFalse(rcfg.load_from_object(obj_nok))
