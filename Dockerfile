FROM suhjohn/base
MAINTAINER johnsuh94@gmail.com

# pip
ENV LANG C.UTF-8
ENV DJANGO_SETTINGS_MODULE config.settings.dev

COPY . /srv/app
RUN /root/.pyenv/versions/app/bin/pip install -r\
    /srv/app/requirements.txt

# pyenv local 설정
WORKDIR /srv/app
RUN pyenv local app

# Nginx
RUN cp /srv/app/.config/dev/nginx/nginx.conf \
        /etc/nginx/nginx.conf
RUN cp /srv/app/.config/dev/nginx/app.conf \
        /etc/nginx/sites-available/
RUN rm -rf /etc/nginx/sites-enabled/*
RUN ln -sf /etc/nginx/sites-available/app.conf \
            /etc/nginx/sites-enabled/app.conf

# uWSGI
RUN mkdir -p /var/log/uwsgi/app

# pyenv local 설정
WORKDIR /srv/app/instagram
RUN /root/.pyenv/versions/app/bin/python manage.py collectstatic --noinput
RUN /root/.pyenv/versions/app/bin/python manage.py migrate --noinput

# supervisor
RUN cp /srv/app/.config/dev/supervisor/* \
    /etc/supervisor/conf.d/
CMD supervisord -n

EXPOSE 80