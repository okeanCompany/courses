import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))   # 1 Option

random_index = random.randint(0, 4)  # 2 Option
print(friends[random_index])
