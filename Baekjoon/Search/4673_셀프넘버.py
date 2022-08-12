s = list(range(1, 10001))
generated_num = []

for i in range(10001):
    generated_num.append(i+sum(list(map(int, str(i)))))

self_num = sorted(set(s) - set(generated_num))
for i in self_num:
    print(i)