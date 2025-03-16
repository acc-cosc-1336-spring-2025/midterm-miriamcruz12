import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config 

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config()) 
    def test_get_miles_per_hour():
        result = get_miles_per_hour(32, 60)
        assert result == 19.883872, f"Test failed! Expected 19.883872, but got {result}"
        print("Test passed!") 

    def test_get_fahrenheit(): 
        assert get_fahrenheit(0) == 32, "Test failed for Celsius 0!"
        assert get_fahrenheit(5) == 41, "Test failed for Celsius 5!"
        assert get_fahrenheit(10) == 50, "Test failed for Celsius 10!"
        print("All test passed!") 

    def test_function(): 
        assert get_assessment_value(10000) == 6000,"Test failed for assessment value 10000!"
        assert get_assessment_value(20000) == 12000,"Test failed for assessment value 20000!"
        assert round(get_tax_assessment(6000), 2) == 43.20, "Test failed for tax assessment 6000!"
        assert round(get_tax_assessment(10000), 2) == 72.00, "Test failed for tax assessment 10000!"

        print("All test cases passed!")

    test_functions()  