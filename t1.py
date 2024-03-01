#implementing luhn's algorithm
card_no = list(input("Enter the Card no.:"))
checksum = int(card_no[-1])
a = list(map(int, card_no[0:15:2]))
b = list(map(int, card_no[1:15:2]))
a2 = [] #doubled no less than 10
a3 = [] #doubled no more than 10
a4 = [] #doubled no more than 10, reduced.
for element in a:
    doubled_value = element * 2
    if doubled_value >= 10:
        a3.append(doubled_value)
    else:
        a2.append(doubled_value)

for i in a3:
    t1 = int(i/10)
    t2 = i%10
    t3 = t1+t2
    a4.append(t3)

total_sum = sum(b)+sum(a2)+sum(a4)
d = 10-total_sum%10
if d == checksum:
    print("Your card is Valid")
else:
    print("InValid")
