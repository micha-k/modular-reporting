# -*- coding: utf-8 -*-

from unittest import TestCase

from modules.DataFileReader import DataFileReader


class DataFileReaderTestCase(TestCase):

    def test_constructor(self):
        expected1 = ["This is a test file",
                    "with special chars: öäüÖÄÜ",
                    "over multiple lines"]
        expected2 = []

        dfr1 = DataFileReader('tests/files/simple_testfile_utf8')
        dfr2 = DataFileReader('tests/files/DOES_NOT_EXISTS')

        self.assertEqual(expected1, dfr1.lines)
        self.assertEqual(expected2, dfr2.lines)

    def test_csv_kv(self):
        expected1 = {"key_a": "2",
                     "Schlüssel B": "234243534636",
                     "zz Key Z": "929324243,234234,75454"}

        dfr1 = DataFileReader('tests/files/csv-kv_testfile')

        self.assertEqual(expected1, dfr1.get_csv_kv())