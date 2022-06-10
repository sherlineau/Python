from classes.store import Store

WholeFoods = Store("Whole Foods")
WholeFoods.add_new_product("steak", 13, "meat")
WholeFoods.add_new_product("apples", 1, "produce")
WholeFoods.add_new_product("apples", 1, "produce")
WholeFoods.add_new_product("apples", 1, "produce")
WholeFoods.inflation(0, 25)
WholeFoods.clearance("produce",10)

print("___________________________________")

Target = Store("Target")
Target.add_new_product("Grill", 30, "outdoor")
Target.add_new_product("apples", 1, "produce")
Target.add_new_product("Nintendo Switch", 199, "electronics")
Target.print_all_products()