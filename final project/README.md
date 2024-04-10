# Twitter Scraper

This Python script uses Selenium WebDriver to automate a web browser for scraping tweets from Twitter.

## Dependencies

The script requires the following Python packages:

- sqlite3
- selenium
- getpass
- time

You can install these packages using pip:

```bash
pip install selenium
```

For web interactions, the script uses Chrome WebDriver. You can install it from the ChromeDriver website. Alternatives are available for other browsers.

## Description

The script has several functionalities:

- **Setup**: Imports necessary modules such as sqlite3 for database interactions, selenium.webdriver for web scraping, and getpass for secure password input.
- **Tweet Data Extraction**: The `get_tweet_data` function extracts data from a tweet card on a webpage. It retrieves the username, date/time, text, reply count, retweet count, and like count of a tweet.
- **Tweet Scraping**: The `scrape_tweets` function scrolls through a Twitter page and scrapes a specified number of tweets using the `get_tweet_data` function.
- **Data Storage**: The `save_to_db` function saves the scraped data into an SQLite database. It creates a new table if it doesn’t exist and inserts the tweet data into the table.
- **Data Retrieval**: The `read_from_db` function reads and prints all rows from the SQLite database.

## How to Run

1. Execute the program. It will automatically open the Chrome WebDriver and redirect to the Twitter login page.
2. Login with your credentials.
3. Search for the profile which you want to scrape.
4. To click on the profile, re-enter its name or you may choose the top latest pages to scrape in case you searched for a hashtag.
5. Enter the number of tweets you want to scrape.
6. The program will automatically scroll and scrape the data and will save it in a .db file.

## Video Demo

You can watch a video demo of the script at [this link](https://youtu.be/4BCYLSN1x4M).
