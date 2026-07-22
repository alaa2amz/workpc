file='kradfile'
file2='uradk'
krads=[]
radnms=[]
class KanjiParts:
    def __init__(self, kanji, part_set):
        self.kanji=kanji
        self.part_set=part_set
class PartNames:
    def __init__(self,part,stroke_count,name_set):
        self.part = part
        self.stroke_count = stroke_count
        self.name_set = name_set
with open(file2) as f:
    for l in f:
        l=l.strip()
        if l[0] != '$':
            continue
        doll,part,strkcnt,*names = l.split()
        names=set(names)
        pn=PartNames(part,strkcnt,names)
        radnms.append(pn)


with open(file,encoding='euc_jp') as f:
    for l in f:
        l=l.strip()
        if l[0] == '#':
            continue
        print(l)
        k ,prts = l.split(':')
        k=k.strip()
        prts=prts.strip()
        prts=prts.split()
        kp=KanjiParts(k,set(prts))
        krads.append(kp)

