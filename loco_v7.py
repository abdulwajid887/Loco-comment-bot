from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from random import randint

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
            except Exception as e_lb:
                print('\n105: Exception on Live Button')
                print(e_lb)
                print('----------------------------------')
                return "loginFail"
        except Exception as log:
            print("110: Exception on login")
            print(log)
            print('----------------------------------')
            return False
                # pass
        # except:
        #     print("94: Exception on Live Button")
        #     return False
            # pass
        # pass
    except Exception as aurl:
        print("121: Exception on accessing url")
        print(aurl)
        print('----------------------------------')
        return False
        # pass
    sleep(5)
    print('sleep 10s ends')

def Comment(linkName, array_comment):
    global live_session
    live_session = True
    if not linkName == "null":
        try:
            print("134: Accessing Link")
            driver.get(linkName)
            # try:
            #     driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div")
            # except Exception as elb:
            #     print("139: Exception on Live Button")
            #     print(elb)
            #     print('----------------------------------')
            #     live_session = False
                # pass
            # pass
        except Exception as els:
            print("146: Exception on Accessing live streaming url")
            print(els)
            print('----------------------------------')
            live_session = False
            # pass
        sleep(5)
        print('sleep 10s ends')
    else:
        print("153: Link Name is NULL")
    if live_session:
        counter_exception = 0
        # print("156: Into Comments Section")
        for liveComment in array_comment:
            if str(liveComment) == "nan":
                print('159: Empty Comment found')
            else:
                try:
                    try:
                        print("163: Writting comment")
                        driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
                    except:
                        try:
                            print("167: Writting comment")
                            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[3]/div/input").send_keys(liveComment)
                        except:
                            try:
                                print("171: Refreshing page")
                                driver.get(linkName)
                                sleep(10)
                                try:
                                    print("175: Writting comment")
                                    driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
                                except:
                                    try:
                                        print("179: Writting comment")
                                        driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[3]/div/input").send_keys(liveComment)
                                    except:
                                        print("182: Exception")
                                        pass
                            except:
                                print("185: Exception")
                                pass
                            pass
                    # pass
                    try:
                        print("190: Publishing comment")
                        # driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/button").click()
                        driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/button[1]").click()
                        # pass
                    except Exception as epc:
                        print("\n195: Exception on posting comment")
                        print(epc)
                        print('----------------------------------')
                        try:
                            print("199: Writting comment")
                            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
                        except:
                            try:
                                print("203: Writting comment")
                                driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[3]/div/input").send_keys(liveComment)
                            except:
                                try:
                                    print("207: Refreshing page")
                                    driver.get(linkName)
                                    sleep(10)
                                    try:
                                        print("210: Writting comment")
                                        driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/div/input").send_keys(liveComment)
                                    except:
                                        try:
                                            print("215: Writting comment")
                                            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[3]/div/input").send_keys(liveComment)
                                        except:
                                            print("218: Exception")
                                            pass
                                except:
                                    print("221: Exception")
                                    pass
                                pass
                        # pass
                        try:
                            print("226: Publishing comment")
                            # driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[3]/div[3]/button").click()
                            driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[3]/div[3]/button[1]").click()
                            # pass
                        except Exception as epc:
                            print("\n231: Exception on posting comment")
                            print(epc)
                            print('----------------------------------')
                            if counter_exception > 4:
                                break
                            counter_exception += 1
                        # if counter_exception > 4:
                        #     break
                        # counter_exception += 1
                        # pass
                except Exception as ewc:
                    print("\n242: Exception on writting comment")
                    print(ewc)
                    print('----------------------------------')
                    if counter_exception > 4:
                        break
                    counter_exception += 1
                    # pass
                sleep(1)
                
            sleep_wait = randint(30,60)
            print('\n'+str(sleep_wait)+'s wait started\n')
            sleep(sleep_wait)
    else:
        print("255: Live Session is False")
    # sleep(60)
    # driver.quit()

if __name__ == "__main__":
    global live_session
    live_session = False
    Link_url = ""
    col_name = ""
    while Link_url=="":
        try:
            Link_url = input("Enter URL Link Plz : ")
            # Link_url = read_cred_file[2]
        except:
            print('269: Error in Link URL')
        pass
    while col_name=="":
        try:
            # col_name = (read_cred_file[1])[:-1]
            col_name = input("Enter Column Name Plz : ")
        except:
            print('276: Error in Column Name of comment')

    if Link_url =="":
        print("279: Please attach URl to the Link")
    elif col_name == "":
        print("281: Please attach name of the column")
    else:
        # try:
        print("File :", Link_url,"-------, Column Name", col_name)
        list_of_comments = read_exel_file(col_name)
        login(Link_url)
        Comment("null", list_of_comments)

        while True:
            live_session = True
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
                try:
                    list_of_comments = read_exel_file(new_comment_column)
                    Comment(new_url, list_of_comments)
                except Exception as emte:
                        print('314: Error in main try except')
                        print(emte)
                        print('----------------------------------')
            except:
                print('318: exception in main second except')