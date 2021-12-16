FROM python:3.7-alpine

WORKDIR /project3

ADD . /project3

RUN pip install -r requirements.txt

CMD ["python", "app.py"]


