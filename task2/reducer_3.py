# #!/usr/bin/env python3
# import sys

# def reducer3():
#     current_id = None
#     cost = 0
#     pos = 0
#     tot = 0
#     for line in sys.stdin:
#         line = line.strip()
#         parts = line.split()
#         client_id, pred, price, code = parts
#         if current_id is None:
#             current_id = client_id
#         if current_id != client_id:
#             print(f"{current_id} {pos}/{tot} {cost}")
#             current_id = client_id
#             cost = 0
#             pos = 0
#             tot = 0
#         if code == '200':
#             cost += int(price)  
#         if pred == '1':
#             pos += 1
#         tot += 1
#     print(f"{current_id} {pos}/{tot} {cost}")
        
# if __name__ == "__main__":
#     reducer3()

#!/usr/bin/env python3
import sys

def reducer3():
    current_id = None
    cost = 0
    pos = 0
    tot = 0
    for line in sys.stdin:
        client_id, pred, price, code = line.strip().split()

        if current_id is None:
            current_id = client_id

        if current_id != client_id:
            print(f"{current_id} {pos}/{tot} {cost}")
            current_id = client_id
            cost = pos = tot = 0  # Reset values

        if code == '200':
            cost += int(price)
        if pred == '1':
            pos += 1
        tot += 1

    print(f"{current_id} {pos}/{tot} {cost}")  # Print the last client

if __name__ == "__main__":
    reducer3()
