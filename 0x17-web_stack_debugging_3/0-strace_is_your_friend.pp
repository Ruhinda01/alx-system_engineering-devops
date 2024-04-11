# Automating the fixing of the 500 error

exec { 'replace_phpp_in_settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
