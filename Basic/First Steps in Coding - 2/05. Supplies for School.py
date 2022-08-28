pens = int(input())
markers = int(input())
chemicals = int(input())
discount = float(input())

end_sum = float((pens * 5.8 + markers * 7.2 + chemicals * 1.2) *((100-discount)/100))

print(f"{end_sum:.2f}")