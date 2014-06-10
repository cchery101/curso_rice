"""
Test suite for format function in "Stopwatch - The game"
"""


def run_test(format_function):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs
    suite.run_test(merge(0), "0:00.0", "Test #1:")


    suite.report_results()
