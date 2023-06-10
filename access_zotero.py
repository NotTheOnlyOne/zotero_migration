from pyzotero import zotero

library_type='user'

import sys

# Access the command line arguments
arguments = sys.argv

# The first argument (index 0) is the script name
# The remaining arguments can be accessed by their index
library_id = arguments[1]
api_key = arguments[2]
zot = zotero.Zotero(library_id, library_type, api_key)

items = zot.top(limit=10)

# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:

    
    print(item['data']['title'])
    print(item['data']['abstractNote'])
    print(item['data']['url'])

    #print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['title'], item['data']['title'],item['data']['title']))
