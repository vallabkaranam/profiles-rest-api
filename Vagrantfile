Vagrant.configure("2") do |config|
  config.vm.define "docker_vm" do |vm|
    vm.vm.provider "docker" do |d|
      d.image = "ubuntu-18.04-sshd"
      d.has_ssh = true
      d.cmd = ["/usr/sbin/sshd", "-D"]
    end

    vm.vm.network "forwarded_port", guest: 8000, host: 8000

    # Disable synced folder for now if not needed
    # vm.vm.synced_folder ".", "/vagrant", type: "rsync"

    vm.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3-venv zip

      touch /home/vagrant/.bash_aliases
      if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
        echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
        echo "alias python='python3'" >> /home/vagrant/.bash_aliases
      fi
    SHELL
  end
end