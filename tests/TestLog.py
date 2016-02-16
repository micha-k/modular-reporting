from unittest import TestCase

from modules.Log import Log


class LogTestCase(TestCase):

    # Todo: Write real test(s)
    def testLogging(self):
        Log.debug("This is a debug message")
        Log.info("This is an info message")
        Log.error("This is an error message")
        Log.fatal("This is a fatal message")
        Log.success("This is a success message")

        self.assertTrue(True)
