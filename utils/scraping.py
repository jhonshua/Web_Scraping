# utils/scraping.py
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By # pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager


def scrape_airbnb_titles():
    """Realiza el scraping de títulos de Airbnb."""
    print("se ejecuta scrape_airbnb_titles")
    print(f'Scraping de Airbnb ejecutado a las {time.strftime("%H:%M:%S")}')
    
    opts = Options()
    
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
#opts.add_argument("--headless")

# Alternativamente:
# driver = webdriver.Chrome(
#     service=Service('./chromedriver'),
#     options=opts
# )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )

    driver.get('https://www.airbnb.com/')

    sleep(3)

    titulos_anuncios = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
    
    for titulo in titulos_anuncios:
        print(titulo.text)
    

    
    
    
