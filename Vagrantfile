# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.box = "data-science-toolbox/dst"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8888" will access port 8888 on the guest machine.
  config.vm.network "forwarded_port", guest: 8888, host: 8888

  # VirtualBox-specific configuration
  # https://www.vagrantup.com/docs/virtualbox/configuration.html
  config.vm.provider "virtualbox" do |vb|
    # generate box image once, link subsequent creations
    vb.linked_clone = true
    # hide the VirtualBox GUI when booting the machine
    vb.gui = false
    # customize the amount of memory on the VM
    vb.memory = "1024"
  end

  # share this folder with the vm
  config.vm.synced_folder ".", "/home/vagrant/notebooks/lots-analysis"
end
