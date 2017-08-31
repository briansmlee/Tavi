# script to create html modal

from trello import Trello
from confluence import Confluence

# script
if __name__ = '__main__':
    modal = '' # html page

    # headers: check links!!!
    head = 
    '<head>
     <link rel="stylesheet" href="https://trello.com/power-ups/power-up.css">
     <style> select { height: 30px; } </style>
     <script src="https://trello.com/power-ups/power-up.min.js"></script>
     </head>'
      
    modal += head
    modal += form('modal', 
            'modalChoice', 
            'Please choose Trello list and Confluence space :') 
    

def form(form_id, label, title):
    trel = Trello()
    conf = Confluence()
    """
    makes form
    options is a dict?
    possible dec num of params?
    """
    # headers: is label neccesary?
    form = '<form id="{}">'.format(form_id)
    label = '<label for="{}">{}</label>'.format(label, title)

    # generalize below using "for options in options_list"
    resp = trel.get_a_on_b(a='lists', b='boards', b_id=board_id)
    lists = { l['name'] : l['id'] for l in resp }
    html += select('trello', 'trelloList', lists)

    spaces = conf.get_spaces()
    html += select('confluence', 'confSpace', spaces)
    html += button('submit', 'mod-primary', 'Create Page!')

    # close form
    html += '</form>'

    html += '<script src="{}"></script>'.format('./js/modal.js')
    
    pprint(html)
    return html


def select(name, s_id, options):
    html = '<select name="{}" id="{}">'.format(name, s_id)
    
    # add each list option to form
    for name, key_or_id in options:  
        line = '<option value="{}">{}</option>'.format(key_or_id, name)
        html += line
    
    html += '<\select>'
    return html

def button(b_type, b_class, text):
    return '<button type="{}" class="{}">{}</button>'.format(b_type, b_class, text)

