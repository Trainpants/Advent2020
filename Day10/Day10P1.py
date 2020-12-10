with open("input.txt") as datafile:
    adapters = [int(line.strip()) for line in datafile.readlines()]

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

diff = [adapters[i+1] - adapters[i] for i in range(0,len(adapters)-1)]

print(diff.count(1)*diff.count(3))
