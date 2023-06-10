from pyzotero import zotero
import csv
import sys

csv_file_path = "zotero.csv"
fieldnames = ["title","text","url"]

library_type='user'

csv_data = []

# Access the command line arguments
arguments = sys.argv

# The first argument (index 0) is the script name
# The remaining arguments can be accessed by their index
library_id = arguments[1]
api_key = arguments[2]
zot = zotero.Zotero(library_id, library_type, api_key)


total_items = zot.count_items()

per_page = 100  # Number of items to fetch per batch
items = []

for start in range(0, total_items, per_page):
    batch =zot.items(start=start, limit=per_page)
    items.extend(batch)
    print(len(items))


# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:

    
    title = item['data']['title'] 
    try:
        text = item['data']['abstractNote']
    except:
        text = ''

    url = item['data']['url']
    csv_data_row = { 
        "text" : text,
	"url" : url,
	"title" : title
    }
    
    csv_data.append(csv_data_row)


# Write the data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(csv_data)

print(len(csv_data))
