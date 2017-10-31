FROM azelf/base
MAINTAINER johnsuh94@gmail.com

ENV LANG C.UTF-8

COPY . /srv/app

RUN /root/.pyenv/versions/app/bin/pip install -r\
    /srv/app/requirements.txt

WORKDIR /srv/app
RUN pyenv local app
