# 247 Webscraping App
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://247sports.com/Season/2024-Football/RecruitRankings/?InstitutionGroup=HighSchool")

try:
    # scroll to the bottom of the page
    print("Scrolling to the bottom of the page...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # click the "load more" button repeatedly until it is no longer visible
    print("Clicking the 'Load More' button...")
    while True:
        try:
            main = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//li[@class='rankings-page__list-item rankings-page__showmore showmore_blk']//a")))
            driver.execute_script("arguments[0].click();", main)
            print("Clicked the 'Load More' button.")
        except:
            print("No more 'Load More' button found.")
            break

    # find all the player names and print them
    print("Printing the player names...")
    recruits = driver.find_elements(By.CLASS_NAME, "rankings-page__list-item")
    for recruit in recruits:
        try:
            name = recruit.find_element(By.XPATH, ".//a[@class='rankings-page__name-link']")
            print(name.text)
        except:
            pass

finally: 
    driver.quit()



