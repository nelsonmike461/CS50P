import sqlite3
from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()

    driver.get('https://twitter.com/login')
    sleep(4)

    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys(input('Username or email: '))
    username.send_keys(Keys.RETURN)
    sleep(2)

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys(getpass('Enter your password: '))
    password.send_keys(Keys.RETURN)
    sleep(6)

    search_input = driver.find_element(By.XPATH, "//input[@aria-label='Search query']")
    search_input.send_keys(input("Search: "))
    search_input.send_keys(Keys.RETURN)
    sleep(4)

    Search = driver.find_element(By.LINK_TEXT, input("Click on: ")).click()

    # Scrape given no of tweets
    num_tweets = int(input("Enter the number of tweets to scrape: "))

    data = scrape_tweets(driver, num_tweets)

    # Save the data to a SQLite database
    save_to_db(data)


def get_tweet_data(driver, card):
    try:
        username = card.find_element(By.XPATH, ".//span").text
        date_time = card.find_element(By.XPATH, ".//time").get_attribute('datetime')
        text = card.find_element(By.XPATH, ".//div[2]/div[2]/div[2]").text
        reply = card.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        retweet = card.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        likes = card.find_element(By.XPATH, ".//div[@data-testid='like']").text
    except StaleElementReferenceException:
        return None  # Return None if the element is stale
    tweet = {
        'Username': username,
        'Datetime': date_time,
        'Text': text,
        'Reply': reply,
        'Retweet': retweet,
        'Likes': likes
    }
    return tweet

def scrape_tweets(driver, num_tweets):
    data = []
    tweet_ids = set()
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True

    while scrolling and len(data) < num_tweets:
        page_cards = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        for card in page_cards:
            if len(data) >= num_tweets:
                break
            tweet = get_tweet_data(driver, card)
            if tweet:
                tweet_id = ''.join(tweet.values())
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)

        scroll_attempt = 0
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(1)
            cur_position = driver.execute_script("return window.pageYOffset;")
            if last_position == cur_position:
                scroll_attempt += 1

                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    sleep(2)
            else:
                last_position = cur_position
                break

    return data

def save_to_db(data):
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS tweets (
            Username TEXT,
            Retweet INTEGER,
            Likes INTEGER
        )
    ''')

    # Insert the data into the table
    for row in data:
        c.execute('''
            INSERT INTO tweets (Username, Datetime, Text, Reply, Retweet, Likes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row['Username'], row['Datetime'], row['Text'], row['Reply'], row['Retweet'], row['Likes']))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def read_from_db():
    # Connect to the SQLite database
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()

    # Execute a query
    c.execute("SELECT * FROM tweets")

    # Fetch and print all the rows
    for row in c.fetchall():
        print(row)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
