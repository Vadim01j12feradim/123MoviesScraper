from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Models import *
from db import *

sql = Sql()

driver.get('https://ww2.123moviesfree.net/genre/action/')

def getDataVideo(click, episod):
    genre = Genre()
    actor = Actor()
    video = Video()
    director = Director()
    country = Country()

    # driver.refresh()
    time.sleep(2)


    if click:
        img = driver.find_element(By.ID, "play-now")
        img = img.find_element(By.TAG_NAME, "picture")
        img = img.find_element(By.TAG_NAME, "img")
        src = img.get_attribute('src')
        video.Img = src
        sql.imgMovieSrcTemp = src
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

    video.Img = sql.imgMovieSrcTemp
    playit = driver.find_element(By.ID, "playit")
    urlVideo = playit.get_attribute('src')
    video.UrlVideo = urlVideo
    video.Episode = episod

    name = driver.find_element(By.TAG_NAME, "h1")
    video.Name = name.text
    openNewTab(urlVideo, 2)
    
    flag = 3
    while flag >= 0:
        try:
            time.sleep(8)
            Duration = driver.find_element(By.XPATH, '//div[contains(@class,"jw-icon") and contains(@class,"jw-icon-inline") and contains(@class,"jw-text")  and contains(@class,"jw-reset") and contains(@class,"jw-text-duration")]')
            video.Duration = Duration.get_attribute("innerHTML")
            if video.Duration == '00:00':
                flag -= 1
            else:
                break
        except Exception as e:
            flag -= 1
            print("null")
    if flag < 0:
        return -1

    driver.close()
    driver.switch_to.window(driver.window_handles[1])

    GenreD = driver.find_element(By.XPATH, "//strong[text()='Genre:']")
    GenreD = GenreD.find_element(By.XPATH, "..")
    Genres = GenreD.find_elements(By.TAG_NAME, "a")
    genresIds = []
    for genreD in Genres:
        genre.Name = genreD.text
        id = sql.insertGenre(genre)
        genresIds.append(id)
    video.Genre = genresIds

    ActorD = driver.find_element(By.XPATH, "//strong[text()='Actor:']")
    ActorD = ActorD.find_element(By.XPATH, "..")
    Actors = ActorD.find_elements(By.TAG_NAME, "a")
    actorsIds = []
    for act in Actors:
        actor.Name = act.text
        idA  = sql.insertActor(actor)
        actorsIds.append(idA)
    video.Actor = actorsIds

    DirectorStr = driver.find_element(By.XPATH, "//strong[text()='Director:']")
    DirectorStr = DirectorStr.find_element(By.XPATH, "..").text
    array_dir = re.split(r',', DirectorStr)
    directorIds = []
    for dir in array_dir:
        director.Name = dir
        idD = sql.insertDirector(director)
        directorIds.append(idD)
    video.Director = directorIds
        
    CountryD = driver.find_element(By.XPATH, "//strong[text()='Country:']")
    CountryD = CountryD.find_element(By.XPATH, "..")
    Countrys = CountryD.find_elements(By.TAG_NAME, "a")
    countryIds = []
    for countr in Countrys:
        country.Name = countr.text
        idC = sql.insertCountry(country)
        countryIds.append(idC)
    video.Country = countryIds

    Release = driver.find_element(By.XPATH, "//strong[text()='Release:']")
    Release = Release.find_element(By.XPATH, "..")
    Releases = Release.find_element(By.TAG_NAME, "a")
    video.Release = Releases.text
    
    IMDb = driver.find_element(By.XPATH, "//strong[text()='IMDb:']")
    IMDb = IMDb.find_element(By.XPATH, "..")
    pattern = re.compile(r'\w\.\w|\w+')  # Word boundary, one or more word characters
    result = pattern.findall(IMDb.text[6:])
    video.Score = result[0]
    
    Duration = driver.find_element(By.XPATH, "//strong[text()='Duration:']")
    Duration = Duration.find_element(By.XPATH, "..")
    print(Duration.text)

    try:
        Episode = driver.find_element(By.XPATH, "//strong[text()='Episode:']")
        Episode = Episode.find_element(By.XPATH, "..")
        pattern = re.compile(r'\d+')  # Word boundary, one or more word characters
        result = pattern.findall(Episode.text)
        # video.Episode = result[0]
        # print(Episode.text)
    except Exception as e:
        Quality = driver.find_element(By.XPATH, "//strong[text()='Quality:']")
        Quality = Quality.find_element(By.XPATH, "..")
        # video.Quality = Quality.text
        # print(Quality.text)

    try:
        description = driver.find_element(By.XPATH, '//div[contains(@class,"fst-italic") and contains(@class,"lh-sm") and contains(@class,"mb-2")]')
        video.Description = description.get_attribute("innerHTML")
    except Exception as e:
        print("null")
    idRet = sql.insertVideo(video)

    # Insert Actors
    Video_Actor = VideoActor()
    Video_Actor.IdVideo = idRet

    for act in actorsIds:
        Video_Actor.IdActor = act
        sql.insertVideoActor(Video_Actor)
    
    Video_Country = VideoCountry()
    Video_Country.IdVideo = idRet
    for coId in countryIds:
        Video_Country.IdCountry = coId
        sql.insertVideoCountry(Video_Country)

    Video_Director = VideoDirector()
    Video_Director.IdVideo = idRet
    for dirE in directorIds: 
        Video_Director.IdDirector = dirE
        sql.insertVideoDirector(Video_Director)

    Video_Genre = VideoGenre()
    Video_Genre.IdVideo = idRet
    for genR in genresIds:
        Video_Genre.IdGenre = genR
        sql.insertVideoGenre(Video_Genre)
    
    return idRet

