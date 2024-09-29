# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

# Slow first version
# lines = []
#
# for i in range(0, n):
#     line = input().strip()
#     lines.append(line)
#
#
# for line in lines:
#     odd = []
#     even = []
#     for i in range(len(line)):
#         if i % 2 == 1:
#             odd.append(line[i])
#         else:
#             even.append(line[i])
#
#     print(f"{''.join(even)} {''.join(odd)}") 

# Optimized
for _ in range(n):
    line = input().strip()
    even = line[::2]
    odd = line[1::2]
    print(f"{even} {odd}")

    # Time Complexity: O(n * m)
    # Space Complexity: O(m)
