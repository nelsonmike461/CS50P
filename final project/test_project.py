import pytest
import unittest
from unittest.mock import MagicMock, patch
from project import get_tweet_data, scrape_tweets, main

class TestTwitterScraper(unittest.TestCase):
    def setUp(self):
        self.driver = MagicMock()
        self.card = MagicMock()

    def test_get_tweet_data(self):
        self.card.find_element.return_value.text = 'test'
        self.card.find_element.return_value.get_attribute.return_value = 'test'
        result = get_tweet_data(self.driver, self.card)
        expected_result = {
            'Username': 'test',
            'Datetime': 'test',
            'Text': 'test',
            'Reply': 'test',
            'Retweet': 'test',
            'Likes': 'test'
        }
        self.assertEqual(result, expected_result)

    @patch('project.webdriver.Chrome')
    def test_scrape_tweets(self, mock_chrome):
        # Mock the behavior of the Chrome driver
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        # Mock the behavior of a tweet card
        mock_card = MagicMock()
        mock_card.find_element.return_value.text = 'test'
        mock_card.find_element.return_value.get_attribute.return_value = 'test'

        # Mock the behavior of the find_elements method
        mock_driver.find_elements.return_value = [mock_card for _ in range(5)]

        # Mock the behavior of the execute_script method
        mock_driver.execute_script.side_effect = [0, 1, 2, 3, 4, 5]

        # Call the function with the mock driver
        data = scrape_tweets(mock_driver, 1)

        # Check that the result is as expected
        self.assertEqual(len(data), 1)



    @patch('project.webdriver.Chrome')
    @patch('project.getpass')
    @patch('project.input', create=True)
    def test_main(self, mock_input, mock_getpass, mock_chrome):
        mock_input.side_effect = ['username', 'search term', 'click on', '1']
        mock_getpass.return_value = 'password'
        main()
        self.assertTrue(mock_chrome.called)
        self.assertTrue(mock_input.called)
        self.assertTrue(mock_getpass.called)

if __name__ == '__main__':
    unittest.main()
