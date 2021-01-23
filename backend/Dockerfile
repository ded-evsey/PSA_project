FROM python:3.8.5
WORKDIR /backend

# copy current directory to the working directory
ADD . /backend
RUN pip install -r requirements.txt
RUN mkdir -p /root/.kaggle &&\
    cp kaggle.json /root/.kaggle/
RUN kaggle competitions download -c airbus-ship-detection
# start the uWSGI
CMD ["uwsgi", "app.ini"]