"""

===========================================================
   LECTURE 05 - SET 05 :     MINI PROJECT
   Topics :       Loops
============================================================

"""

# ==========================================================
#              RESTAURANT BILLING SYSTEM
# ==========================================================

# ----------------------------------------------------------
#    STEP 01:     Display Menu
# ----------------------------------------------------------

print("\n--- Menu ---")

menu = ['Burger', 'Pizza', 'Pasta', 'Juice']
prices = [150, 250, 180, 60]

for i, item in enumerate(menu, 1) :
    print(str(i) + ".", item, "- Rs." + str(prices[i - 1]))

# ----------------------------------------------------------
#    STEP 02:    Take Orders & Calculate Bill
# ----------------------------------------------------------

print("\n--- Order & Bill ---")

orders = [(0, 2), (1, 1), (3, 3)]   # (menu_index, qty)
total = 0

for idx, qty in orders :
    subtotal = prices[idx] * qty
    total += subtotal
    print(menu[idx], "x" + str(qty), "= Rs." + str(subtotal))

if total > 500 :
    discount = total * 10 // 100
    total -= discount
    print("Discount (10%): -Rs." + str(discount))

print("Grand Total: Rs." + str(total))

# ----------------------------------------------------------
#    STEP 03:    Receipt Border Pattern
# ----------------------------------------------------------

print("\n--- Receipt ---")

for row in range(5) :
    for col in range(25) :
        if row == 0 or row == 4 :
            print("=", end=" ")
        elif col == 0 or col == 24 :
            print("|", end=" ")
        elif row == 2 and 8 <= col <= 16 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ----------------------------------------------------------
#    STEP 04:    Weekly Sales Report
# ----------------------------------------------------------

print("\n--- Weekly Sales ---")

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [1200, 800, 950, 2100, 2500]
best_day = days[0]
best_sale = sales[0]
total_sales = 0

for i in range(len(days)) :
    total_sales += sales[i]
    if sales[i] > best_sale :
        best_sale = sales[i]
        best_day = days[i]
    if sales[i] < 1000 :
        print(days[i] + ": Rs." + str(sales[i]), "⚠ Low")
        continue
    print(days[i] + ": Rs." + str(sales[i]), "✓")

print("Total: Rs." + str(total_sales))
print("Best Day: ", best_day, "(Rs." + str(best_sale) + ")")

