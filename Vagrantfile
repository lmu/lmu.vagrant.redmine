# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "canonical/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  config.vm.define "scm", primary: true do |scm|
    #scm.vm.box = "SCM-APP1"
    scm.vm.box = "canonical/trusty64"
    scm.vm.provider "virtualbox" do |vb|
      vb.name = "SCM-APP1"
      vb.memory = 4096
      vb.cpus = 4
      #vb.customize ["modifyvm", :id, "--memory", "1024"]
      #vb.customize ["modifyvm", :id, "--name", "SCM-APP1" ]
      #vb.synced_folder "./shared_folders/server.scm/data", "/data", owner: "root", group: "root"
    end
    
    # Network Settings
    scm.vm.network "forwarded_port", guest: 80, host: 20080, auto_correct: true
    scm.vm.network "forwarded_port", guest: 443, host: 20443, auto_correct: true
    scm.vm.network "forwarded_port", guest: 9001, host: 9001, auto_correct: true
    scm.vm.network "forwarded_port", guest: 10000, host: 10001, auto_correct: true

    scm.vm.network "private_network", ip: "192.168.1.10"

  end

  config.vm.define "db" do |db|
    #db.vm.box = "SCM-DB1"
    db.vm.box = "canonical/trusty64"
    db.vm.provider "virtualbox" do |vb|
      vb.name = "SCM-DB1"
      vb.memory = 8192
      vb.cpus = 4
      #vb.customize ["modifyvm", :id, "--memory", "1024"]
      #vb.customize ["modifyvm", :id, "--name", "SCM-DB1" ]
      #vb.synced_folder "./shared_folders/server.db/data", "/data", owner: "root", group: "root"
    end

    # Network Settings
    db.vm.network "forwarded_port", guest: 10000, host: 10002, auto_correct: true

    db.vm.network "private_network", ip: "192.168.1.5"
  end




  config.vm.provision "ansible" do |ansible|
    # Ansible Inventory File 
    ansible.groups = {
      "dbs" => ["db"],
      "apps" => ["scm"],
      "all_groups:children" => ["dbs", "apps"]
    }

    # Ansible Playbook
    ansible.playbook = "playbooks/playbook.yml"
  end

  # Trigger on Startup
  config.trigger.after [:provision, :up, :reload] do
    system('echo "
rdr pass on lo0 inet proto tcp from any to 127.0.0.1 port 80 -> 127.0.0.1 port 20080  
rdr pass on lo0 inet proto tcp from any to 127.0.0.1 port 443 -> 127.0.0.1 port 20443  
" | sudo pfctl -f - > /dev/null 2>&1; echo "==> Fowarding Ports: 80 -> 20080, 443 -> 20443"')  
  end

  # Trigger on halt / destroy
  config.trigger.after [:halt, :destroy] do
    system("sudo pfctl -f /etc/pf.conf > /dev/null 2>&1; echo '==> Removing Port Forwarding'")
  end

end
