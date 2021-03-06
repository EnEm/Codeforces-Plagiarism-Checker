from bs4 import *
import requests
import json
import time
import os
from selenium import webdriver

def subDownload(contest,submission,submissions):

    files = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome( executable_path="chromedriver.exe", options=options )

    driver.get('https://codeforces.com/contest/' + str(contest) + '/submission/' + str(submission))
    
    code_page = driver.page_source
    soup_code = BeautifulSoup(code_page, 'lxml')
    source_text = soup_code.find( "pre", id="program-source-text" )

    language = source_text['class'][1][5:]

    for i in range(0,len(submissions)):

        print('\rDownloading Codes : ' + str(i+1) + '/' + str(len(submissions)) , end='')

        flag_exist = False
        lang_exist = None

        for filename in os.listdir('codes'):
            if os.path.splitext(filename)[0] == str(submissions[i]):
                flag_exist = True
                lang_exist = os.path.splitext(filename)[1][1:]

        if flag_exist:
            if lang_exist == language:
                files.append('codes/' + str(submissions[i]) + '.' + lang_exist)
            continue

        driver.get('https://codeforces.com/contest/' + str(contest) + '/submission/' + str(submissions[i]))

        code_page = driver.page_source
        soup_code = BeautifulSoup(code_page, 'lxml')
        source_text = soup_code.find( "pre", id="program-source-text" )

        if source_text['class'][1][5:] == language:
            files.append('codes/' + str(submissions[i]) + '.' + source_text['class'][1][5:])

        fn = open('codes/' + str(submissions[i]) + '.' + source_text['class'][1][5:] , 'w' )

        lines = source_text.find_all("li")

        for line in lines:
            words=line.stripped_strings
            for word in words:
                fn.write(repr(word.encode('utf-8'))[2:-1] + ' ')

            fn.write('\n')

        fn.close()

        time.sleep(2)

    driver.close()

    print('\nCompleted Downloading codes')

    return files