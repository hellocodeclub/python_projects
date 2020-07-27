import json
products_json='''
    {"products":
        [{"product":
            {"name":"Bike",
             "department":"sports",
             "stock": 4}
        },
        {"product":
            {"name":"Lamp",
             "department":"home",
             "stock": 3}
        },
        {"product":
            {"name":"Table",
             "department":"home",
             "stock": 1}
        }]
    }'''
products = json.loads(products_json)
products= products['products']
stock_list = [int(product['product']['stock']) for product in products]
print(sum(stock_list))
