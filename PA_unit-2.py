#Prices of the three items
item1 = 200.0
item2 = 400.0
item3 = 600.0

#Discount rules
combo_discount = 0.10     #10% for two-item combos
gift_discount = 0.25      #25% for all three items


def online_store():
    print("Online Store")
    print("---------------------------")
    print("Product(S)          Price")

    #Print individual items (no discount)
    print(f"Item 1              {item1}")
    print(f"Item 2              {item2}")
    print(f"Item 3              {item3}")

    #Get the discount price of Item 1 + 2
    combo1_total = item1 + item2
    combo1_price = combo1_total - (combo1_total * combo_discount)

    #Get the discount price of Item 2 + 3
    combo2_total = item2 + item3
    combo2_price = combo2_total - (combo2_total * combo_discount)

    #Get the discount price of Item 1 + 3
    combo3_total = item1 + item3
    combo3_price = combo3_total - (combo3_total * combo_discount)

    #Get the discount price of when all three Item is bought 1 + 2 + 3
    combo4_total = item1 + item2 + item3
    combo4_price = combo4_total - (combo4_total * gift_discount)

    #Print combos
    print(f"Combo 1 (Item 1 + 2)    {combo1_price}")
    print(f"Combo 2 (Item 2 + 3)    {combo2_price}")
    print(f"Combo 3 (Item 1 + 3)    {combo3_price}")
    print(f"Combo 4 (Item 1 + 2 + 3) {combo4_price}")

    print("-----------------------------")
    print("For delivery Contact:98764678899")


# Call the function
online_store()
