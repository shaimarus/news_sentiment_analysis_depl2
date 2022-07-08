FROM python:3.9
RUN apt-get update 

RUN pip3 install torchserve torch-model-archiver torch-workflow-archiver transformers openpyxl
RUN mkdir /opt/flask_serv/
COPY . /opt/flask_serv/
RUN pip3 install -r /opt/flask_serv/requirements.txt
RUN cd /opt/flask_serv/sentiment_depl/serve/ && python ts_scripts/install_dependencies.py

