import ConfigParser
from crypto import decrypt

class Secrets(object):
    def __init__(self):
    	self.config = ConfigParser.ConfigParser()
    	self.config.read('secrets.cfg')

    def get(self, secret):
        return decrypt(self.config.get('secrets', secret))