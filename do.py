import digitalocean as docean

class DO():
    def __init__(self,token):
        self.token = token
        self.manager = docean.Manager(token=self.token)

    def get_keys(self):
        return self.manager.get_all_sshkeys()

    def create_droplet(self):
        keys = self.get_keys()
        droplet = docean.Droplet(token=self.token,
                                name='droplet1',
                                region='ams3',
                                image='ubuntu-18-04-x64',
                                size_slug='512mb',
                                ssh_key=keys,
                                tags=["vpn-server"],
                                backups=False)
        droplet.create()

    def get_all_droplets(self,tag_name):
        return self.manager.get_all_droplets(tag_name=tag_name)