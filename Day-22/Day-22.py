s1, s2 = 0, {}
for num in map(int, open("./Day-22/input.in")):
    seen = set()
    last4 = (10, 10, 10, 10)
    for _ in range(2000):
        prev = num%10
        num ^= num*64 % 16777216
        num ^= num//32
        num ^= num*2048 % 16777216
        last4 = last4[1:] + (num%10 - prev,)
        if last4 not in seen:
            seen.add(last4)
            s2[last4] = s2.get(last4, 0) + num%10
    s1 += num



solution_1 = s1
solution_2 = max(s2.values())

print ("Answer to Day 22: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)