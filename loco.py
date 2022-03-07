from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
import sys

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 0,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 0 
  })

DRIVER_PATH = 'driver/chromedriver.exe'
driver = webdriver.Chrome(options=opt, executable_path=DRIVER_PATH)

def read_exel_file(columnName):
    df = pd.read_excel (r'comments.xlsx')
    df = pd.DataFrame(df, columns= [columnName])
    df = df.to_numpy()
    commentArray = []
    for x in df:
        commentArray.append(x[0])
        print(x[0])
    print(commentArray)
    return commentArray

def login_comment(linkName, array_comment):
    try:
        print("Accessing Link")
        # stream_link = "https://loco.gg/stream/b869839a-0f37-4145-b09f-c1a663d88fe2"
        driver.get(linkName)
        pass
    except:
        print("Exception on live streaming url")
        pass
    sleep(5)
    print('sleep 10s ends')

    try:
        print("Click on Login Button")
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/button[3]").click()
    except:
        print("Exception on login")
        pass


    print('sleep 180s start')

    sleep(180)

    print('Sleep 180s ends')
    for liveComment in array_comment:
        try:
            print("Successfully Login")
            print("Writting comment")
            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
            pass
        except:
            print("Exception on writting comment")
            pass
        sleep(1)
        try:
            print("Publishing comment")
            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/button").click()
            pass
        except:
            print("Exception on posting comment")
            pass
        sleep(randint(30,60))

    # sleep(60)
    driver.quit()

if __name__ == "__main__":
    Link_url = sys.argv[2]
    col_name = str(sys.argv[1])
    if Link_url =="":
        print("Please attach URl to the Link")
    elif col_name == "":
        print("Please attach name of the column")
    else:
        print("File :", Link_url,"-------, Column Name", col_name)
        list_of_comments = read_exel_file(col_name)
        login_comment(Link_url, list_of_comments)