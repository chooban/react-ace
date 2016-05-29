FROM mhart/alpine-node:6.1.0
MAINTAINER Ross Hendry "rhendry@googlemail.com"

ADD package.json /build/package.json
WORKDIR /build
RUN npm install --progress=false && npm cache clean

ADD . /build
RUN npm run build && \
  mkdir -p /var/www/acereact/public_html && \
  cp -r ./build/* /var/www/acereact/public_html/ && \
  rm -rf /build

VOLUME /var/www/acereact/public_html/

CMD ["true"]
