import kopError as err 
import unittest
import kopREST


class test_JsonErrorUnexpected(unittest.TestCase):
    """Test of the possible errors in our application"""

    def test_simple(self):
        expectedResponse=err.JsonErrorUnexpected()
        self.assertEquals(expectedResponse.status_code,500)

if __name__ == '__main__':
    unittest.main()        