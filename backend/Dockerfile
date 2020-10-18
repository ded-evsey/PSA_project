FROM python:3.8.5
WORKDIR /backend

# copy current directory to the working directory
ADD . /backend

# Install the python dependencies
RUN pip install -r requirements.txt

# start the uWSGI
CMD ["uwsgi", "app.ini"]