# scores = [100, 23, 45,65,121,45,65,99, 123]

# Input: 1 2 3 4 5
scores = list(map(int, input("Enter integers separated by space: ").split()))

max_score = 0

for score in scores:
    if score > max_score:
        max_score = score

print(max_score)