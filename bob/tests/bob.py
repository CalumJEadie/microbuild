#!/usr/bin/python

"""
Unit tests for the bob.bob module.

Run these tests using `python -m bob.tests.bob` from project root directory.
"""

import unittest

from .. import bob

class TestBuildSimple(unittest.TestCase):
        
    def test_get_tasks(self):
        import build_scripts.simple
        ts = bob._get_tasks(build_scripts.simple)
        print ts
        self.assertEqual(len(ts),5)
        
class TestBuildWithDependancies(unittest.TestCase):
        
    def test_get_tasks(self):
        import build_scripts.dependancies
        ts = bob._get_tasks(build_scripts.dependancies)
        print ts
        self.assertEqual(len(ts),5)
        
class TestDecorationValidation(unittest.TestCase):

    def test_1(self):
        with self.assertRaises(bob.TaskDecorationException) as cm:
            import build_scripts.annotation_misuse_1
        print cm.exception

    def test_2(self):
        with self.assertRaises(bob.TaskDecorationException) as cm:
            import build_scripts.annotation_misuse_2
        print cm.exception

    def test_3(self):
        with self.assertRaises(bob.TaskDecorationException) as cm:
            import build_scripts.annotation_misuse_3
        print cm.exception

if __name__ == "__main__":
    unittest.main(verbosity=2)
