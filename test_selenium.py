from selenium import webdriver # Installera med pip install selenium
import time

driver = webdriver.Chrome() # Öppna en Chrome-webbläsare
driver.get('https://www.example.com') # Gå till en webbplats
print(driver.title) # Skriv ut sidans titel
time.sleep(5) # Vänta i 5 sekunder med sidan öppen
driver.quit() # Stäng webbläsaren