def openNewTab(new_tab_url, target):        
    driver.execute_script(f'window.open("{new_tab_url}", "_blank");')
    driver.switch_to.window(driver.window_handles[target])
    driver.get(new_tab_url)

def getEpisodes():
    eps_list = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "eps-list"))
                    )
                    
    episodes = eps_list.find_elements(By.TAG_NAME, "button")
    return episodes
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
            
            video = Video()
            movie = Movie()
            serie = Serie()

            name = element.find_element(By.TAG_NAME, "h2")
            source = element.find_element(By.TAG_NAME, "a")
            new_tab_url = source.get_attribute('href')
            img = element.find_element(By.TAG_NAME, "img")
            resolution = element.find_element(By.TAG_NAME, "span")

            try:
                span_element = element.find_element(By.CLASS_NAME, 'mlbe')  
                num = span_element.find_element(By.TAG_NAME, 'i').text
                serie.Eps = num
                serie.Name = name.text
                serie.Img = img.get_attribute('src')
                idSerie = sql.insertSerie(serie)
                openNewTab(new_tab_url, 1)
                try:
                    
                    episodes = getEpisodes()#eps_list.find_elements(By.TAG_NAME, "button")

                    pattern = re.compile(r'\w+')  # Word boundary, one or more word characters
                    result = pattern.findall(episodes[0].get_attribute("innerHTML"))
                    result = result[1]
                    ok = []
                    ok.append(result)
                    idsMovies = []
                    firstEpisode = getDataVideo(True, result)
                    if firstEpisode != -1:
                        idsMovies.append(firstEpisode)
                    try:
                        for epi in episodes:
                            result = pattern.findall(epi.get_attribute("innerHTML"))
                            result = result[1]
                            if result not in ok:
                                ok.append(result)
                                driver.execute_script("arguments[0].click();", epi)
                                time.sleep(3)
                                idCurrent = getDataVideo(False, result)
                                if idCurrent != -1:
                                    idsMovies.append(idCurrent)
                                
                        serie_video = SerieVideo()
                        serie_video.IdSerie = idSerie

                        for mov in idsMovies:
                            serie_video.IdVideo = mov
                            sql.insertSerieVideo(serie_video)
                    except Exception as e:
                        e = 1
                        print(e)
                except Exception as e:
                    e = 1
                    print(e)
            except Exception as e:
                span_element = element.find_element(By.CLASS_NAME, 'mlbq').text
                movie.Quality = span_element
                movie.Img = img.get_attribute('src')
                openNewTab(new_tab_url, 1)

                
                movie.IdVideo = getDataVideo(True, "")
               
                if movie.IdVideo != -1: 
                    sql.insertMovie(movie)

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

