# A manifest that kills a process

exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell,
  returns  => [0, 1]
}
