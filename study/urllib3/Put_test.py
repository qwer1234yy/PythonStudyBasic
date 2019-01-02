import unittest, requests

class MyTestCase(unittest.TestCase):
    def test_something(self):
        resp = requests.put('https://10.133.33.99:8090/ingestionagent/errorRetry')
        print(resp.text)



if __name__ == '__main__':
    unittest.main()
