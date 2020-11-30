FROM python:3.6.3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN apt-get install -y ghostscript libgs-dev
RUN apt-get install -y libmagickwand-dev imagemagick --fix-missing
RUN apt-get install -y libpng-dev zlib1g-dev libjpeg-dev

# Required
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip \
    pip install -r requirements.txt 
RUN chmod +x geckodriver
EXPOSE 5000 

# Unit tests

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
