# Python program to get top 100 rated movies from imdb 
import time
import pandas as pd
from selenium import webdriver 
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# util func	
def click(action_driver, browser_driver, element, quit_=False):
	try:
		time.sleep(1)
		action_driver.click(on_element=element)
		action_driver.perform()
		print("Done!")
		time.sleep(1)
		if quit_: 
			browser_driver.quit()
	except Exception as e:
		print("Failed Error: ",e)
		time.sleep(1)
		browser_driver.quit()


# chromedriver initialization
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(executable_path='/home/keshav/chromedriver',
				options=options)


# enter keyword to search (URL)
url = 'https://www.imdb.com/'
driver.get(url)
# action driver initialization
action = ActionChains(driver)

time.sleep(2)
# get hamburger from nav-bar
element = driver.find_element(By.CSS_SELECTOR,"#imdbHeader-navDrawerOpen--desktop > svg > path:nth-child(2)")
click(action, driver, element)
# get top rated movies button
element = driver.find_element(By.XPATH,"/html/body/div[2]/nav/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[3]")
click(action, driver, element)

# get data table
imdb_top_rated = driver.find_element(By.CSS_SELECTOR, "#main > div > span > div > div > div.lister > table > tbody")
rows = imdb_top_rated.find_elements(By.TAG_NAME,"tr")
# no of movies displayed
print(len(rows))


names = []
release_yrs = []
ratings = []


for row in rows[:100]:
	# data columns in table rows
	data_cols = row.find_elements(By.TAG_NAME,"td")
	name_release = data_cols[1]
	name = name_release.find_element(By.TAG_NAME,"a").text
	release_year = name_release.find_element(By.TAG_NAME,"span").text[1:-1]
	rating = data_cols[2].find_element(By.TAG_NAME,"strong").text

	# store data in lists
	names.append(name)
	release_yrs.append(release_year)
	ratings.append(rating)
	print(name, release_year, rating)

imdb_data = {
			"Name" : names,
			"Release Year" : release_yrs,
			"Rating" : ratings
			}

imdb_df = pd.DataFrame(imdb_data)
imdb_df.to_csv('imdb_db.csv', index=False)

time.sleep(5)
driver.quit()

