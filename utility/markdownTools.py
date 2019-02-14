
def markdownTable(table):
    width=max(map(lambda row:len(row),table))
    res = (' | '.join(table[0]))+'\n'+('|'.join(['---' for i in range(0,width)]))
    for row in table[1:]:
        res+='\n'+(' | '.join(row))
    return res

        