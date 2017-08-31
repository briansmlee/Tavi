# Class to model Trello objects

import requests           # a 3rd party library. `pip install requests`
import json               # all responses from Trello come back as JSON
import markdown as md
from db import add_card, print_instances
from pprint import pprint # this is a handy utility for printing dictionaries in a human readable way
from settings import trello_key, trello_token

class Trello:
    # TODO: need to use OAuth to hide key and token
    # currently gets key and token from the settings file.
    # if not key or token:
    #  from settings import trello_key, trello_token
    #  key = trello_key
    #  token = trello_token
    key = trello_key
    token = trello_token
    params = { 
            'key' : key,
            'token' : token
            }
    # Since we only want the name of the board, let's supply the 'fields' argument as well. 
    # We're also going to ask for lists, to be used later.
    arguments = {'fields': 'name', 'lists': 'open'}
    
    base = 'https://trello.com/1/' # The base url for all reqs
    
    # below are unused for now
    # urls = {
    #         'get_boards' : base
    #         'get_lists_of_board' : base + '/boards/[board_id]/lists'
    #         'get_cards_of_list' : base + '/lists/[list_id]/cards' 
    #         }

    def get_a_on_b(self, a, b, b_id):
        """
        ref: https://trello.readme.io/docs/api-introduction
        generalized method to get all As on a specific B. 
        for example, get cards on a board with board_id
        """
        # do error checking prior to forming url
        
        url = self.base + b + '/' + b_id + '/' + a
        resp = requests.get(url, params=self.params, data=self.arguments)
        return resp.json()
       
    def make_page(self, list_id):
        """main functionality on Trello side.
        prompts user to choose a list,
        gets all cards on list,
        and returns formed pageData from cards
        """
        # list_id input is brought from js
        # list_id, list_name = self.prompt_list()
        
        cards = self.get_a_on_b(a='cards', b='lists', b_id=list_id)
        # pprint(cards) #TEST

        # need a way to find list_name.

        page = self.list_to_page(cards, list_name) 
        # pprint(page) #TEST
        
        return page

    def prompt_list(self):
        """
        prompts user to choose a list 
        returns list name and id
        """ 
        # hard-coded for now.
        list_id = '598bf789aa7a8937cfde79b8'
        list_name = '테스트용 트렐로 리스트'
        return list_id, list_name

    def list_to_page(self, cards, list_name):
        """forms page dict from cards"""
        page = {}
        page['type']  = 'page'
        page['title'] = list_name
        page['space'] = {'key' : 'AP'} # prompt usr to select space
        page['body']  = {
                "storage" : {
                    "value" : "",
                    "representation" : "storage"
                    }
                }

        ##### now using markdown...
        # add card content for all cards
        # for idx, card in enumerate(cards, start=1):
        #     header = '<h' + str(idx) + '>' + card['name'] + '</h' + str(idx) + '>\n'
        #     body = '<p>' + card['desc'] + '</p>\n\n'
        #     content = header + body 
        #     page['body']['storage']['value'] += content
        
        # text = ''
        # for card in cards:
        #     # add attachments and comments here.
        #     name = card['name']
        #     desc = card['desc']
        #     
        #     

        #     for 
        #     card_text = card['name'] + '\n\n' + card['desc'] + '\n\n'
        #     print(card_text) 
        #     card_text1 = md.markdown(card['name']) + md.markdown(card['desc'])
        #     print(card_text1)
        #     text += card_text

        page['body']['storage']['value'] = self.build_page_body(cards)
        return page
    
    def build_page_body(self, cards, headers=True):
        """builds html body from cards data""" 
        # h = HTML()
        body = ''
        if headers:
            # add table of contents
            body += '<h4>목차</h4>'
            table_of_contents = '<p><ac:structured-macro \
            ac:name="toc" ac:schema-version="1" /></p>'
            # ac:macro-id="09b161a6-bce0-4449-8e49-7dcabd03c68b"\
            body += table_of_contents

        for idx, card in enumerate(cards, start=1):
            # if table of contents is on, add headers
            if headers:
                header = '<h4>(' + str(idx) + ')</h4>' # h3 for now
                body += header
            
            # name doesn't have newline
            # body += h.p(card['name'])
            p = '<p>' + card['name'] + '</p>'
            body += p
            
            # linebreak card description
            # handle lists(lu) here
            for line in card['desc'].split('\n'):
                if line: # check if empty
                   body += ('<p>' + line + '</p>')

        print(body)           
        return body
            
    ##### FIVE METHODS BELOW ARE NO LONGER USED
    ##### see get_a_on_b
    #####
    # def cards_in_list(self, ):
    #     """ get all cards from list """
    #     list_id = get_list_id()
    #     resp = requests.get(
    #     
    #     # get target list id
    #     # form url
    #     # send req, get resp
    #     # test for card names
    #
    # def get_list_id(self):
    #     """ 
    #     gets id of the target list.
    #     currently takes first list in board.
    #     """
    #     board_id = get_board_id()
    #     lists = get_all_lists(board_id)
    #     firstList = lists[0]
    #     list_id = firstList['id']
    #     return list_id 
    #
    # def get_all_lists(self, board_id):
    #     """
    #     gets all lists
    #     """
    #     # GET /1/boards/[board_id]/lists - Get an array of Lists on a board
    #     lists_ur 
    #     resp = requests.get(lists_url, params=self.params_key_and_token, data=arguments)
    #     return resp.json()
    # 
    # def get_board_id(self):
    #     """
    #     gets board id
    #     currently takes first board
    #     """
    #     boards = self.get_all_boards()
    #     firstBoard = boards[0]
    #     board_id = firstBoard['id']
    #     return board_id
    # 
    # def get_all_boards(self):
    #     """
    #     gets list of all boards
    #     """
    #     boards_url = self.base + 'members/me/boards'
    #     resp = requests.get(boards_url, params=self.params_key_and_token, data=arguments)
    #     return resp.json()
    #     
    
    def get_cards(self):

        params_key_and_token = {'key': self.key, 'token': self.token} # store API key and token as parameters
        boards_url = self.base + 'members/me/boards'

        # Since we only want the name of the board, let's supply the 'fields' argument as well. 
        # We're also going to ask for lists, to be used later.
        arguments = {'fields': 'name', 'lists': 'open'}

        # The requests library has separate methods for get, put, post, and delete. We need a GET here.
        # We need to provide the URL we want to access, the key and token (params_key_and_token) as params, as well as
        # any arguments (arguments) as data.
        response = requests.get(boards_url, params=params_key_and_token, data=arguments)

        # Since we're using requests, use json() method for decoding the response
        # following will give us an array of dictionaries
        response_array_of_dict = response.json()

        return response_array_of_dict
    
    def create_cards_table(self, boards):
        """adds cards to DB"""
        print("아래의 보드 중 카드 데이터를 추출할 보드를 선택해주세요:\n")

        # iter board and index
        for idx, board in enumerate(boards):
            print("%d: %s" % (idx, board['name']))

        choice = int(input("\n선택한 보드에 해당하는 숫자를 적어주세요: "))
        board = boards[choice]
        board_id = board['id']

        cards_url = self.base + 'boards/' + board_id + '/cards'

        # cards in target board. (list of dicts)
        resp = requests.get(cards_url, params=self.params_key_and_token, data=self.arguments).json()

        # pprint(resp)

        # keys to extract from card
        keys = ['name', 'desc']

        for card in resp:
            filtered_card = { key: card[key] for key in keys }
            add_card(filtered_card)

        print_instances()



# unused script for testing
if __name__ == "__main__111":
    t = Trello()
    page = t.mmain()

    boards = t.get_cards()
    pprint(boards)

    # b = boards['name' == 'TtoC'] 
    for board in boards:
        if board['name'] == 'TtoC':
            b = board

    # print( b['id'], b['name'])
    lists = t.get_a_on_b(a='lists', b='boards', b_id=b['id'])
    pprint(lists)
    print('\n\n\n')
    
    list_id, list_name = t.prompt_list() # hardcoded for now
    cards = t.get_a_on_b(a='cards', b='lists', b_id=list_id)
    pprint(cards)

    page = t.list_to_page(cards, 'TtoC') 
    print(page)

    # use 'desc' and 'name' of card

if __name__ == "__main__":
    t = Trello()
    page = t.mmain()
    
    
    
    
    
    

 
