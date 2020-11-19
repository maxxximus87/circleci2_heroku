import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_buttonPressed(self):
        ButtonPressed = "Yes"
        response = self.app.post('/button')
        if ButtonPressed in str(response.data):
            self.assertEqual(ButtonPressed, ButtonPressed)
        else:
            self.assertEqual(response.data, ButtonPressed)

if __name__ == '__main__':
    unittest.main()
