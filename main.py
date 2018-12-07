import configparser
from ssh import SSH
from do import DO
from sys import exit
import time
import wx

#labelをいれたらアイテムを辞書型で返す
def configparse(label):
    settings = configparser.ConfigParser()
    settings.read('settings.ini')

    settings = dict(settings.items(label))
    return settings

def setup_droplet():
    # Create a droplet
    do_key = configparse('DigitalOcean')['digitalocean_api_key']
    do = DO(do_key)
    #do.create_droplet()

    for droplet in do.get_all_droplets(tag_name="vpn-server"):
        ip = droplet.ip_address
    
    print("Waiting for setup of VPN")
    #sleep(35)

    # SSH接続
    path = configparse('SSH')['ssh_secretkey_path']
    
    print(path)
    ssh = SSH(ip,"root",path)
    ssh.connect

    ssh.excute_command("wget https://raw.githubusercontent.com/s151003/openvpn-install/master/openvpn-install.sh && chmod 777 openvpn-install.sh && bash openvpn-install.sh")
    ssh.close()


if __name__ == '__main__':
    setup_droplet()
