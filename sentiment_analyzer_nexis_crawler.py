from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

top_30_djia_companies = [
    # "Amazon.com Inc",
    # "American Express Co",
    # "Amgen Inc",
    # "Apple Inc",
    # "Boeing Co",
    # "Caterpillar Inc",
    # "Cisco Systems Inc",
    # "Chevron Corp",
    # "Goldman Sachs Group Inc",
    # "Home Depot Inc",
    # "Honeywell International Inc",
    # "International Business Machines Corp",
    # "Johnson & Johnson",
    # "Coca-Cola Co",
    # "JPMorgan Chase & Co",
    # "McDonald's Corp",
    # "3M Co",
    # "Merck & Co Inc",
    # "Microsoft Corp",
    # "Nike Inc",
    # "Procter & Gamble Co",
    "Sherwin-Williams Co",
    "Travelers Companies Inc",
    "Unitedhealth Group Inc",
    "Salesforce Inc",
    "NVIDIA Corp",
    "Verizon Communications Inc",
    "Visa Inc",
    "Walmart Inc",
    "Walt Disney Co"
]

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\samue\\Downloads\\ucf"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get("https://guides.ucf.edu/database/LNA")

# Set wait
wait = WebDriverWait(driver, 60)

# Log in to nexus
# Username
wait.until(ec.element_to_be_clickable((By.NAME, "loginfmt"))).send_keys("sa820782@ucf.edu")
wait.until(ec.element_to_be_clickable((By.ID, "idSIButton9"))).click()

# Password
wait.until(ec.element_to_be_clickable((By.NAME, "passwd"))).send_keys("************")
wait.until(ec.element_to_be_clickable((By.ID, "idSIButton9"))).click()

# Click "News" link
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='gvs-tab-button-link new-gvs-tab-button-link' and contains(text(), 'News')]"))).click()

# Click Advanced Search
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(text(), 'Advanced Search')]"))).click()

# Loop through each company name, enter search term, pull first 10 articles
for i in range(0, 30):
    # Enter search term
    wait.until(ec.element_to_be_clickable((By.ID, "searchTerms"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "searchTerms"))).send_keys(top_30_djia_companies[i])

    # Enter from and to dates, publication type, select English
    wait.until(ec.element_to_be_clickable((By.ID, "dateFrom"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "dateFrom"))).send_keys("01/01/2024")

    wait.until(ec.element_to_be_clickable((By.ID, "dateTo"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "dateTo"))).send_keys("07/31/2024")

    wait.until(ec.element_to_be_clickable((By.ID, "publication-type"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "publication-type"))).send_keys("Newspapers")

    wait.until(ec.element_to_be_clickable((By.XPATH, "//option[contains(@class, 'languageoption') and @value='ZW4']"))).click()

    # Click search button
    #wait.until(ec.element_to_be_clickable((By.ID, "mainSearch"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='button' and @data-action='search' and contains(text(), 'Search')]"))).click()

    # Set Geography filter
    wait.until(ec.element_to_be_clickable((By.ID, "podfiltersbuttonen-geography-news"))).click()
    time.sleep(1)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'supplemental filters') and @data-id='en-geography-news']/li/label/span[contains(text(), 'North America')]/../.."))).click()
    time.sleep(1)

    wait.until_not(ec.text_to_be_present_in_element_attribute((By.ID, "hc-yk"), "class", "loading"))

    # Set Subject filter
    wait.until(ec.element_to_be_clickable((By.ID, "podfiltersbuttonen-subject"))).click()
    time.sleep(1)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'supplemental filters') and @data-id='en-subject']/li/label/span[contains(text(), 'Business News')]/../.."))).click()
    time.sleep(1)

    wait.until_not(ec.text_to_be_present_in_element_attribute((By.ID, "hc-yk"), "class", "loading"))
    time.sleep(5)

    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@data-action='downloadopt' and @data-qaid='toolbar_downloadopt']"))).click()

    wait.until(ec.element_to_be_clickable((By.ID, "SelectedRange"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "SelectedRange"))).send_keys("1-10")

    wait.until(ec.element_to_be_clickable((By.ID, "Rtf"))).click()

    wait.until(ec.element_to_be_clickable((By.ID, "FileName"))).clear()
    wait.until(ec.element_to_be_clickable((By.ID, "FileName"))).send_keys(f"{top_30_djia_companies[i].replace(" ", "").replace(".", "").replace("'", "").replace("&", "").replace("-", "")}")
    time.sleep(5)

    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @data-action='download' and contains(text(), 'Download')]"))).click()
    time.sleep(120)

    wait.until(ec.element_to_be_clickable((By.XPATH, "//ul[@class='header-breadcrumb']/li[contains(@class, 'tierTwoBreadcrumb')]/a[@class='tier2BrdCrb' and @title='News' and contains(text(), 'News')]"))).click()