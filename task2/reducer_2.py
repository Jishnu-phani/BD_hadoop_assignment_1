# #!/usr/bin/env python3
# import sys
# endpoint_prices = {
#     'user/profile': 100,
#     'user/settings': 200,
#     'order/history': 300,
#     'order/checkout': 400,
#     'product/details': 500,
#     'product/search': 600,
#     'cart/add': 700,
#     'cart/remove': 800,
#     'payment/submit': 900,
#     'support/ticket': 1000
# }
# def reducer2():
#     for line in sys.stdin:
#         parts = line.strip().split()
#         request_id, client_id, endpoint, predicted_code, actual_code = parts
#         if int(actual_code) == int(predicted_code):
#             print(f"{client_id} {endpoint} {1} {actual_code}")
#         else:
#             print(f"{client_id} {endpoint} {0} {actual_code}")
        
# if __name__ == "__main__":
#     reducer2()

#!/usr/bin/env python3
import sys

def reducer2():
    for line in sys.stdin:
        request_id, client_id, endpoint, predicted_code, actual_code = line.strip().split()
        is_match = 1 if actual_code == predicted_code else 0
        print(f"{client_id} {endpoint} {is_match} {actual_code}")

if __name__ == "__main__":
    reducer2()
