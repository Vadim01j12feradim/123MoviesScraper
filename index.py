from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver.get('https://ww2.123moviesfree.net/genre/action/')

def getDataVideo(click):
    if click:
        mid = driver.find_element(By.ID, "mid")
        mid.click()
        time.sleep(3)

        try:
            driver.switch_to.window(driver.window_handles[2])
            driver.close()
        except Exception as e:
                print("null")
        finally:
            driver.switch_to.window(driver.window_handles[1])

    playit = driver.find_element(By.ID, "playit")
    urlVideo = playit.get_attribute('src')
    print("Video"+urlVideo)

    Genre = driver.find_element(By.XPATH, "//strong[text()='Genre:']")
    Genre = Genre.find_element(By.XPATH, "..")
    Genres = Genre.find_elements(By.TAG_NAME, "a")
    for genre in Genres:
        print(genre.text)

    Actor = driver.find_element(By.XPATH, "//strong[text()='Actor:']")
    Actor = Actor.find_element(By.XPATH, "..")
    Actors = Actor.find_elements(By.TAG_NAME, "a")
    for act in Actors:
        print(act.text)
    
     
    Director = driver.find_element(By.XPATH, "//strong[text()='Director:']")
    Director = Director.find_element(By.XPATH, "..")
    print(Director.text)

    Country = driver.find_element(By.XPATH, "//strong[text()='Country:']")
    Country = Country.find_element(By.XPATH, "..")
    Countrys = Country.find_elements(By.TAG_NAME, "a")
    for countr in Countrys:
        print(countr.text)
    try:
        Episode = driver.find_element(By.XPATH, "//strong[text()='Episode:']")
        Episode = Episode.find_element(By.XPATH, "..")
        print(Episode.text)
    except Exception as e:
        Quality = driver.find_element(By.XPATH, "//strong[text()='Quality:']")
        Quality = Quality.find_element(By.XPATH, "..")
        print(Quality.text)
        
    Release = driver.find_element(By.XPATH, "//strong[text()='Release:']")
    Release = Release.find_element(By.XPATH, "..")
    Releases = Release.find_elements(By.TAG_NAME, "a")
    for rel in Releases:
        print(rel.text)
    

    IMDb = driver.find_element(By.XPATH, "//strong[text()='IMDb:']")
    IMDb = IMDb.find_element(By.XPATH, "..")
    print(IMDb.text)
    
    Duration = driver.find_element(By.XPATH, "//strong[text()='Duration:']")
    Duration = Duration.find_element(By.XPATH, "..")
    print(Duration.text)

    try:
        target_div = driver.find_element(By.XPATH, '//div[contains(@class,"fst-italic") and contains(@class,"lh-sm") and contains(@class,"mb-2")]')
        print(target_div.text)
    except Exception as e:
        print("null")



uniqueText = r"\w+"
# Print the text content of each element
Genres = driver.find_element(By.XPATH, '//a[contains(.,"Genres")]')
Genres.click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

Genres = Genres.find_element(By.XPATH, 'following-sibling::*')
Genres = Genres.find_elements(By.TAG_NAME, "li")

for gener in Genres:
    gener.click()
    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print("null")
    while True:
        main_element = driver.find_element(By.TAG_NAME, "main")
        Fch = main_element.find_element(By.TAG_NAME, "div")
        d1 = Fch.find_element(By.TAG_NAME, "div")
        d1 = d1.find_element(By.TAG_NAME, "h1")

        print("Gener: "+d1.text+"\n\n")

        elements_with_class = Fch.find_elements(By.CLASS_NAME, 'col')
        
        for element in elements_with_class:
            
            name = element.find_element(By.TAG_NAME, "h2")
            source = element.find_element(By.TAG_NAME, "a")
            img = element.find_element(By.TAG_NAME, "img")
            resolution = element.find_element(By.TAG_NAME, "span")
            span_element = driver.find_element(By.CLASS_NAME, 'mlbe')
            num = span_element.find_element(By.TAG_NAME, 'i').text

            text_content = span_element.text.replace(num, '')
            text_content = re.search(uniqueText, text_content)
            print("\n\nTitle:", name.text)
            print("Source:", source.get_attribute('href'))
            print("Img:", img.get_attribute('src'))
            print("Sol:", text_content.group(0))
            print("num:", num)

            new_tab_url = source.get_attribute('href')
            driver.execute_script(f'window.open("{new_tab_url}", "_blank");')

            driver.switch_to.window(driver.window_handles[1])

            driver.get(new_tab_url)

            getDataVideo(True)

            try:
                episodes = driver.find_element(By.ID, "eps-list")
                eps_list = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "eps-list"))
                )
                
                episodes = eps_list.find_elements(By.TAG_NAME, "button")
                ok = []
                ok.append(episodes[0].text)
                for epi in episodes:
                    if epi.text not in ok:
                        print(epi.text)
                        ok.append(epi.text)

                        driver.execute_script("arguments[0].click();", epi)
                        
                        time.sleep(3)

                        getDataVideo(False)

            except Exception as e:
                print("null")

            
            
            driver.switch_to.window(driver.window_handles[0])

            window_handles = driver.window_handles

            for window_handle in window_handles:
                if window_handle != driver.current_window_handle:
                    driver.switch_to.window(window_handle)
                    driver.close()

            driver.switch_to.window(driver.window_handles[0])

            time.sleep(2)
        try:
            Next = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
            Next.click()
        except Exception as e:
                break
        time.sleep(5)
driver.quit()

