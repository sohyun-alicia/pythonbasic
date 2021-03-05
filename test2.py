ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]

lst = []
for i in ohlc[1:]:
    plus = i[3] - i[0]
    lst.append(plus)
print(sum(lst))