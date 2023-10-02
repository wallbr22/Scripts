#!/usr/bin/env python3

import os

# Install NFS server package
os.system('sudo dnf install nfs-utils -y')

# Create a directory to share
os.system('sudo mkdir /nfs_share')

# Set permissions for the directory
os.system('sudo chmod -R 777 /nfs_share')

# Configure NFS server
with open('/etc/exports', 'w') as f:
    f.write('/nfs_share *(rw,sync,no_root_squash,no_all_squash)')

# Start NFS server
os.system('sudo systemctl start nfs-server')

# Enable NFS server to start on boot
os.system('sudo systemctl enable nfs-server')