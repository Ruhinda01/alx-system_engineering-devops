# Automate the task of creating a custom HTTP header response

exec { 'updating_system':
   command  => '/usr/bin/apt-get update',
}

package { 'nginx':
   ensure   => 'installed',
   require  => Exec['updating_system'],
}

file_line { 'nginx_redirect':
   ensure   => 'present',
   path     => '/etc/nginx/sites-available/default',
   after    => 'listen 80 default_server;',
   line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
   content  => 'Hello World',
}

exec { 'HTTP_header':
   command  => 'sudo sed -i "/server_name _;/ a\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
   provider => shell,
}

service { 'nginx':
   ensure   => 'running',
   require  => Package['nginx'],
}
