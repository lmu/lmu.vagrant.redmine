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

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"
  #config.vm.box = "ubuntu/xenial64"
  #config.vm.box = "centos/7"

  config.ssh.forward_agent = true
  #config.ssh.private_key_path = "~/.ssh/id_rsa"

  # Disable SharedFolder by default.
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.define "redmine2.verwaltung.uni-muenchen.de", primary: false, autostart: AUTOSTART_SECONDARY do |node|
    node.vm.box = "ubuntu/trusty64"

    node.vm.provider "virtualbox" do |vb|
      vb.name = "Redmine2"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".82"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".82"
    end
  end

  config.vm.define "redminetest2.verwaltung.uni-muenchen.de", autostart: AUTOSTART_SECONDARY do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.provider "virtualbox" do |vb|
      vb.name = "RedmineTest2"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".87"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".87"
    end
  end

  config.vm.define "redmine3.verwaltung.uni-muenchen.de", primary: true, autostart: true do |node|
    node.vm.box = "centos/7"
    node.vm.provider "virtualbox" do |vb|
      vb.name = "Redmine3"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".83"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".83"
    end
  end
  config.vm.define "redminetest3.verwaltung.uni-muenchen.de", autostart: AUTOSTART_SECONDARY do |node|
    node.vm.box = "centos/7"
    node.vm.provider "virtualbox" do |vb|
      vb.name = "RedmineTest3"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".88"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".88"
    end
  end

  config.vm.define "redmine4.verwaltung.uni-muenchen.de", primary: false, autostart: AUTOSTART_SECONDARY do |node|
    node.vm.box = "ubuntu/xenial64"
    node.vm.provider "virtualbox" do |vb|
      vb.name = "Redmine4"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end
    config.vm.provision "bootstrap", type: "shell" do |s|
      s.inline = "echo Bootstrap Machine; apt install -y python aptitude"
    end
    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".84"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".84"
    end
  end

  config.vm.define "redminetest4.verwaltung.uni-muenchen.de", autostart: AUTOSTART_SECONDARY do |node|
    node.vm.box = "ubuntu/xenial64"
    node.vm.provider "virtualbox" do |vb|
      vb.name = "RedmineTest4"
      vb.memory = 8192
      vb.cpus = 8
      vb.customize ["modifyvm", :id,
                    "--cpuexecutioncap", "50",
                    "--groups", "/Vagrant/LMU/Redmine"
                   ]
    end

    config.vm.provision "bootstrap", type: "shell" do |s|
      s.inline = "echo Bootstrap Machine; apt install -y python aptitude"
    end

    node.vm.network :private_network, ip: PRIVATE_NETWORK_BASE + ".89"
    if USE_PUBLIC_NETWORK
      node.vm.network :public_network, ip: PUBLIC_NETWORK_BASE + ".89"
    end
  end
  config.vm.provision "bootstrap", type: "shell" do |s|
    s.inline = "echo Bootstrap Machine"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "lmu.ansible.playbooks/base-preseed.yml"
    #ansible.verbose = "vvv"
  end
#  config.vm.provision "ansible" do |ansible|
#    ansible.playbook = "lmu.ansible.playbooks/redmine.yml"
#    ansible.groups = {
#      "redmine-dbs-production" => ["redmine2.verwaltung.uni-muenchen.de"],
#      "redmine-dbs-staging" => ["redminetest2.verwaltung.uni-muenchen.de",
#                                "redminetest3.verwaltung.uni-muenchen.de",
#                                "redminetest4.verwaltung.uni-muenchen.de"],
#      "redmine-dbs:children" => ["redmine-dbs-production",
#                                 "redmine-dbs-staging"],
#      "redmine-workers-production" => ["redmine2.verwaltung.uni-muenchen.de"],
#      "redmine-workers-staging" => ["redminetest2.verwaltung.uni-muenchen.de",
#                                    "redminetest3.verwaltung.uni-muenchen.de",
#                                    "redminetest4.verwaltung.uni-muenchen.de"],
#      "redmine-workers:children" => ["redmine-workers-production",
#                                     "redmine-workers-staging"],
#      "redmine-frontends-production" => ["redmine2.verwaltung.uni-muenchen.de"],
#      "redmine-frontends-staging" => ["redminetest2.verwaltung.uni-muenchen.de",
#                                      "redminetest3.verwaltung.uni-muenchen.de",
#                                      "redminetest4.verwaltung.uni-muenchen.de"],
#      "redmine-frontends:children" => ["redmine-frontends-production",
#                                       "redmine-frontends-staging"],
#    }
#    #ansible.verbose = "vvvv"
#    #ansible.verbose = "vvv"
#    #ansible.verbose = "vv"
#    #ansible.verbose = "v"
#    #ansible.verbose = ""
#    #ansible.start_at_task = "Start Setup Instance"
#    #ansible.start_at_task = "Setup Redmine Multi-Instance"
#    #ansible.start_at_task = "Finish Setup"
#    #ansible.limit = "all"
#    #ansible.limit = "lmu.ansible.playbooks/redmine.retry"
#    #ansible.tags = ["setup", "configuration", "update"]
#    #ansible.skip_tags = ["update"]
#    ansible.extra_vars = {
#      #ansible_ssh_user: 'ubuntu',
#      ansible_ssh_user: 'ansible',
#      ansible_connection: 'ssh',
#      ansible_ssh_args: '-o ForwardAgent=yes',
#      ansible_ssh_private_key_file: ['~/.ssh/id_rsa']
#    }
#  end

end
