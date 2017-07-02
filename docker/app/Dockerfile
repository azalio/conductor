FROM python:2
MAINTAINER Mikhail Petrov <azalio@azalio.net>

ENV REFRESHED_AT 2017-07-02
WORKDIR /usr/src/app
COPY ./requirements.txt ./
COPY ./commands ./commands/
COPY ./dc.py ./
COPY ./import.py ./
COPY ./micro.py ./
COPY ./app ./app/
COPY ./config ./config/
COPY ./library ./library/
RUN pip install --no-cache-dir -r requirements.txt
# RUN ./micro.py index

# CMD [ "python", "./micro.py", "run" ]
COPY ./docker/app/start.py ./
EXPOSE 5000
CMD while true; do sleep 30; done
