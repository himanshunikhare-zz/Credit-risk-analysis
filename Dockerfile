FROM python:3.6.3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip


# Required
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip \
    pip install -r requirements.txt 

EXPOSE 5000 

ENV FLASK_APP=project
ENV FLASK_DEBUG=1

ENTRYPOINT [ "flask" ] 
CMD [ "run","--host=0.0.0.0" ] 