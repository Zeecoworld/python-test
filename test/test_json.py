# Writing unit test case function here....

import unittest
from validate_json import validateJSON


class TestJson(unittest.TestCase):
    
    """
    Testing for json object validity for both input/output json objects
    
    """
    
    def test_json_input(self):
        self.assertFalse(validateJSON("data/data_2.json"))
    
    def test_json_output(self):
         self.assertFalse(validateJSON("schema/result1.json"))



if __name__ == "__main__":
    unittest.main()









