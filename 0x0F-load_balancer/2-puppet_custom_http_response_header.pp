# Install Nginx with HTTP header

exec { 'update':
  provider => shell,
  command  => 'apt-get -y update',
  before   => Exec['instal nginx']
}


exec { 'install Nginx':,
  provide => shell,
  command => 'apt-get -y install nginx',
  before  =>   Exec['add-header']
}

exec { 'add-header':
  provide     => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx']
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
