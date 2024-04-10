print("Amount Due: 50")

coca_cola = 50
coins = 0

while True:
    coin = int(input("Insert Cion: "))
    if coin in [25, 10, 5]:
        coca_cola -= coin
        coins += coin

    if coins >= 50:
        print(f"Change Owed: {coins - 50}")
        break
    else:
        print(f"Amount Due: {coca_cola}")
