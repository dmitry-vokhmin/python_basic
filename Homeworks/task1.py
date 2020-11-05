from sys import argv

_, hours, h_rate, benefits = argv

result = (int(hours) * int(h_rate)) + int(benefits)

print(result)