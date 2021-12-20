import math

levelofprod = 2
maxminer = 2700 /30/(1+levelofprod/10) /2
maxrad  = maxminer *3
tilegauge = 3.5
tilegroup =2
print(maxminer,maxrad)
for i in range(2,888,2):
    
    area = i *900/30/(1+levelofprod/10) * 10.5
    radiu = math.sqrt(area/math.pi)
    lanesofpatch = int(math.ceil(radiu/tilegauge))
    print(str(i)+'lanes',str(area)+'sqrm',round(radiu,2),lanesofpatch)
    if radiu > maxrad:
        print('too large for current layout')
        break
    epmn = 0
    if lanesofpatch % 2:
        epmn -= int(((radiu/1.5)//3+1)*3)*2
        for j in range(lanesofpatch//2+1):
            numberofminer = math.cos(math.asin(j * 2*tilegauge/radiu))*radiu/1.5
            print('o'+str(j),int((numberofminer//tilegroup+1)*tilegroup),numberofminer)
            epmn += int((numberofminer//tilegroup+1)*tilegroup) * 4
        print(epmn,int(area/10.5))
    else:
        for j in range(lanesofpatch//2):
            numberofminer = math.cos(math.asin((j * 2*tilegauge+tilegauge)/radiu))*radiu/1.5
            print('o'+str(j),int((numberofminer//tilegroup+1)*tilegroup),numberofminer)
            epmn += int((numberofminer//tilegroup+1)*tilegroup) * 4
        print(epmn,area/10.5)

print('max rad is ',maxrad)