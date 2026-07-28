from itertools import filterfalse
import sys
file_full_name = 'uradk'
with open(file_full_name) as f:
    content = f.read()
content = content.split('$')

class Part:
    def __init__(self, literal, stroke_order,names, kanji_set):
        self.literal = literal 
        self.stroke_order = stroke_order 
        self.names = names 
        self.kanji_set = kanji_set 
        
parts=[]
for index,part_lines in enumerate(content):
    if index < 2: continue
    header,kanjies = part_lines.split('\n',1)
    #literal, stroke_order, *names = header.split(maxsplit=3)
    literal, stroke_order, *names = header.split()
    kanji_set=set(kanjies)
    kanji_set.discard(' ')
    kanji_set.discard('\n')
    #print(f'{literal=} {names=} {kanji_set=}')
    part=Part(literal, stroke_order, names, kanji_set)
    parts.append(part)

if len(sys.argv) > 1:
    final_set=set()
    for c,i in enumerate(sys.argv[1:]):
        for part in parts:
            if i in part.names:
                print('match',part.literal)
                if c > 0:
                    final_set = final_set.intersection(part.kanji_set)
                else:
                    #print('into',part.kanji_set)

                    final_set = final_set.union(part.kanji_set)
                    #print(999,final_set)

    print(''.join(final_set))



