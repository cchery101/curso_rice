"""
Test suite for 2048
"""

import poc_simpletest

def run_test(merge):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs
    suite.run_test(merge([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1:")


    suite.report_results()
