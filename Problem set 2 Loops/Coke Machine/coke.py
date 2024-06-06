amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: ").strip())
    if insert_coin != 25 and insert_coin != 10 and insert_coin != 5:
        continue
    elif insert_coin <= amount_due:
        amount_due = amount_due - insert_coin
        if amount_due == 0:
            print(f"Change Owed: {0}")
            break
    elif insert_coin > amount_due:
        print(f"Change Owed: {insert_coin - amount_due}")
        break



#OPTIMIZED CODE FOR GIVEN
# amount_due = 50
# valid_coins = {25, 10, 5}

# while amount_due > 0:
#     print(f"Amount Due: {amount_due}")
#     try:
#         insert_coin = int(input("Insert Coin: ").strip())
#     except ValueError:
#         continue

#     if insert_coin in valid_coins:
#         amount_due -= insert_coin

#     if amount_due <= 0:
#         print(f"Change Owed: {abs(amount_due)}")
#         break

