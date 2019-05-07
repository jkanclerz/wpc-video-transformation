import unittest
from dir_management import generate_dirname

class TestDirGeneration(unittest.TestCase):
    
    def test_generate_dir_name(self):
        # Arrange / Given
        name = "katalog jakuba k"
        # Act / When
        reslt_name = generate_dirname(name)
        # Assert / Then / Expect
        assert reslt_name == "katalog-jakuba-k"
    
    def test_addition(self):
        assert 2 + 2 == 4
        