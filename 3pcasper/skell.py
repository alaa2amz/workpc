import itertools
import json
from itertools import product, zip_longest


def main():
    s=Skell(sample)
    #print(s.get_sequences())
    s.insert()


## constants
### colors
blue                = [0, 0, 255]
electric_indigo     = [100, 0, 255]
blue_ribbon         = [0, 100, 255]
alone_in_the_dark   = [0, 0, 100]
#https://colordesigner.io/color-name-finder

### transparency
low_transparency    = 0.3
zero_transparency   = 0.0


def mater_plastic(color, transparency=0.0 , reflection=0.0):
    """construct mater command arguments supplied after group.
    mater group "shader" color inherent?"""
    color_string = ' '.join(map(str,color))
    return f'"plastic {{tr {transparency} re {reflection}}}" {color_string} 0'


### materials
vertical_column_mater   = mater_plastic(blue, low_transparency)
long_beam_mater         = mater_plastic(electric_indigo, low_transparency)
cross_beam_mater        = mater_plastic(alone_in_the_dark, zero_transparency)
base_mater              = mater_plastic(alone_in_the_dark, low_transparency)
boundary_box_color      = mater_plastic(alone_in_the_dark, zero_transparency)


def get_vector(from_point, to_point):
    return [to_c - fro_c for to_c, fro_c in zip_longest(to_point, from_point, fillvalue=0)]

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
    'post': {'flange_thick': 10, 'flange_width': 100, 'handle':
                        'cen', 'rotation': [0, 90, 0], 'total_height': 150, 'type':
                        'fi', 'web_thick': 20},
    'beams': {
        '0_1_1_v': {'flange_thick': 10, 'flange_width': 100, 'rotation':
                              [0, 90, 0], 'total_height': 150, 'type': 'fi',
                              'web_thick': 20},
              },
    'margin': 5000,
    'floor_depth': 2000,
         }

class SequenceDescriptor:
    def __init__(self, count=3, absolutes={0:0}, offsets={'default':3000}):
        #print(count)
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
        return long_name

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
        return long_name

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
        return long_name

class IBeam:
    def __init__(self,name ,length, total_height, web_thick, flange_thick, flange_width, location = [0,0,0],rotation = [0,0,0], handle='cen',**kargs):
        self.lower_flange = RPP(name+'-lflng',0,length,-flange_width/2, flange_width/2, 0,flange_thick)
        self.web = RPP(name + '-web', 0, length,-web_thick/2,web_thick/2 ,flange_thick, total_height - flange_thick) 
        self.upper_flange = RPP(name + '-uflng', 0,length,-flange_width/2, flange_width/2, total_height-flange_thick, total_height)
        self.orig = Sph(name+'-o',[0,0,total_height/2], web_thick/2)
        self.tos = Sph(name + '-t' , [0,0,total_height] , web_thick/2)
        #self.bound_box = RPP(name+'_bb',0, length, -flange_width/2, flange_width/2, 0, total_height)
        self.handle = handle
        self.rotation = rotation
        self.location = location
        self.name = name
        self.solids = [self.lower_flange, self.web, self.upper_flange]
        #self.guides = [self.orig, self.tos, self.bound_box]
        self.guides = [self.orig, self.tos]

    def insert(self,prefix='',suffix='.c'):
        long_name = prefix + self.name + suffix
        unions = [i.insert() for i in self.solids]
        addsubs = [i.insert() for i in self.guides]
        for i in unions:
            print(f'comb {long_name} u {i}')
        for i in addsubs:
            print(f'comb {long_name} u {i} - {i}')
        handle_name=''
        if self.handle == 'cen':
            handle_name = addsubs[0]
        if self.handle == 'tos':
            handle_name = addsubs[1]
        print(f'B {long_name}')
        print(f'oed / {long_name}/{handle_name}')
        location_string = ' '.join(map(str,self.location))
        rotation_string = ' '.join(map(str,self.rotation))
        print(f'rot {rotation_string}')
        print(f'translate {location_string}')
        print(f'accept')
        bound_box_name = long_name.replace('.c','-bb.s',1)
        print(f'bb -c {bound_box_name} {long_name}')
        return long_name, bound_box_name 




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
        self.post = data['post']
        self.long_beam = data['long_beam']
        self.cross_beam = data['cross_beam']
        self.beams = data['beams']
    def get_sequences(self):
        return [ i.get_squence() for i in self.descriptors ]
    def get_ranges(self):
        return [ range(i.count) for i in self.descriptors ]
    def insert_function(self,i,j,k,collumns,rows,plans):
        #TODO: to be moved to top
        sequances=[collumns,rows,plans]
        node_name = f'{i}-{j}-{k}'
        node_radius = 40
        axis_radius = 10
        vertex = [collumns[i], rows[j], plans[k]]
        name = 'node-' + node_name
        node = Sph(name ,vertex,node_radius)
        node.insert()
        if k + 1< self.plans.count :
            name = 'vax-'+ node_name
            from_p = vertex
            to_p = vertex[:]
            to_p[2]= plans[k+1]
            vcl=RCC.fromto(name, from_p, to_p, axis_radius)
            vcl.insert()
            beam = self.find_beam(i,j,k,2,'p',sequances)
            beam.insert()
        if j + 1< self.rows.count and k != 0:
            name ='cax-'+ node_name 
            from_p = vertex
            to_p = vertex[:]
            to_p[1]= rows[j+1]
            ccl=RCC.fromto(name, from_p, to_p, axis_radius)
            ccl.insert()
            beam = self.find_beam(i,j,k,1,'c',sequances)
            beam.insert()
        if i + 1< self.collumns.count and k != 0:
            name ='lax-'+ node_name 
            from_p = vertex
            to_p = vertex[:]
            to_p[0]= collumns[i+1]
            lcl=RCC.fromto(name, from_p, to_p, axis_radius)
            lcl.insert()
            beam = self.find_beam(i,j,k,0,'l',sequances)
            beam.insert()
    def find_beam(self,i,j,k,index,direction_indicator,sequances):
        name=''
        match direction_indicator:
            case 'p':
                name = 'post'
            case 'c':
                name = 'cbeam'
            case 'l':
                name = 'lbeam'
        key = f'{name}-{i}-{j}-{k}'
        dimension_index = [i,j,k][index]
        sequance = sequances[index]
        location = [sequances[0][i],sequances[1][j],sequances[2][k]]
        length = sequance[dimension_index + 1] - sequance[dimension_index] 
        section={}
        if key not in self.beams:
            match direction_indicator:
                case 'p':
                    section = self.post
                case 'c':
                    section = self.cross_beam
                case 'l':
                    section = self.long_beam
        else:
            section = self.beams[key]
        beam = IBeam(name=key,length=length,location=location,**section) # pyright: ignore
        return beam

    def insert(self):
        sequences = self.get_sequences()
        ranges = self.get_ranges()
        for i,j,k in product(*ranges):
            print('#',i,j,k)
            self.insert_function(i,j,k,*sequences)



if __name__ == '__main__':
    main()
