import sys
import json
def reducer():
    current_city = None
    profit_stores = 0
    loss_stores = 0

    for line in sys.stdin:
        city, turnover = line.strip().split('\t')
        turnover = float(turnover)

        if current_city and current_city != city:
            x = {'city': current_city, 'profit_stores': profit_stores, 'loss_stores': loss_stores}
            # print(f"{x}")
            print(json.dumps(x))
            profit_stores = 0
            loss_stores = 0

        current_city = city

        if turnover > 0:
            profit_stores += 1
        elif turnover <= 0:
            loss_stores += 1

    if current_city:
        x = {'city': current_city, 'profit_stores': profit_stores, 'loss_stores': loss_stores}
        # print(f"{x}")
        print(json.dumps(x))

if __name__ == "__main__":
    reducer()
