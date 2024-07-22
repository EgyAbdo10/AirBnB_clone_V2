#!/usr/bin/env bash
# install nginx and make dirs
if ! dpkg -l | grep nginx; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

if test -f /data/web_static/current; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a\location /hbnb_static {\n   alias /data/web_static/current;\n}' /etc/nginx/sites-available/default
sudo service nginx restart

