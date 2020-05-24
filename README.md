# Test-Development Environment in Vagrant - Example for Youtube clip
A Vagrant based virtual environment for testing the out of the box expericence of Kiwi TCMS. 

# Instructions for getting started with Vagrant
## Prerequisites (Linux)
- Oracle VirtualBox https://www.virtualbox.org/
- Vagrant https://www.vagrantup.com/downloads.html
- Note: in the youtube video I used Libvirt as a virtualization provider if you want to provision without Oracle VirtualBox you can also do so you but you need Libvirtd, QEMU-KVM and Vagrant Libvirt plugin!

## Start the Vagrant Virtual Machine
- Clone this repo
- Go into the local repository from the step above
- run `vagrant up`
- Now wait for the process to complete

## Open the Virtual machine (Ubuntu)
- The default username and password is **vagrant**

## What's provided?
- The provisioning script (.sh)

## Extra step (export)
To export the VM to a portable OVA file, follow these steps:
- Stop the VM
- Select the VM in the list
- From the VirtualBox manager menu choose 'Machine --> Export to OCI' (rightclick on the machine in the list will also bring up this menu).
