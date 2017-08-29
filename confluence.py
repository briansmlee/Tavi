# posts pages to confluence server

from trello import Trello
import requests
import json
import pprint
from settings import conf_home, conf_auth

class Confluence:
    """ Confluence class for using Server REST API """
    # CLASS VARS 
    auth = conf_auth 
    base_addr = conf_home # base address for API calls
    create_addr = base_addr + '/rest/api/content/' # addr for creating content
    headers = ({'Content-Type' : 'application/json'})
    # headers_admin = ('admin' , 'admin')
    
    def print_Response(self, resp):
        pass


    ##### This functionality has been moved to trello.py
    #
    # def form_pageData(self):
    #     """forms page data from input"""
    #     data = {}
    #     data['type'] = "page" # fix
    #     data['title'] = "API 테스트용 페이지" # Trello list name
    #     data['space'] = {"key":"AP"} # prompt usr to select
    #     data['body'] = {
    #             "storage": {
    #                 "value": "<p>This is a new page</p>", # format as html page
    #                 "representation": "storage"
    #                 }
    #             }
    #     
    #     print(data)
    #     return data
    #

    def get_page(self):
        """gets page"""
        # url = self.base_addr + '/rest/api/content'
        url = self.base_addr + '/rest/api/content/2228952?expand=body.storage'
        params_ = {
                'type' : 'page',
                'title': 'test: get conf page (check if html)',
                }
                
        resp = requests.get(url, params = params_, auth= self.auth)
        print(resp)
        print(resp.json())
        return resp.json()
        
        

    # def create_page(self):
    #     """
    #        creates page with content from input dictionary
    #     """
    #     
    #     pageData = self.form_pageData()
    #     r = requests.post(Conf.create_addr, data=json.dumps(pageData), 
    #             auth = Conf.auth_, headers = Conf.headers_)
    #     r.json()
    #     print(r)

    def create_page(self, page):
        """
        creates page with content from input dictionary
        """
        resp = requests.post(self.create_addr, data=json.dumps(page), 
                auth = self.auth, headers = self.headers)
        print(resp)
        resp = resp.json()
        print(resp)
        pprint(resp) #TEST
        
if __name__ == "__main__":
    t = Trello()
    conf = Confluence()
    page = conf.get_page() 
    print(page)
    # conf.create_page(t.mmain())
    # print("done")
       
