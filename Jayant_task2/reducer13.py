#!/usr/bin/env python3
import sys
curr_client = None
tot = 0
true_pred = 0
price = 0
endpoint_dict = {
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
for line in sys.stdin:
	d = line.strip().split(" ")
	c_id, endpoint, stat, pred = d
	try:
		stat = int(stat)
		pred = int(pred)
	except ValueError:
		continue
	if curr_client == c_id:
		if pred == 1:
			true_pred += 1
		tot += 1
		if stat == 200:
			price += endpoint_dict[endpoint]
	else:
		if curr_client:
			print(f"{curr_client} {true_pred}/{tot} {price}")
		curr_client = c_id
		tot = 1
		true_pred = 1 if pred == 1 else 0
		price = endpoint_dict[endpoint] if stat == 200 else 0
if curr_client:
	print(f"{curr_client} {true_pred}/{tot} {price}")