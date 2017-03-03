FROM mhart/alpine-node:6.9.2
MAINTAINER Ross Hendry "rhendry@googlemail.com"

RUN mkdir -p /usr/src/app
RUN mkdir -p /var/www/acereact/
VOLUME /var/www/acereact/

WORKDIR /usr/src/app
ADD package.json ./package.json
RUN npm install --progress=false && npm cache clean

ADD . ./

CMD ["sh", "build.sh"]
