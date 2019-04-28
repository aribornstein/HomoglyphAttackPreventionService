FROM python:3.6-alpine

ENV KEY="Azure Computer Vision Key"
ENV REGION="Azure Computer Vision Region"

RUN echo "http://uk.alpinelinux.org/alpine/latest-stable/main" > /etc/apk/repositories &&\
    echo "http://uk.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories &&\
    apk --no-cache --update-cache add gfortran build-base wget freetype-dev libpng-dev openblas-dev &&\
    ln -s /usr/include/locale.h /usr/include/xlocale.h &&\
    pip install Flask requests matplotlib &&\
    mkdir /app

COPY ./server.py /app/server.py
CMD python /app/server.py -k $KEY -r $REGION