import unittest
from app.models import Headlines

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''

    def setUp(self):

        '''
        Set up method that will run before every Test
        '''
        self.new_headline = Headlines(None,'breaking news','breaking break news ','https://www.cnn.com/hakunamatata','image.com/hakunamatata','2017-09-28 16:06:30.439388')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_headline,Headlines))

if __name__ == '__main__':
  unittest.main()