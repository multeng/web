rm /etc/nginx/sites-enabled/default
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo apt update
sudo pip install gunicorn
sudo install django==1.6.1
/etc/init.d/nginx restart
