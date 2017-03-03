FROM mhart/alpine-node:6.9.2
MAINTAINER Ross Hendry "rhendry@googlemail.com"

RUN apk add gosu --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN mkdir -p /usr/src/app
RUN mkdir -p /var/www/acereact/
VOLUME /var/www/acereact/

WORKDIR /usr/src/app
ADD package.json ./package.json
RUN npm install --progress=false && npm cache clean

ADD . ./

CMD ["sh", "entrypoint.sh", "./build.sh"]
