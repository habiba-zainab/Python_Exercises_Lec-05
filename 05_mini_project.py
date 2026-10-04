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
