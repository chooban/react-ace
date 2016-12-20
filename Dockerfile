FROM mhart/alpine-node:6.9.2
MAINTAINER Ross Hendry "rhendry@googlemail.com"

RUN mkdir -p /usr/src/app
RUN mkdir -p /var/www/acereact/public_html

WORKDIR /usr/src/app
ADD package.json ./package.json
RUN npm install --progress=false && npm cache clean

ADD . ./
RUN npm run build && \
  cp -r ./build/* /var/www/acereact/public_html/

VOLUME /var/www/acereact/public_html/

CMD ["true"]
