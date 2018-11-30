import configparser
from ssh import SSH

#labelをいれたらアイテムを辞書型で返す
def configparse(label):
    config = configparser.ConfigParser()
    config.read('settings.ini')

    settings = dict(config.items(label))
    return settings