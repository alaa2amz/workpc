file='kradfile'
krads=[]
class KanjiParts:
    def __init__(self, kanji, part_set):
        self.kanji=kanji
        self.part_set=part_set
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
