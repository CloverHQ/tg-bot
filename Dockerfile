FROM python:alpine3.16
COPY . /var/app
WORKDIR /var/app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]

