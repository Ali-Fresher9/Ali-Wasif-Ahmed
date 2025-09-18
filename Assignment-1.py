import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from gensim.summarization import summarize

# Fetch the article
url = 'https://example.com/news-article'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the article content
article = soup.find('div', class_='article-body').get_text()

# Preprocess the text
stop_words = set(stopwords.words('bengali'))
tokens = [word for word in article.split() if word not in stop_words]
cleaned_article = ' '.join(tokens)

# Summarize the article
summary = summarize(cleaned_article)

print(summary)
