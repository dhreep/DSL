import fileinput
for line in fileinput.input():
    data = line.strip().split(",")
    if len(data) == 8:
        SNo, Observation,  Province, Country, LastUpdate, Confirmed, Deaths, Recovered = data
        if not Confirmed.isnumeric():
            continue
        print("{0}\t{1}".format(Country, Confirmed))
