# script to create html modal

from trello import Trello
from confluence import Confluence


modal = '' # html page

# check links
head =
' <head>
    <link rel="stylesheet" href="https://trello.com/power-ups/power-up.css">
    <style>
      select { height: 30px; }
    </style>
    <script src="https://trello.com/power-ups/power-up.min.js"></script>
  </head>'

modal += head




def make_form(options, form_id, label, title, form_name):
    """
    makes form
    possible dec num of params?
    """
    # headers
    form = '<form id="{}">'.format(form_id)
    label = '<label for="{}">{}</label>'.format(label, title)
    select = '<select name="{}" id="{}">'.format(form_name, label)
    html = form + label + select
    
    # add each list option to form
    for item in options:
        name = item['name']
        line = '<option value="{}">{}</option>'.format(name.lower(), name)
        html += line
    
    # close
    html += '</select></form>'
    
    pprint(html)
    return html
    
