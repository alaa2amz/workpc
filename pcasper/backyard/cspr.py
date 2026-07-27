import itertools
import json
from itertools import product

def main():
    s=Skell(sample)
    print(s.get_sequences())
    s.insert()

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
sample = {
    'collumns': {
        'absolutes': {0:0, 1: 3000}, 
        'count': 3, 
        'offsets': {'default':2500, '2': 3500},
                },
    'rows': {
        'absolutes': {0:0, 1:3000}, 
        'count': 3, 
        'offsets': {'default':2500,2: 3500},
            },
    'plans': {
        'absolutes': {0:0,1: 7000}, 
        'count': 3, 
        'offsets': {'default':2500, 2: 3500},
              },
    'long_beam': {
                  'flange_thick': 10, 
                  'flange_width': 100,
                  'handle': 'tos',
                  'rotation': [0, 0, 0], 
                  'total_height': 150, 
                  'type': 'fi',
                  'web_thick': 20,
                   },
    'cross_beam': {
                  'flange_thick': 10, 
                  'flange_width': 100, 
                  'handle': 'tos',
                  'rotation': [0, 0, -90], 
                  'total_height': 150, 
                  'type': 'fi',
                  'web_thick': 20,
                   },
    'vertical_column': {
        'flange_thick': 10, 
        ' flange_width': 100, 
        'handle': 'cen', 
        'rot': [0, 90, 0], 
        'total_height': 150, 
        'type': 'fi', 
        'web_thick': 20,
                        },
    'beams': {
                (0,1,1,'vertical'): 
                    {
                     'flange_thick': 10, 
                     'flange_width': 100, 
                     'rot': [0, 90, 0], 
                     'total_height': 150, 
                     'type': 'fi', 
                     'web_thick': 20,
                     },
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


class Sph:
    def __init__(self,name,vertex,radius):
        self.name = name
        self.vertex = vertex
        self.radius = radius
    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        vertex_string = ' '.join(map(str,self.vertex))
        print(f'in {long_name} sph {vertex_string} {self.radius}')

class RPP:
    def __init__(self,name,xmin,xmax,ymin,ymax,zmin,zmax):
        self.name = name
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        s=self
        print(f'in {long_name} rpp {s.xmin} {s.xmax}  {s.ymin} {s.ymax} {s.zmin} {s.zmax}')

class RCC:
    def __init__(self,name ,vertex, vector, radius):
        self.name = name
        self.vertex = vertex
        self.vector = vector
        self.radius = radius
    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        vertex_string = ' '.join(map(str,self.vertex))
        vector_string = ' '.join(map(str,self.vector))
        print(f'in {long_name} rcc {vertex_string} {vector_string} {self.radius}')
        
class Beam():
    def __init__()
class Skell:
    #TODO handle live setter updates
    def __init__(self, data):
        self.collumns={}
        self.rows={}
        self.plans={}
        for key in data:
            setattr(self, key, data[key])
    
    def get_sequences(self):
        collumns = SequenceDescriptor(**self.collumns).get_squence()
        rows = SequenceDescriptor(**self.rows).get_squence()
        plans = SequenceDescriptor(**self.plans).get_squence()
        return [collumns, rows, plans]

    def insert_function(self,i,j,k,collumns,rows,plans):
        node_name = f'node_{i}_{j}_{k}'
        node_radius = 250
        node = Sph(node_name,[i,j,k],node_radius)
        node.insert()
        if k < len(plans):
            self.insert_collumn(i,j,k,plans)
        if j < len(rows) and j != 0:
            self.insert_cross_beam(i,j,k,rows)
        if i < len(collumns) and i != 0:
            self.insert_long_beam(i,j,k,collumns)

    def insert_collumn(self,i,j,k,plans):
        pass
    def insert_cross_beam(self,i,j,k,rows):
        pass
    def insert_long_beam(self,i,j,k,collumns):
        pass

    def insert(self):
        sequences = self.get_sequences()
        for i,j,k in product(*sequences):
            print('#',i,j,k)
            self.insert_function(i,j,k,*sequences)



if __name__ == '__main__':
    main()
