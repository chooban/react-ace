FROM mhart/alpine-node:6.1.0
MAINTAINER Ross Hendry "rhendry@googlemail.com"

ADD . /build
WORKDIR /build

RUN npm install && \
  npm run build && \
  npm cache clean  && \
  mkdir -p /var/www/acereact/public_html && \
  cp -r ./build/* /var/www/acereact/public_html/ && \
  rm -rf /build

CMD ["true"]
