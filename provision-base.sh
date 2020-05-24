#!/bin/bash
# Script for creating a Kiwi TCMS VM for testing
#
# Some useful commands in Vagrant (run these from your own machine)
#
# # to start a new VM go into the directory with the Vagrantfile and type
# vagrant up
#
# # connect to a Linux vm using ssh
# vagrant ssh
#
# # Run the provisioning script on a running vm
# vagrant provision
#
# # remove VM created by Vagrant
# vagrant destroy -f
#

export HOME=/home/vagrant

echo "Provision VM"
dnf -y install git vim docker docker-compose firefox
service docker start
docker pull kiwitcms/kiwi

# Follow along the lines of these steps from the Docs
# https://kiwitcms.readthedocs.io/en/latest/installing_docker.html
cd $HOME
git clone https://github.com/kiwitcms/Kiwi.git
cd Kiwi
docker-compose up -d
wget --no-check-certificate https://localhost/static/ca.crt

# Initial configuration of running container
# Run below commands by hand
# docker exec -it kiwi_web /Kiwi/manage.py migrate
# docker exec -it kiwi_web /Kiwi/manage.py createsuperuser
# docker exec -it kiwi_web /Kiwi/manage.py set_domain public.tenant.kiwitcms.org

# SSL configuration
# TODO deploy certificate to firefox (/usr/lib64/mozilla/certificates/ ?)

# TODO add hashkey to the hosts file (/etc/hosts)
#sed -i "2i192.241.xx.xx  venus.example.com venus" /etc/hosts

# Optional: Enable plain text HTTP access
#
# environment:
#    KIWI_DONT_ENFORCE_HTTPS: "true"
#
