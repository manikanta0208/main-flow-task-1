my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list.append(6)
print("List after adding an element:", my_list)
my_list.remove(3)
print("List after removing an element:", my_list)
my_list[0] = 10
print("List after modifying an element:", my_list)

print("\n")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)
del my_dict['b']
print("Dictionary after removing an element:", my_dict)
my_dict['a'] = 10
print("Dictionary after modifying an element:", my_dict)
print("\n")
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
my_set.add(6)
print("Set after adding an element:", my_set)
my_set.remove(3)
print("Set after removing an element:", my_set)
my_set.remove(1)
my_set.add(10)
print("Set after modifying an element (indirectly):", my_set)
