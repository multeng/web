rm /etc/nginx/sites-enabled/default
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
