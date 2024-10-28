from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from spelling_bee import * 

def online_bee():
    url = "https://www.nytimes.com/puzzles/spelling-bee"
    button_class = "pz-moment__button primary default"
    letter_class = "hive"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    button = driver.find_element(By.CSS_SELECTOR, f".{button_class.replace(' ', '.')}")
    button.click()

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    letters = soup.find("div",class_=letter_class)
    valid_pool = letters.text
    driver.quit()

    possible_words = get_words(WORD_FILE)
    invalid_pool = "abcdefghijklmnopqrstuvwxyz" 
    for letter in valid_pool:
        invalid_pool = invalid_pool.replace(letter,"")

    results = cull_words(possible_words,valid_pool,invalid_pool)
    results = sort_by_length(results)
    nice_print(results)
    panagrams(results,valid_pool)

if __name__ == "__main__":
    online_bee()