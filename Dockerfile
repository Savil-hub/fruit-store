# From a certain lighter version of python
FROM python:3.10-slim-buster

# This can be called anything this is ran within the image
WORKDIR /app

# This copies requirements.txt from the computer to the image and calls it requirements.txt
COPY requirements.txt requirements.txt

# Intalls th requirements specified in the requirments.txt
RUN pip3 install -r requirements.txt

# Copies all files from the same directory
COPY . .

# Runs the command line to start server at port 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
