with open("weather.csv") as reader:
...    head = reader.read()
...    rain = []
...    for line in reader.readlines():
...       r = line.strip().split(",")[-1]
...       r = float(r)
...       rain.append(r)
... 
>>> print rain

