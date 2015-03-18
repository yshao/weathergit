# data: a lists of lists (length 2) of measurements
# res: resulting list of lists
# delta: time delta

# output list (will be a list of lists, as in the question

res = []
# end of first bin:
binstart = data[0][0]
res.append([binstart, []])

# iterate through the data item
for d in data:
    # if the data item belongs to this bin, append it into the bin
    if d[0] < binstart + delta:
        res[-1][1].append(d[1])
        continue

    # otherwise, create new empty bins until this data fits into a bin
    binstart += delta
    while d[0] > binstart + delta:
        res.append([binstart, [])
        binstart += delta

    # create a bin with the data
    res.append([binstart, [d[1]]])