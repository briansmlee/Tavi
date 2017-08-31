# main script to create page in confluence.
# 
# This script is called by event hanlder in config.js,
# when submit button is clicked.
#

from trello import Trello
from confluence import Confluence

def main(list_id, space_id):
    trel = Trello()
    conf = Confluence()
    page = trel.format_page(list_id) # html pageData
    conf.create_page(page, space_key) # creates page
    print('\n\n\n page.py script is done!!! \n\n\n') # TEST 

if __name__ == '__main__':
    # $_POST[''] is the syntax to access data sent by ajax()
    list_id = $_POST['list_id']
    space_key = $_POST['space_key']
    main(list_id, space_key)
