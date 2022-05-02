FROM python:3.9-slim-buster

WORKDIR /emis_python_engineer_task

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", './main.py' ]