# test_wispforge.py
"""
Tests for WispForge module.
"""

import unittest
from wispforge import WispForge

class TestWispForge(unittest.TestCase):
    """Test cases for WispForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WispForge()
        self.assertIsInstance(instance, WispForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WispForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
