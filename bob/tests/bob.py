#!/usr/bin/python

"""
Unit tests for the bob.bob module.

Run these tests using `python -m bob.tests.bob` from project root directory.
"""

import unittest

from .. import bob

class TestBuildSimple(unittest.TestCase):

    def test_get_functions(self):
        import build_simple
        fs = bob._get_functions(build_simple)
        print fs
        self.assertEqual(len(fs),6)
        
    def test_get_tasks(self):
        import build_simple
        ts = bob._get_tasks(build_simple)
        print ts
        self.assertEqual(len(ts),5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
