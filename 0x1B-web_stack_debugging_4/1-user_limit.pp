# Enables login with the holberton user and open a file
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}