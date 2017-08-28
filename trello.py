# Class to model Trello objects

import requests           # a 3rd party library. `pip install requests`
import json               # all responses from Trello come back as JSON
from db import add_card, print_instances
from pprint import pprint # this is a handy utility for printing dictionaries in a human readable way

class Trello:
    # TODO: need to use OAuth to hide key and token
    # currently gets key and token from the settings file.
    # if not key or token:
    #  from settings import trello_key, trello_token
    #  key = trello_key
    #  token = trello_token
    key = trello_key
    token = trello_token
    params_key_and_token = { 
            'key' : key,
            'token' : token
            }

    base = 'https://trello.com/1/' # The base url for every request is the same
    
    def cards_in_list(self, ):
        """ get all cards from list """
        
        # get target list id
        # form url
        # send req, get resp
        # test for card names
    
    def get_list_id(self, params):
        """ 
        gets id of the target list.
        currently takes first list in board.
        """
        
    
    def get_board_id(self):
        """
        gets board id
        currently takes first board
        """
        boards = self.get_all_boards()
        firstBoard = boards[0]
        # 
    
    def get_all_boards(self):
        """
        gets list of all boards
        """
        boards_url = self.base + 'members/me/boards'
        resp = requests.get(boards_url, params=self.params_key_and_token, data=arguments)
        return resp.json()
        

        
        
    
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
 
