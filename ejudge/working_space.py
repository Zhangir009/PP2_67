n = int(input())
a = list(map(str, input().split()))
sum = list(lambda x_i : x_i[0] % 2 == 0, enumerate(a))
even = [x for i, x in sum]
print(sum)