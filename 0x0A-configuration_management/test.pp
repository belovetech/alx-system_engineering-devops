package { 'nginx':
    ensure = > 'installed
}

exec { 'apt-get update':
    command => '/usr/bin/apt-get update'
}

package { 'python-software-properties'
    ensure => 'installed'
}

exec { 'add-repository' 
    command => '/usr/bin/add-apt-repository ppa:ondrej/php5 -y',
    require => Package['python-software-properties']
}

# Declare a string variable

$package = 'vim'
package { $package
    ensure => 'installed'
}

# Declare an array variable

$packages = ['vim', 'git', 'curl']
package { $packages
    ensure => 'installed'
}

# or

$packages.each |String $package| {
    package {
        ensure => 'installed'
    }
}
