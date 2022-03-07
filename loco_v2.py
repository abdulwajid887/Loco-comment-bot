from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from random import randint
import sys

from selenium.webdriver.common.proxy import Proxy, ProxyType

f = open("settings.txt", "r")
read_cred_file = f.readlines()
print(read_cred_file)

# proxy_ip_port = '116.202.165.119:3128'

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


if "no proxy" in str(read_cred_file[0]).lower():
    DRIVER_PATH = 'driver/chromedriver.exe'
    driver = webdriver.Chrome(options=opt, executable_path=DRIVER_PATH)
else:
    proxy_ip_port = read_cred_file[0]
    print('----------')
    print(proxy_ip_port)
    print('----------')

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    # replace 'your_absolute_path' with your chrome binary absolute path
    

    DRIVER_PATH = 'driver/chromedriver.exe'
    driver = webdriver.Chrome(options=opt, executable_path=DRIVER_PATH, desired_capabilities=capabilities)

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def read_exel_file(columnName):
    print('---------')
    print(columnName)
    print('-------')
    df = pd.read_excel (r'comments.xlsx')
    df = pd.DataFrame(df, columns= [columnName])
    df = df.to_numpy()
    commentArray = []
    for x in df:
        commentArray.append(x[0])
        print(x[0])
    print(commentArray)
    return commentArray

def login(linkName):
    try:
        print("Accessing Link")
        driver.get(linkName)
        # try:
        #     driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div")
        try:
            print("Click on Login Button")
            login_button = "LOGIN"
            while login_button == "LOGIN":
                print('\nPlease Login to continue !!!')
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/button[3]").click()
                print('sleep 10s start')
                sleep(10)
                print('Sleep 10s ends')
                
                continue_press = ""
                while continue_press == "":
                    continue_press = input('Enter any key to continue ---------- :')
                login_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div[3]/button[3]").text
                print('LOgin Info: ', login_button)
            print('\n-------------')
            print("Successfully Login")
            print('-------------\n')
            try:
                driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div")
            except:
                print('\n96: Exception on Live Button')
                return "loginFail"
        except:
            print("91: Exception on login")
            return False
                # pass
        # except:
        #     print("94: Exception on Live Button")
        #     return False
            # pass
        # pass
    except:
        print("98: Exception on accessing url")
        return False
        # pass
    sleep(5)
    print('sleep 10s ends')

def Comment(linkName, array_comment):
    live_session = True
    if not linkName == "null":
        try:
            print("Accessing Link")
            driver.get(linkName)
            try:
                driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div")
            except:
                print("111: Exception on Live Button")
                live_session = False
                # pass
            # pass
        except:
            print("115: Exception on live streaming url")
            live_session = False
            # pass
        sleep(5)
        print('sleep 10s ends')
    if live_session:
        for liveComment in array_comment:
            if str(liveComment) == "nan":
                print('Empty Comment found')
            else:
                try:
                    print("Writting comment")
                    driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
                    # pass
                    try:
                        print("Publishing comment")
                        driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/button").click()
                        # pass
                    except:
                        print("\n139: Exception on posting comment")
                        break
                        # pass
                except:
                    print("\n142: Exception on writting comment")
                    break
                    # pass
                sleep(1)
                
            sleep_wait = randint(30,60)
            print('\n'+str(sleep_wait)+'s wait started\n')
            sleep(sleep_wait)

    # sleep(60)
    # driver.quit()

if __name__ == "__main__":
    Link_url = ""
    col_name = ""
    while Link_url=="":
        try:
            Link_url = input("Enter URL Link Plz : ")
            # Link_url = read_cred_file[2]
        except:
            print('119: Error in Link URL')
        pass
    while col_name=="":
        try:
            # col_name = (read_cred_file[1])[:-1]
            col_name = input("Enter Column Name Plz : ")
        except:
            print('114: Error in Column Name of comment')

    if Link_url =="":
        print("Please attach URl to the Link")
    elif col_name == "":
        print("Please attach name of the column")
    else:
        # try:
        print("File :", Link_url,"-------, Column Name", col_name)
        list_of_comments = read_exel_file(col_name)
        login(Link_url)
        Comment("null", list_of_comments)

        while True:
            try:
                print("\n\n")
                new_url = ""
                new_comment_column = ""
                print("Previous URl was "+str(Link_url))
                while new_url =="":
                    new_url = input("Enter new Stream URl: ")
                    if new_url == "":
                        print("Enter Valid URL Please")
                        print()
                    else:
                        print("Previous Column Name was "+str(col_name))
                        while new_comment_column == "":
                            new_comment_column = input('Enter Column name for comments: ')
                            if new_comment_column == "":
                                print("Enter Valid Comment's Column Name please!")
                                print()
                print("\n\n")
                print("File :", new_url,"-------, Column Name", new_comment_column)
                list_of_comments = read_exel_file(new_comment_column)
                Comment(new_url, list_of_comments)
                print('197: Error in main try except')
            except:
                print('199: exception in main second except')
