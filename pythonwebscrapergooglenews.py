# Dependencies
# pip install pandas
# pip install GoogleNews

# Imports
from GoogleNews import GoogleNews
import pandas as pd

def get_news():
    news_you_want = ('Ukraine War') # Specify the news keywords you want to search for
    gNews = GoogleNews(period='1')
    gNews.search(news_you_want)
    result = gNews.result()
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=['img'])
    data.head()

    for res in result:
        print ('Title: ', res['title'])
        print ('Details: ', res['link'])


# Call on function
get_news()