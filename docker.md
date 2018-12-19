# How to install Docker engine on new VM

# Install Docker binary
sudo tar zxvf docker-18.06.1-ce.tgz; sudo cp docker/* /usr/bin

# Add docker group & add $USER to it
sudo groupadd docker ; sudo usermod -aG docker op_ap ; mkdir /etc/docker
vim /etc/docker/daemon.json

# Manually enable systemctl docker service
# Add two files into /etc/systemd/system/docker.service & /etc/systemd/system/docker.socket
vim /etc/systemd/system/docker.service
vim /etc/systemd/system/docker.socket
sudo systemctl daemon-reload

# Start service by systemctl
systemctl start docker

# Check docker service status
systemctl status docker

# Change docker.sock group to docker
chgrp docker /var/run/docker.sock
chgrp docker /etc/docker/*
chmod 664 /etc/docker/*

# Check docker installation. Try to pull image
docker login dockeruncer.tsmc.com.tw
docker pull dockeruncer.tsmc.com.tw/base/coreos/etcd:v3.2




### daemon.json
{
    "graph": "/userap/docker-data",
    "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:2375"],
    "insecure-registries": ["dockeruncer.tsmc.com.tw"]
}


### docker.socket
[Unit]
Description=Docker Socket for the API
PartOf=docker.service

[Socket]
ListenStream=/var/run/docker.sock
SocketMode=0660
SocketUser=root
SocketGroup=docker

[Install]
WantedBy=sockets.target



### docker.service
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target docker.socket firewalld.service
Wants=network-online.target
Requires=docker.socket

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=1048576
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
