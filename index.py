from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://ww2.123moviesfree.net/genre/action/')

main_element = driver.find_element(By.TAG_NAME, "main")
Fch = main_element.find_element(By.TAG_NAME, "div")
d1 = Fch.find_element(By.TAG_NAME, "div")
d1 = d1.find_element(By.TAG_NAME, "h1")

print("Gener: "+d1.text+"\n\n")

elements_with_class = Fch.find_elements(By.CLASS_NAME, 'col')

# Print the text content of each element
for element in elements_with_class:
    name = element.find_element(By.TAG_NAME, "h2")
    source = element.find_element(By.TAG_NAME, "a")
    img = element.find_element(By.TAG_NAME, "img")
    resolution = element.find_element(By.TAG_NAME, "span")
    print("Title:", name.text)
    print("Source:", source.get_attribute('href'))
    print("Img:", img.get_attribute('src'))
    print("Img:", resolution.text)

driver.quit()
