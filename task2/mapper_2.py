# #!/usr/bin/env python3
# import sys
# id = {}
# endpoint_dict = {}
# def mapper2():
#     for line in sys.stdin:
#         parts = line.strip().split()
#         if len(parts) == 6:
#             timestamp, request_id, client_id, endpoint, servers_down, predicted_code = parts
#             if timestamp not in id:
#                 id.clear()
#                 id[timestamp] = []
                
#             if client_id in id[timestamp]:
#                 # print(f"{request_id} {client_id} {endpoint}, '500'")
#                 continue
#             id[timestamp].append(client_id)
            
#             if timestamp not in endpoint_dict:
#                 endpoint_dict.clear()
#                 endpoint_dict[timestamp] = {}
                
#             if endpoint not in endpoint_dict[timestamp]:
#                 endpoint_dict[timestamp][endpoint] = {}
#                 endpoint_dict[timestamp][endpoint]["servers_down"] = float(servers_down)
                
#             if endpoint_dict[timestamp][endpoint]["servers_down"] < 3.0:
#                 endpoint_dict[timestamp][endpoint]["servers_down"] +=1
#                 actual_code = 200
#                 print(f"{request_id} {client_id} {endpoint} {predicted_code} {actual_code}")
#             else:
#                 actual_code = 500
#                 print(f"{request_id} {client_id} {endpoint} {predicted_code} {actual_code}")
            
# if __name__ == "__main__":
#     mapper2()

#!/usr/bin/env python3
import sys
id = {}
endpoint_dict = {}
def mapper2():
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) == 6:
            timestamp, request_id, client_id, endpoint, servers_down, predicted_code = parts
            if client_id in id.get(timestamp, []):
                continue

            id.setdefault(timestamp, []).append(client_id)

            endpoint_info = endpoint_dict.setdefault(timestamp, {}).setdefault(endpoint, {"servers_down": float(servers_down)})

            if endpoint_info["servers_down"] < 3.0:
                endpoint_info["servers_down"] += 1
                actual_code = 200
            else:
                actual_code = 500

            print(f"{request_id} {client_id} {endpoint} {predicted_code} {actual_code}")

if __name__ == "__main__":
    mapper2()
