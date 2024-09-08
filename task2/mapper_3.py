#!/usr/bin/env python
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
def mapper3():
    for line in sys.stdin:
        parts = line.strip().split()
        client_id, endpoint, success = parts
        print(f"{client_id} {success} {endpoint_prices[endpoint]}")
        
if __name__ == "__main__":
    mapper3()