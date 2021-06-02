from app.sentimentAnalysis import readArticles, readHeadlines
from app.scraper import getArticlesCNN, getHeadlinesCNN, getHeadlinesNYT, getArticlesNYT, getHeadlinesWP, getHeadlinesDW, getArticlesDW, getArticlesFOX, getHeadlinesFOX, getHeadlinesHP, getArticlesHP, getHeadlinesNYP, getArticlesNYP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def mainAction(keywords, sources):
    keywords = keywords.lower()
    keywordArr = keywords.split(", ")
    options = Options()
    
    options.add_argument("--incognito")
    driver = webdriver.Chrome('.\drivers\chromedriver.exe', options=options)
    driver.set_page_load_timeout(5)

    rtn = [] #array of data
    
    #analyze all news sources chosen
    for i in sources:
        if ("CNN headlines (500)") == i:
            rtn.append(readHeadlines(getHeadlinesCNN(keywordArr, driver), keywordArr))

        if ("New York Post headlines (500)") == i:
            rtn.append(readHeadlines(getHeadlinesNYP(keywordArr, driver), keywordArr))
        
        if ("New York Post articles (50)") == i:
            rtn.append(readArticles(getArticlesNYP(keywordArr, driver), keywordArr))

        if ("CNN articles (50)") == i:
            rtn.append(readArticles(getArticlesCNN(keywordArr, driver), keywordArr))

        if ("New York Times headlines (500-limited)") == i:
            rtn.append(readHeadlines(getHeadlinesNYT(keywordArr, driver), keywordArr)) 

        if ("New York Times articles (50)") == i:
            rtn.append(readArticles(getArticlesNYT(keywordArr, driver), keywordArr)) #NEEDS AN ACCOUNT

        if ("Washington Post headlines (500)") == i:
            rtn.append(readHeadlines(getHeadlinesWP(keywordArr, driver), keywordArr))

        if ("Daily Wire headlines (500-limited)") == i:
            rtn.append(readHeadlines(getHeadlinesDW(keywordArr, driver), keywordArr))

        if ("Daily Wire articles (50)") == i:
            rtn.append(readArticles(getArticlesDW(keywordArr, driver), keywordArr))

        if ("FOX headlines (500-limited)") == i:
            rtn.append(readHeadlines(getHeadlinesFOX(keywordArr, driver), keywordArr))

        if ("FOX articles (50)") == i:
            rtn.append(readArticles(getArticlesFOX(keywordArr, driver), keywordArr))

        if ("Huffington Post headlines (500-limited)") == i:
            rtn.append(readHeadlines(getHeadlinesHP(keywordArr, driver), keywordArr))

        if ("Huffington Post articles (50)") == i:
            rtn.append(readArticles(getArticlesHP(keywordArr, driver), keywordArr))

    driver.quit()
    return rtn