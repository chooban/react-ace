#! /bin/sh

npm run build
cp -r ./build/* /var/www/acereact/
