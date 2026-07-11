import itertools
import json
from itertools import product

## constants
blue = [0, 0, 255]
electric_indigo = [100, 0, 255]
blue_ribbon = [0, 100, 255]
alone_in_the_dark = [0, 0, 100]
#https://colordesigner.io/color-name-finder
low_transparency = 0.3
zero_transparency = 0.0
skell_sample_file = 'skell_sample.json'

def mater_plastic(color, transparency=0.0 , reflection=0.0):
    """construct mater command arguments supplied after group.
    mater group "shader" color inherent?"""
    color_string = ' '.join(map(str,color))
    return f'"plastic {{tr {transparency} re {reflection}}}" {color_string} 0'  

vertical_column_mater = mater_plastic(blue, low_transparency)
long_beam_mater = mater_plastic(electric_indigo, low_transparency)
cross_beam_mater = mater_plastic(alone_in_the_dark, zero_transparency)
base_mater = mater_plastic(alone_in_the_dark, low_transparency)
boundary_box_color = mater_plastic(alone_in_the_dark, zero_transparency)

def parse_json_file(file_path):
    with open(file_path) as file:
        json_dict = json.loads(file.read())
        return json_dict

sample = {
        'collumns': {'absolutes': {0:0, 1: 3000}, 'count': 3, 
                     'offsets': {'default':2500, '2': 3500}},
        'rows': {'absolutes': {0:0, 1:3000}, 'count': 3, 
                 'offsets': {'default':2500,2: 3500} },
        'plans': {'absolutes': {0:0,1: 7000}, 'count': 3, 
                  'offsets': {'default':2500, 2: 3500}},

    'long_beam': {'flange_thick': 10, 'flange_width': 100, 'handle': 'tos',
                   'rotation': [0, 0, 0], 'total_height': 150, 'type': 'fi',
                   'web_thick': 20},
    'cross_beam': {'flange_thick': 10, 'flange_width': 100, 'handle': 'tos',
                   'rotation': [0, 0, -90], 'total_height': 150, 'type': 'fi',
                   'web_thick': 20},
    'vertical_column': {'flange_thick': 10, 'flange_width': 100, 'handle':
                        'cen', 'rot': [0, 90, 0], 'total_height': 150, 'type':
                        'fi', 'web_thick': 20},
    'beams': {(0,1,1,'vertical'): {'flange_thick': 10, 'flange_width': 100, 'rot':
                              [0, 90, 0], 'total_height': 150, 'type': 'fi',
                              'web_thick': 20},
              },
    'margin': 5000,
    'floor_depth': 2000,
         }

class SequenceDescriptor:
    def __init__(self, count=3, absolutes={0:0}, offsets={'default':3000}):
        print(count)
        self.count = count
        self.absolutes = absolutes
        self.offsets = offsets

    def get_squence(self):
        sequence = [0] * self.count
        for i in range(self.count):
            #always take zero from absolutes
            if i in self.absolutes:
                sequence[i] = self.absolutes[i]
                continue
            elif i in self.offsets:
                sequence[i] = sequence[i-1] + self.offsets[i]
            else:
                sequence[i] = sequence[i-1] + self.offsets['default']
        return sequence

def main():
    s=Skell(sample)
    print(s.get_sequences())
    s.insert()

class Skell:
    #TODO handle live setter updates
    def __init__(self, data):
        self.collumns=''
        self.rows=''
        self.plans=''
        for key in data:
            setattr(self, key, data[key])
    
    def get_sequences(self):
        collumns = SequenceDescriptor(**self.collumns).get_squence()
        rows = SequenceDescriptor(**self.rows).get_squence()
        plans = SequenceDescriptor(**self.plans).get_squence()
        return [collumns, rows, plans]

    def insert_function(i,j,k,collumns,rows,plans):
        if k < len(plans):
            self.insert_collumn(i,j,k,plans[k],plans[k+1])
        if j < len(rows) and j =! 0:
            pass
        if i < len(collumns) and i =! 0:
            pass


    def insert(self):
        sequences = self.get_sequences()
        for i,j,k in product(*sequences):
            print('#',i,j,k)
            self.insert_function(i,j,k,*sequences)



if __name__ == '__main__':
    main()
