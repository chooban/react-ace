FROM mhart/alpine-node:5.11.1
MAINTAINER Ross Hendry "rhendry@googlemail.com"

ADD . /build
WORKDIR /build

RUN npm install --progress=false && \
  npm run build && \
  npm cache clean  && \
  mkdir -p /var/www/acereact/public_html && \
  cp -r ./build/* /var/www/acereact/public_html/ && \
  rm -rf /build

VOLUME /var/www/acereact/public_html/

CMD ["true"]
