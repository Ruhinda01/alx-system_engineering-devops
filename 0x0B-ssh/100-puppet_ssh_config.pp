# Puppet changes our configuration file

file { '/etc/ssh/ssh_config':
  ensure => present,
  content => "# Using Puppet
Include /etc/ssh/ssh_config.d/*.conf

Host *
   PasswordAuthentication no
   IdentityFile ~/.ssh/school",
}
