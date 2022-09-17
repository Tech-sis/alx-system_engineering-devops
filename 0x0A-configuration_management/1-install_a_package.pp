# Install a package using Puppet

exec { 'install flask':
	command => '/usr/bin/pip install flask',
	creates => '/usr/local/lib/python2.7/dist-packages/flask',
}
