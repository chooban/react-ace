FROM mhart/alpine-node:4.4.4
MAINTAINER Ross Hendry "rhendry@googlemail.com"

RUN mkdir -p /var/www/acereact/public_html
RUN mkdir -p /build
ADD . /build
WORKDIR /build

RUN npm install; npm run build
COPY ./build/* /var/www/acereact/public_html/

RUN rm -rf /build
CMD ["true"]
