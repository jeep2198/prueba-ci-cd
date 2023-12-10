FROM python:3.8.3-alpine
COPY ./requirements.txt /requirements/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements/requirements.txt 

COPY ./main.py/ /main.py

CMD [ "python", "-u", "./main.py"]
