# demo from https://github.com/bmccormack/trello-python-demo/blob/master/demo.py#L54


import requests           # a 3rd party library. I installed via `pip install requests`
#import json               # all responses from Trello come back as JSON, so have your favorite JSON library handy
from pprint import pprint # this is a handy utility for printing dictionaries in a human readable way


### Getting an API Key and Token
# need to use OAuth to hide key and token
# get key and token from the settings file.
key = ''
token = ''

if not key or token:
  from settings import trello_key, trello_token
  key = trello_key
  token = trello_token


### make requests to the Trello API
# For each request, you need to do two things:
#
#   1) Identify which HTTP method you're going to use: GET, PUT, POST, or DELETE
#        - NB: You can think of PUT as shorthand for 'update' (something that already exists)
#              and POST as shorthand for 'insert' (something that's being added for the first time).
#              HTTP pedants might balk at that, but it will work for us.
#   2) Piece together the URL you want to target
#
# You'll probably want to create helper methods/classes for your particular environment to make that
# a bit easier. For now, I'll piece stuff together manually. For an example of a small python library that
# does some of this for you, see https://developers.kilnhg.com/Code/Trello/Group/TrelloSimple/Files/trelloSimple.py?rev=eeef45bd880a&nr=
#####################

### GET request to the Trello API ###
#
# We're going to make a GET request to the Trello API and print out a list of the boards
# to which we belong.
#
# The base url for every request is the same
base = 'https://trello.com/1/'

# Build out the URL based on the documentation
boards_url = base + 'members/me/boards'

# Let's store our API key and token as parameters
params_key_and_token = {'key':key,'token':token}

# Since we only want the name of the board, let's supply the 'fields' argument as well. We're also going to
# ask for lists, to be used later.
arguments = {'fields': 'name', 'lists': 'open'}

# The requests library has separate methods for get, put, post, and delete. We need a GET here.
# We need to provide the URL we want to access, the key and token (params_key_and_token) as params, as well as
# any arguments (arguments) as data.
response = requests.get(boards_url, params=params_key_and_token, data=arguments)

# We should pause here and point out that the requests library is making everying incredibly
# easy for us. We're able to work in native python dictionaries and requests is automatically
# form-encoding our 'arguments' dictionary when the request is made. This is quite handy
# and lets us get right to working with the Trello API.
#
# If you're making your own script, you might check out query_trello in
# trello_helper.py, which wraps up the last few lines of code in a repeatable
# fashion.

# Since we're using requests, there's a json() method for decoding the response. If you're not using
# requests or are using a different language, you may need to use your favorite JSON library to deserialize
# the content of the response into a native dictionary.
#
# The following will give us an array of dictionaries
response_array_of_dict = response.json()

# Let's go ahead and iterate through the list of boards and print the name of each board
for board in response_array_of_dict:
  print(board['name'])

###########################



### Adding a card to the welcome board #######################
#
# Now that we've comfortable making a request, let's try adding a card to the Welcome Board.
#
# NB: This part assumes you have a board named "Welcome Board", which is added when you sign
#     up for Trello, but if you removed or renamed it, go ahead and add one to the account
#     you're testing with.
#
# Since we already have a list of boards, let's iterate through that list and find the welcome board

for board in response_array_of_dict:
  # Look for the board name that matches 'Welcome Board'
  if board['name'] == 'Welcome Board':

    # get board id
    board_id = board['id']

    # url to get all cards
    cards_url = base + 'boards/' + board_id + '/cards'

    resp = requests.get(cards_url, params=params_key_and_token, data=arguments).json()

    print('Following are card names for Welcome Board:')


    for card in resp:
        print(card['name'])



    # Before we go further, let's go ahead and build our URL, based on https://trello.com/docs/api/card/index.html#post-1-cards
    #cards_url = base + 'cards'

    # Back when we originally queried the Trello API, we asked it to include the lists on the board.
    # We need a list to add a card, so let's grab the id of the first list:
    #id_list = board['lists'][0]['id']

    # Let's provide a name and description for the card
    #name = 'Card via the API'
    #description = 'I made this card using the Trello API :fist:'

    # These values need to be put into a dictionary, which requests will form-encode for us
    #arguments = {'name': name,
    #            'desc': description,
    #             'idList' : id_list}

    # Since this particular method uses POST, we're going to need to use requests.post
    #response = requests.post(cards_url, params=params_key_and_token, data=arguments)

    # When we POST a new card to Trello, the API will respond with json data about the
    # the new card. Let's pretty print the response and take a look at it.
    # pprint(response.json())
























