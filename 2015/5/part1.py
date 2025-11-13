from main import is_nice_1, is_nice_2

with open("input.txt") as i:
    all_messages = i.readlines()

print(sum(1 for m in all_messages if is_nice_1(m)))
print(sum(1 for m in all_messages if is_nice_2(m)))