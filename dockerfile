From python:3.10-slim-buster

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip3 install -r requirments.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]