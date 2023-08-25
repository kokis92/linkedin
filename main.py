from homePage import HomePage
import time

def test_Launch_HomePage():
    driver = HomePage()
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(10)


test_Launch_HomePage()