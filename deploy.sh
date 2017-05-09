#! /bin/bash

tar cfz --exclude='*.map' -C build . | ssh $DEPLOYMENT_USER@ace.rosshendry.com 'cat | tar xf -C /var/www/acemyorder'
