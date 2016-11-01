FROM mhart/alpine-node:6.1.0
MAINTAINER Ross Hendry "rhendry@googlemail.com"

RUN addgroup -S app && adduser -S -g app app
ENV HOME=/home/app
RUN mkdir -p /var/www/acereact/public_html && \
  chgrp app /var/www/acereact/public_html

ADD package.json $HOME/build/package.json
RUN chown -R app:app $HOME/*
WORKDIR $HOME/build
USER app
RUN npm install --progress=false && npm cache clean

ADD . $HOME/build
RUN npm run build && \
  cp -r $HOME/build/* /var/www/acereact/public_html/

VOLUME /var/www/acereact/public_html/

CMD ["true"]
