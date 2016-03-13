#UVa_100 2016.03.12
def cycleL(num):
    cycle = []
    cycle.append(num)
    while num != 1:
        numcri = num %2
        if numcri != 0:
            num = num*3 + 1
        else:
            num = num/2
        cycle.append(num)
    #print (cycle)
    return len(cycle)
        
def main(numi,numj):
        if numi > numj:
            newnumi = numj
            newnumj = numi
        else:
            newnumi = numi
            newnumj = numj
        cal_list = []
        for a in range(newnumi,newnumj+1,1):
            cal_list.append(a)
        cyc_list = []
        for i in cal_list:
            cyc_list.append(cycleL(i))
        print (numi,numj,max(cyc_list))

numi = int(input("(Number only)Number:"))
numj = int(input("(Number only)Number:"))
main(numi, numj)
