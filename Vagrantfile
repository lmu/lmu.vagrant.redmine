# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "canonical/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.define "SCM", primary: true do |scm|
    scm.vm.provider "virtualbox" do |vb|
      vb.name = "SCM-APP1"
      vb.memory = 4096
      vb.cpus = 4
    end
    scm.vm.network :private_network, ip: "192.168.1.80"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.limit = "all"
    ansible.playbook = "lmu.ansible.playbooks/base-preseed.yml"
  end

end
