FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 

# Unit tests
# RUN python test_basic.py

EXPOSE 5000 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 