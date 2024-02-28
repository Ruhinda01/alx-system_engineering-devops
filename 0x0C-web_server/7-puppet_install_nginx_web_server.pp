# Install Nginx web server (w/ Puppet)

exec { 'updating system':
   command => '/usr/bin/apt-get update',
}

package { 'nginx':
   ensure  => 'installed',
   require => Exec['updating system']
}

file_line { 'nginx redirect':
   ensure  => 'present',
   path    => '/etc/nginx/sites-available/default',
   after   => 'listen 80 default_server;',
   line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
   content => 'Hello World!',
}

service { 'nginx':
   ensure  => 'running',
   require => Package['nginx'],
}
