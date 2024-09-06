import json
import sys

def mapper():
    buffer = ''
    for line in sys.stdin:
        line = line.strip().rstrip(',')

        if not line or line in ["[", "]"]:
            continue
        buffer += line
        
        if buffer.endswith('}'):
            try:
                data = json.loads(buffer)
                buffer = ""
                there = False
                turnover = 0
                for j in data['categories']:
                    if j in data['sales_data']:
                        # if 'revenue' not in data['sales_data'][j] and 'cogs' not in data['sales_data'][j]:
                        #     continue
                        there = True
                        if 'revenue' not in data['sales_data'][j]:
                            data['sales_data'][j]['revenue'] = 0
                        if 'cogs' not in data['sales_data'][j]:
                            data['sales_data'][j]['cogs'] = 0
                        turnover = turnover + data['sales_data'][j]['revenue'] - data['sales_data'][j]['cogs']

                if there:
                    print(f"{data['city']}\t{turnover}")
            
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    mapper()



# import json

# # Specify the path to the JSON file
# file_path = 'BD\\Assignment_1\\large_data.json'

# # Open the file and load the JSON data
# with open(file_path) as file:
#     data = json.load(file)
    
# fin = []

# for i in data:
#     if i['sales_data']:
#         turnover = 0
#         for j in i['sales_data']:
#             if j not in i['categories']:
#                 continue
#             if 'revenue' not in i['sales_data'][j] and 'cogs' not in i['sales_data'][j]:
#                 continue
#             if 'revenue' not in i['sales_data'][j]:
#                 # print("no revenue present")
#                 i['sales_data'][j]['revenue'] = 0
#             if 'cogs' not in i['sales_data'][j]:
#                 # print("no cogs present")
#                 i['sales_data'][j]['cogs'] = 0
#             turnover += i['sales_data'][j]['revenue'] - i['sales_data'][j]['cogs']
#         # print(turnover)
#         x = {'city': i['city'],'store_id': i['store_id'], 'turnover': turnover}
#         # print(x)
#         fin.append(x)

# out = {}
# fin.sort(key = lambda x: x['city'])
# for i in fin:
#     if i['city'] in out:
#         if i['turnover'] > 0:
#             out[i['city']]['profit_stores'] += 1
#         elif i['turnover'] < 0:
#             out[i['city']]['loss_stores'] += 1
#     else:
#         out[i['city']] = {'profit_stores': 0, 'loss_stores': 0}
#         if i['turnover'] > 0:
#             out[i['city']]['profit_stores'] += 1
#         elif i['turnover'] < 0:
#             out[i['city']]['loss_stores'] += 1
# # print(out)

# outt = []
# for i in out.keys():
#     outt.append({'city': i, 'profit_stores': out[i]['profit_stores'], 'loss_stores': out[i]['loss_stores']})

# for i in outt:
#     print(i)