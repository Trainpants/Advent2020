def adjseats(x,y,matrix):
    adjs = []
    for xs in range(x-1,x+2):
        for ys in range(y-1,y+2):
            adjs += [matrix[xs][ys]]
    return adjs
# returns a list of the state of chairs around/including a given chair (5) in form of
# 1 2 3
# 4 5 6 
# 7 8 9   -> [1,2,3,4,5,6,7,8,9]


with open("input.txt") as datafile:
    seats = ["." + line.strip() + "." for line in datafile.readlines()]

cap = ["."*len(seats[0])]
print(cap)
seats = cap + seats + cap
# adds "floor" around entirety of dataset so as to avoid index errors
# while checking for occupied adjacent seats

newseats = cap
print(cap)
print(newseats)
#while newseats != seats:

for irow,erow in enumerate(seats[1:len(seats)-1]):
    newrow = "."
    for icol,ecol in enumerate(seats[irow+1][1:len(seats[0])-1]):
        if ecol != ".":
            adjs = adjseats(irow+1,icol+1,seats)
            if ecol == "L":
                if adjs.count("#") == 0:
                    newrow += "#"
            else:
                if adjs.count("#") > 4:
                    newrow += "L"
        else:
            newrow += "."
    
    newrow += "."
    newseats += [newrow]


print(cap)

#    newseats.append(cap)
#    if newseats != seats:
#        seats = newseats
#        newseats = [cap]


#sum = 0
#for line in seats:
#    sum += line.count("#")

#print(sum)