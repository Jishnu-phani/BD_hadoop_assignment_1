import sys

def reducer():
    current_city = None
    profit_stores = 0
    loss_stores = 0

    for line in sys.stdin:
        city, turnover = line.strip().split('\t')
        turnover = float(turnover)

        if current_city and current_city != city:
            print(f"city: {current_city}, profit_stores: {profit_stores}, loss_stores: {loss_stores}")
            profit_stores = 0
            loss_stores = 0

        current_city = city

        if turnover > 0:
            profit_stores += 1
        elif turnover < 0:
            loss_stores += 1

    if current_city:
        print(f"city: {current_city}, profit_stores: {profit_stores}, loss_stores: {loss_stores}")

if __name__ == "__main__":
    reducer()
