FROM python:3.12-alpine
RUN apk update
RUN apk add sqlite
WORKDIR /home
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .
#ENTRYPOINT /usr/local/bin/python /home/ejemplo_args.py 1 2 arg3
