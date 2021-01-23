FROM python:3.8.5
WORKDIR /backend

# copy current directory to the working directory
ADD . /backend
RUN pip install -r requirements.txt &&\
    mkdir -p /root/.kaggle &&\
    cp kaggle.json /root/.kaggle/ &&\
    kaggle competitions download -c airbus-ship-detection &&\
    unzip airbus-ship-detection.zip -d input/ &&\
    rm airbus-ship-detection.zip
# start the uWSGI
CMD ["uwsgi", "app.ini"]