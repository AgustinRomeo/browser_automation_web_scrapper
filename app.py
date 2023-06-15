from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    selected_tag = input("Enter your tag: ")

    chrome_path = r"C:\Users\outlet\Documents\ChromeDrive\chromedriver.exe"
    service = Service(chrome_path)
    chrome = webdriver.Chrome(service=service)
    chrome.get("https://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, selected_tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An Unknown error has occurred. Try Again")

input("Press Enter to exit...")
