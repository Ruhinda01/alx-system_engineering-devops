# Automating the fixing of the 500 error
exec { 'fix-settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
