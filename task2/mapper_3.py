#!/usr/bin/env python3
import sys
endpoint_prices = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}
# def mapper3():
#     for line in sys.stdin:
#         parts = line.strip().split()
#         client_id, endpoint, pred, code = parts
#         print(f"{client_id} {pred} {endpoint_prices[endpoint]} {code}")
        
# if __name__ == "__main__":
#     mapper3()

#!/usr/bin/env python3
# import sys

# endpoint_prices = {
#     'user/profile': 100,
#     'user/settings': 200,
#     # Add other endpoints here
# }

def mapper3():
    for line in sys.stdin:
        client_id, endpoint, pred, code = line.strip().split()
        price = endpoint_prices[endpoint] 
        print(f"{client_id} {pred} {price} {code}")

if __name__ == "__main__":
    mapper3()