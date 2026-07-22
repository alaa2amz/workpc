import itertools
import json
from itertools import product, zip_longest

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

def get_vector(from_point, to_point):
    return [to_c - fro_c for to_c, fro_c in zip_longest(to_point, from_point, fillvalue=0)]

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
    def __init__(self, name, vertex,vector, radius):
        self.name = name
        self.vertex = vertex
        self.vector = vector
        self.radius = radius
    
    @classmethod
    def fromto(cls,name,from_p ,to_p,radius):
        vector = get_vector(from_p, to_p)
        vertex = from_p
        return cls(name, vertex, vector, radius) 

    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        vertex_string = ' '.join(map(str,self.vertex))
        vector_string = ' '.join(map(str,self.vector))
        print(f'in {long_name} rcc {vertex_string} {vector_string} {self.radius}')

class Skell:
    #TODO handle live setter updates
    def __init__(self, data):
        """------"""
        collumns_data = data['collumns']
        rows_data = data['rows']
        plans_data = data['plans']
        self.collumns = SequenceDescriptor(**collumns_data)
        self.rows = SequenceDescriptor(**rows_data) 
        self.plans= SequenceDescriptor(**plans_data)
        self.descriptors = [self.collumns, self.rows, self.plans]
    def get_sequences(self):
        return [ i.get_squence() for i in self.descriptors ]
    def get_ranges(self):
        return [ range(i.count) for i in self.descriptors ]

    def insert_function(self,i,j,k,collumns,rows,plans):
        #TODO: to be moved to top
        node_name = f'node_{i}_{j}_{k}'
        node_radius = 40
        axis_radius = 10
        vertex = [collumns[i], rows[j], plans[k]]
        node = Sph(node_name,vertex,node_radius)
        node.insert()
        if k + 1< self.plans.count :
            name = node_name+ '_vcl'
            from_p = vertex
            to_p = vertex[:]
            to_p[2]= plans[k+1]
            vcl=RCC.fromto(name, from_p, to_p, axis_radius)
            vcl.insert()
            #
            self.insert_collumn(i,j,k,plans)
        if j + 1< self.rows.count and k != 0:
            name = node_name+ '_ccl'
            from_p = vertex
            to_p = vertex[:]
            to_p[1]= rows[j+1]
            vcl=RCC.fromto(name, from_p, to_p, axis_radius)
            vcl.insert()
            #
            self.insert_cross_beam(i,j,k,rows)
        if i + 1< self.collumns.count and k != 0:
            self.insert_long_beam(i,j,k,collumns)
            name = node_name+ '_lcl'
            from_p = vertex
            to_p = vertex[:]
            to_p[0]= collumns[i+1]
            vcl=RCC.fromto(name, from_p, to_p, axis_radius)
            vcl.insert()
            #
            #self.insert_long_beam()

    def insert_collumn(self,i,j,k,plans):
        pass
    def insert_cross_beam(self,i,j,k,rows):
        pass
    def insert_long_beam(self,i,j,k,collumns):
        pass

    def insert(self):
        sequences = self.get_sequences()
        ranges = self.get_ranges()
        for i,j,k in product(*ranges):
            print('#',i,j,k)
            self.insert_function(i,j,k,*sequences)



if __name__ == '__main__':
    main()
