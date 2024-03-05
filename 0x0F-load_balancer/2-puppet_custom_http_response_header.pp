# Automate the task of creating a custom HTTP header response

exec {'configure_nginx':
  command  => @(EOT),
     sudo apt-get -y update
     sudo apt-get -y install nginx
     sudo sed -i '/server_name _;/ a\\tadd_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default
     sudo service nginx restart
EOT
  provider => shell,
}
