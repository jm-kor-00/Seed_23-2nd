def combi(n,r):
    i = 1
    p = 1
    while i <= r:
        p = p*(n-i+1) // i
        i += 1
    return p
    
sum = 0

for i in range(0,21):
    sum += combi(120,i) * ((0.1) ** i) * (0.9)**(120-i)

print(sum) 