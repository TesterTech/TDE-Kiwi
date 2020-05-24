# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "mrlesmithjr/fedora30-desktop"
  #config.vm.network "forwarded_port", guest: 8000, host: 8000
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  #config.vm.network "private_network", type: "dhcp"
  # config.vm.network "public_network"
  # config.vm.synced_folder ".", "/vagrant", nfs: true
  # config.vm.synced_folder "Kiwi/", "/vagrant/Kiwi"

  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true
    # Customize the amount of memory on the VM:
    vb.memory = "1024" 
  end
end
Vagrant.configure("2") do |config|
    config.vm.provision "shell", path: "provision-base.sh" # do not remove base!
end

