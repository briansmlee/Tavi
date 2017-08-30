# main script to make Conf page from Trello list

from trello import Trello
from confluence import Confluence

if __name__ == "__main__":
   t = Trello()
   conf = Confluence()
   conf.create_page(t.mmain())
   print('main sript done!')
   

