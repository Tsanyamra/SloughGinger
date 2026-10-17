# test_sloughginger.py
"""
Tests for SloughGinger module.
"""

import unittest
from sloughginger import SloughGinger

class TestSloughGinger(unittest.TestCase):
    """Test cases for SloughGinger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SloughGinger()
        self.assertIsInstance(instance, SloughGinger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SloughGinger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
