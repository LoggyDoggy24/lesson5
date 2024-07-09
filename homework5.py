immutable_var = 1, 2, "a", "b"
print(immutable_var)
print(immutable_var)
# immutable_var[0] = 3 # кортеж не поддерживает обращение по элементам, является неизменяемым объектом.
mutable_list = [1, 2, "Freddy's coming for you", 3, 4, "Better lock your door", 5, 6, "Grab a crucifix", 7, 8, "Gonna stay up late", 9, 10, "Never sleep again..."]
print(mutable_list)
mutable_list[0] = "One"
mutable_list[1] = "two"
mutable_list[3] = "three"
mutable_list[4] = "four"
mutable_list[6] = "five"
mutable_list[7] = "six"
mutable_list[9] = "seven"
mutable_list[10] = "eight"
mutable_list[12] = "nine"
mutable_list[13] = "ten"
print(mutable_list)