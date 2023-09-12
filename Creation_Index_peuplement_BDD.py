from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class Product(Document):
    id = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    prices__amountMax = float()
    prices__amountMin = float()
    prices__availability = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    prices__condition = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    prices__currency = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    prices__isSale = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    prices__merchant = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    asins = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    brand = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    name = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    primaryCategories = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    upc = Text(analyzer={"rebuilt_whitespace":{"tokenizer": "standard","filter": ["lowercase"]}})
    

    class Index:
        name = 'test2_ingest'
        settings = {
          "number_of_shards": 2,
        }

    
# create the mappings in elasticsearch
Product.init()

# create and save and article
Product = Product()
Product.id = '1'
Product.prices__amountMax= 20
Product.prices__availability = 'In stock'
Product.prices__condition = 'New'
Product.prices__currency = 'USD'
Product.prices__isSale = 'True'
Product.prices__merchant = "Test.com"
Product.asins = 'TEST'
Product.brand = 'Sony'
Product.name = 'TEST'
Product.primaryCategories = 'Electronics'
Product.upc = '6.42E+11'
Product.save()

Prod = Product.get(id=1)
print(Prod.name)

# Display cluster health
print(connections.get_connection().cluster.health())