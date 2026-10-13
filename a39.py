basket1 = {"apple","banana","mango","apple","grape"}
basket2 = {"mango","kiwi","banana","kiwi"}
print("basket 1:", basket1)
print("basket2 :",basket2)

basket1.add("orange")
print("basket 1 added orange:",basket1)


comman_fruit = basket1.intersection(basket2)
print ("fruit in basket",comman_fruit)

import array as arr
fruit_counter = arr.array('i',[3,5,2,4])
print("fruit counts array:",fruit_counter)

fruit_counter.insert(0,1)
fruit_counter.append(6)
print("food count:",fruit_counter)

count_of_4 = fruit_counter.count(4)
print("nummber of times 4 appears:",count_of_4)

fruit_counter.reverse()
print("raver fruit count arry:",fruit_counter)



print("")
print("=============================================================================================================================Class fruit baskit ===================================================================================")
print("baskit1",basket1)
print("baskit2",basket2)
print("shared fruits:",comman_fruit)
print("fruit counter",fruit_counter)
