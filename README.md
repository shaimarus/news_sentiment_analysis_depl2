# Sentiment analysis for news
This repo use https://github.com/karpathy/arxiv-sanity-lite and get news from flask web server<br/>
News get from https://newsapi.org. using API <br/>

## Installation (python 3.9)
* 1.pip install -r requirements.txt<br/>

* Installation transformers u can use (https://github.com/pytorch/serve.git) <br/>
apt update<br/>
apt install -y default-jdk <br/>
pip install torchserve torch-model-archiver torch-workflow-archiver <br/>
pip install transformers<br/>
python ./ts_scripts/install_dependencies.py<br/>

## Downloading news
* 2.News download from https://newsapi.org using API
* ![Image alt](https://github.com/shaimarus/news_sentiment_analysis/blob/main/news_api.jpg)
 we need run next scripts:<br/>
 python arxiv_daemon.py --num 1
 
 * run next script for compute some features:<br/>
 python compute.py
 
 ## Finally<br/>
 We run flask web server and get news sentiment analysis, higher score is positive news ohterwise is negative:<br/>
 python serve.py 
 * ![Image alt](https://github.com/shaimarus/news_sentiment_analysis/blob/main/news_sentiment_analysis_1.jpg)
 * ![Image alt](https://github.com/shaimarus/news_sentiment_analysis/blob/main/news_sentiment_analysis_2.jpg)
 
## How we get score for sentiment analysis?

* At the first we make simple text preparation and then get text summarization using transformers, pretrained  sshleifer/distilbart-cnn-12-6 <br/>
* After that, we use another transformers for sentiment analysys - distilbert-base-uncased-finetuned-sst-2-english
* ![Image alt](https://github.com/shaimarus/news_sentiment_analysis/blob/main/code_summarization_and_sentiment_analysis.jpg)
* ![Image alt](https://github.com/shaimarus/news_sentiment_analysis/blob/main/text_preparation.jpg)


