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
  config.vm.box = "canonical/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.define "redmine2.verwaltung.uni-muenchen.de", primary: true do |scm|
    scm.vm.provider "virtualbox" do |vb|
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

    scm.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".80"
    if USE_PUBLIC_NETWORK
      scm.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".80"
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.limit = "all"
#    ansible.playbook = "lmu.ansible.playbooks/base-preseed.yml"
    ansible.playbook = "lmu.ansible.playbooks/redmine.yml"
    ansible.groups = {
      "redmine" => ["redmine2.verwaltung.uni-muenchen.de"]
    }
    #ansible.start_at_task = "Create User"
    ansible.verbose = ""
  end

end
