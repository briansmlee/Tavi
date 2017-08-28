# posts pages to confluence server

import requests
import json
import pprint
from settings import conf_home, auth

class Conf:
    """ Confluence class for using Server REST API """
    base_addr = conf_home # base address for API calls
    create_addr = base_addr + '/rest/api/content/' # addr for creating content
    
    auth_ = auth
    headers_ = ({'Content-Type' : 'application/json'})
    # headers_admin = ('admin' , 'admin')
    
    def printResponse(self, r):
        pass


    def form_pageData(self):
        """forms page data from input"""
        data = {}
        data['type'] = "page" # fix
        data['title'] = "API 테스트용 페이지" # Trello list name
        data['space'] = {"key":"AP"} # prompt usr to select
        data['body'] = {
                "storage": {
                    "value": "<p>This is a new page</p>", # format as html page
                    "representation": "storage"
                    }
                }
        
        print(data)
        return data
    
    def get_page(self):
        """gets page"""
        url = Conf.base_addr + '/rest/api/content'
        params_ = {
                'type' : 'page',
                # 'spacekey'
                'title': 'Retrospective',
                }
                
        r = requests.get(url,
	    params = params_,
	    auth= Conf.auth_
            )
        print(r.json())
        
        


    def create_page(self):
        """
           creates page with content from input dictionary
        """
        pageData = self.form_pageData()
        r = requests.post(Conf.create_addr, data=json.dumps(pageData), 
                auth = Conf.auth_, headers = Conf.headers_)
        r.json()
        print(r)

if __name__ == "__main__":
    conf = Conf()
    conf.create_page()
    print("done")
        
        


