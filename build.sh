#! /bin/sh

echo "Building..."
npm run build
cp -r ./build/* /var/www/acereact/
