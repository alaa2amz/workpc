import os
from yaml import safe_load
from sqlite3 import connect
from xml.etree import ElementTree as ET
kdict_file = ''
jmdict_file = 'JMdict'
radkfile_file = ''
ksdb='ksdb.sqlite'

schema_yaml = '''# yaml
tables:
    dict:
        - name

    class:
        - name
    entry:
        - content
        - dict_id
        - format_type #to be moved to dict type

    word:
        - value unique

    class:
        - class_name
        - class_id
   
    word__class:
        - word_id
        - class_id

    word__entry:
        - word_id
        - entry_id
'''

def cr_tbl_tmplt(name,columns):
    columns = [f'{name}_id integer primary key']+columns
    return f'''create table if not exists {name}({','.join(columns)});'''

print(cr_tbl_tmplt('car',['brand','model']))

schema_dict=safe_load(schema_yaml)
print(schema_dict)
schama_string=''
for tbl_nm, clmns in schema_dict['tables'].items():
    schama_string+=cr_tbl_tmplt(tbl_nm, clmns)

print(schama_string,888)
os.remove(ksdb)
conn=connect(ksdb)
cur=conn.cursor()
cur.executescript(schama_string)
jf=open(jmdict_file,encoding='utf-8')
jm=ET.iterparse(jf)

jmdictcode=2
kebcode=25
rebcode=23
counter=0
rebs=[]
kebs=[]
for ev, el in jm:
    if el.tag == 'reb':
        cur.execute('insert or ignore into word(value) values (?)',[el.text])
        lastid = cur.lastrowid
        #print(lastid,el.text)
        if cur.rowcount != 1: 
            r=cur.execute('select word_id from word where value = ?',[el.text])
            lastid = r.fetchone()[0]
            print(lastid,77777777777777777)
            #input()
        rebs.append(lastid)
    if el.tag == 'keb':
        cur.execute('insert or ignore into word(value) values (?)',[el.text])
        lastid = cur.lastrowid
        if not lastid: 
            r=cur.execute('select word_id from word where value = ?',[el.text])
            lastid = r.fetch[0]
            print(lastid,77777777777777777,el.text)
        kebs.append(cur.lastrowid)
    if el.tag == 'entry':
        elstr = ET.tostring(el,encoding='unicode')
        cur.execute('insert into entry(content,dict_code) values (?,?)',[elstr,jmdictcode])
        entryid = cur.lastrowid
        print(entryid)
        words=[(entryid,item) for item in rebs+kebs]
        rebvalues=[(rebcode,item) for item in rebs]
        kebvalues=[(kebcode,item) for item in kebs]
        cur.executemany('insert into word__entry(entry_id,word_id) values (?,?)',words)
        cur.executemany('insert into word__class(class_code,word_id) values (?,?)',rebvalues+kebvalues)
        rebs=[]
        kebs=[]
        rebvalues=[]
        kebvalues=[]


conn.commit()
