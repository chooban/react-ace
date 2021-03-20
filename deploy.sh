#! /bin/bash

tar cfz -C build/ . | ssh $DEPLOYMENT_USER@ace.rosshendry.com 'cat | tar xf -C /var/www/acemyorder'
