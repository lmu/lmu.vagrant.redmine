# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# Special Settings for this Vagrant Environment
USE_PUBLIC_NETWORK = false
#USE_PUBLIC_NETWORK = true
PRIVATE_NETWORK_BASE = "192.168.1"
#PRIVATE_NETWORK_BASE = PRIVATE_NETWORK_BASE + ""
PUBLIC_NETWORK_BASE = "137.193.211"
#PUBLIC_NETWORK_BASE = "192.168.2"
AUTOSTART_SECONDARY = false
#AUTOSTART_SECONDARY = true
AUTOSTART_INFRASTRUKTURE = false
#AUTOSTART_INFRASTRUKTURE = true

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  #config.vm.box = "ubuntu/trusty64"
  config.vm.box = "ubuntu/xenial64"
  #Default hashicorp box
  #config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.define "redmine2.verwaltung.uni-muenchen.de", primary: true do |node|
    node.vm.provider "virtualbox" do |vb|
      vb.name = "Redmine2"
      vb.memory = 8192
      #vb.memory = 4096
      vb.cpus = 8
      #vb.cpus = 4
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end

    node.vm.network "forwarded_port", guest: 3000, host: 3000
    node.vm.network "forwarded_port", guest: 3001, host: 3001
    #node.vm.network "forwarded_port", guest: 5000, host: 5000
    node.vm.network "forwarded_port", guest: 9001, host: 9001
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".80"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".80"
    end
  end

  if ENV['OS'] != "Windows_NT"
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "lmu.ansible.playbooks/redmine.yml"
      ansible.groups = {
        "redmine" => ["redmine2.verwaltung.uni-muenchen.de"]
      }
      #ansible.verbose = "vvvv"
      #ansible.verbose = "vvv"
      #ansible.verbose = "vv"
      ansible.verbose = "v"
      #ansible.verbose = ""
      #ansible.start_at_task = "Start Setup Instance"
      #ansible.start_at_task = "Setup Redmine Multi-Instance"
      #ansible.limit = "all"
      #ansible.limit = "lmu.ansible.playbooks/redmine.retry"
      #ansible.tags = ["setup", "configuration", "update"]
      #ansible.skip_tags = ["update"]
      #ansible.ask_vault_pass = true
    end
  end
end
