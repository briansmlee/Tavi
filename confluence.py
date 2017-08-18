# posts pages to confluence server

import requests
import json
from settings import conf_addr

class Conf:
    """ Confluence class for using Server REST API """
    base_addr = conf_addr # base address for API calls
    username = ''
    password = ''
    
    auth = ('admin', 'admin')
    headers = ({'Content-Type' : 'application/json'})
    
    def printResponse(r):
	print '{} {}\n'.format(json.dumps(r.json(), sort_keys=True, \
            indent=4, separators=(',', ': ')), r)

    def form_pagedata(self):
        data = {}
        data['type'] = 'page',
        data['title'] = 'my test Page'
        data['space'] = {"key":'TST'}
        data['body'] = {
                'storage': {
                    'value': "<p>This is a new page</p>",
                    'representation': 'storage'
                    }
                }
        
        return page


    def create_page(self, dct):
        """
           creates page with content from input dictionary
        """
        r = requests.post(url)
    
    
    

    


