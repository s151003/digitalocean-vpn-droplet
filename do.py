import digitalocean as docean

class DO():
    def __init__(self,token):
        self.token = token
        self.manager = docean.Manager(token=self.token)

    def create_droplet(self):
        keys = self.manager.get_all_sshkeys()
        droplet = docean.Droplet(token=self.token,
                                name='DropletWithSSHKeys',
                                region='ams3',
                                image='ubuntu-18-04-x64',
                                size_slug='512mb',
                                ssh_keys=keys,
                                tags=["vpn-server"],
                                backups=False)
        droplet.create()

    def get_all_droplets(self,tag_name):
        return self.manager.get_all_droplets(tag_name=tag_name)