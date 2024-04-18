# Fixing the number of files that worker can open at a time
exec { 'fix-worker_rlimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}