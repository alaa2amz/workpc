from os import name

import wc
import yaml
from itertools import product, zip_longest
from copy import deepcopy

#yaml sample
ys = {}
def main():
    global ys 
    ys = yaml.safe_load(yaml_sample)
    sample = ys
    ##s=Skell(sample)
    #print(s.get_sequences())
    ##s.insert()
    #print(blue)
    #print(color('blue'))
    #rcc = RCC('test',[0,0,0], [0,0,3000],1000)
    #trcc = Shell(rcc,20)
    #trcc.insert()
    tsh=ToriSphEnd('ddd',3000,15)
    tsh.insert()



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

def color(name,sep=' '):
    return sep.join([str(i) for i in list(wc.name_to_rgb(name))])

def mater_plastic(color, transparency=0.0 , reflection=0.0):
    """construct mater command arguments supplied after group.
    mater group "shader" color inherent?
    """
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
yaml_sample =''' #yaml: 
name: ea
location: [0,0,0]
rotation: [0,0,0]

collumns:
  count: 5
  absolutes:
    0: 0
    1: 3000
  offsets:
    default: 2500
    2: 3500

rows:
  count: 7
  absolutes:
    0: 0
    1: 3000
  offsets:
    default: 2500
    2: 3500

plans:
  count: 4
  absolutes:
    0: 0
    1: 4000
  offsets:
    default: 2500
    2: 3500

long_beam:
  total_height: 150
  flange_width: 100
  web_thick: 20
  flange_thick: 10
  rotation: [0,0,0]
  handle: tos
  type: fi

cross_beam:
  total_height: 150
  flange_width: 100
  web_thick: 20
  flange_thick: 10
  rotation: [0, 0, -90]
  handle: tos
  type: fi

post:
  total_height: 150
  flange_width: 100
  flange_thick: 10
  web_thick: 20
  handle: cen
  rotation: [0, 90, 0]
  type: fi

beams:
  0_1_1_v:
    total_height: 150
    flange_width: 100
    web_thick: 20
    flange_thick: 10
    rotation: [0, 90, 0]
    type: fi

margin: 5000
floor_depth: 2000
'''
pv_sample ='''#yaml
name: test
location: [0,0,0] #or cen of 0-1, 
rotation: [0,0,0]
diameter: 2000
length: 2500
thick: -12
end1_thick: -12
end2_thick: -12
supports:
nozzles: 
'''
sample = {
        'name':'ea',
        'location':[0,0,0],
        'rotation':[0,0,0],
        'collumns': {'absolutes': {0:0, 1: 3000}, 'count': 5, 
                     'offsets': {'default':2500, 2: 3500}},
        'rows': {'absolutes': {0:0, 1:3000}, 'count': 7, 
                 'offsets': {'default':2500,2: 3500} },
        'plans': {'absolutes': {0:0,1: 4000}, 'count': 4, 
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
        print(f'in {long_name} rpp {s.xmin} {s.xmax}  {s.ymin} {s.ymax} \
                {s.zmin} {s.zmax}')
        return long_name

class Tor:
    def __init__(self, name, vertex, normal, radius_big, radius):
        self.name = name
        self.vertex = vertex
        self.normal = normal
        self.radius_big = radius_big
        self.radius = radius

    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        vertex_string = ' '.join(map(str,self.vertex))
        normal_string = ' '.join(map(str,self.normal))
        print(f'in {long_name} tor {vertex_string} \
                {normal_string} {self.radius_big} {self.radius}')
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
        print(f'in {long_name} rcc {vertex_string} \
                {vector_string} {self.radius}')
        return long_name


class TRC:
    def __init__(self, name, vertex,vector, radius, radius_top):
        self.name = name
        self.vertex = vertex
        self.vector = vector
        self.radius = radius
        self.radius_top = radius_top
    
    @classmethod
    def fromto(cls,name,from_p ,to_p,radius, radius_top):
        vector = get_vector(from_p, to_p)
        vertex = from_p
        return cls(name, vertex, vector, radius, radius_top) 

    def insert(self, prefix='',suffix='.s'):
        long_name = prefix + self.name + suffix
        vertex_string = ' '.join(map(str,self.vertex))
        vector_string = ' '.join(map(str,self.vector))
        print(f'in {long_name} trc {vertex_string} \
                {vector_string} {self.radius} {self.radius_top}')
        return long_name

class Shell():
    def __init__(self,rcc, thick, ref=0):
        self.name =  rcc.name
        self.thick = thick
        self.ref = 0
        self.inner_rcc = deepcopy(rcc)
        self.inner_rcc.name += '-inner'
        self.outer_rcc = deepcopy(rcc)
        self.outer_rcc.name += '-outer'
        if type(self) == TRC:
            self.trc = True
        else:
            self.trc = False
        if ref == 0:
            self.outer_rcc.radius += thick
            if self.trc:
                self.outer_rcc.radius_base += thick
        elif ref == 1:
            self.inner_rcc.radius -= thick/2
            self.outer_rcc.radius += thick/2
            if self.trc:
                self.inner_rcc.radius_base -= thick/2
                self.outer_rcc.radius_base += thick/2
        elif ref == 2:
            self.inner_rcc.radius -= thick
            if self.trc:
                self.outer_rcc.radius_base -= thick

    def insert(self, prefix='',suffix='.c'):
        long_name = prefix + self.name + suffix
        inner_name = self.inner_rcc.insert()
        outer_name = self.outer_rcc.insert()
        comb_name = print (f'comb {long_name} u {outer_name} - {inner_name}')
        return comb_name


class ToriSphEnd:
    def __init__(self,name,diameter,thick,ref=0):
        self.name = name
        self.diameter = diameter
        self.thick = thick
        self.ref = ref
        self.barrel_height = 3.5 * thick

    def insert(self):
        tori_radius = self.diameter  / 10
        tori_height = ((self.diameter - tori_radius)**2 - (self.diameter/2 -tori_radius)**2)**0.5
        tori_ring_radius = self.diameter/2-tori_radius
        barrel = RCC(self.name+'-barrel',[0,0,0],[0,0,self.barrel_height],self.diameter/2)
        shell_barrel = Shell(barrel,self.thick)
        torus = Tor(self.name+'-tor',[0,0,self.barrel_height],[0,0,1],tori_ring_radius,tori_radius)
        shell_torus = Shell(torus,self.thick)
        sph_z = - self.diameter + self.barrel_height + (self.diameter-tori_height)
        spher = Sph(self.name+'-sph',[0,0,sph_z],self.diameter)
        shell_sph = Shell(spher, self.thick)
        b=shell_barrel.insert()
        t=shell_torus.insert()
        s=shell_sph.insert()
        cutter = RCC(self.name+'-cutter', [0,0,0],[0,0,sph_z+self.thick] ,self.diameter/2 + self.thick)
        c = cutter.insert()
        print(f'comb {self.name}-crud.c u {s} + {c}')
        print(f'comb {self.name}-dish.c u {self.name}-crud.c - {t}')


class IBeam:
    def __init__(self, name, length,
        total_height,
        web_thick,
        flange_thick,
        flange_width,
        location = [0,0,0],
        rotation = [0,0,0],
        handle='cen',
        **kargs):
        """--- --- ---"""
        self.lower_flange = RPP(name + '-lflng',
            0,
            length,
            -flange_width/2,
            flange_width/2,
            0,
            flange_thick)
        self.web = RPP(name + '-web',
            0,
            length,
            -web_thick/2,
            web_thick/2,
            flange_thick,
            total_height - flange_thick) 
        self.upper_flange = RPP(name + '-uflng',
            0,
            length,
            -flange_width/2,
            flange_width/2,
            total_height - flange_thick,
            total_height)
        self.orig = Sph(name+'-o',[0,0,total_height/2], web_thick/2)
        self.tos = Sph(name + '-t' , [0,0,total_height] , web_thick/2)
        self.handle = handle
        self.rotation = rotation
        self.location = location
        self.name = name
        self.solids = [self.lower_flange, self.web, self.upper_flange]
        self.guides = [self.orig, self.tos]

    def insert(self,prefix='',suffix='.c'):
        long_name = prefix + self.name + suffix
        unions = [i.insert() for i in self.solids]
        unions_u_join = ' u '.join(unions)
        addsubs = [i.insert() for i in self.guides]
        addsubs_minus = [ f'{i} - {i}' for i in addsubs ]
        addsubs_u_join = ' u '.join(addsubs_minus)
        print(f'comb {long_name} u {unions_u_join} u {addsubs_u_join}')
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
    extension = 5000

    def __init__(self, data):
        """------"""
        self.extension = Skell.extension
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

        self.nodes = []
        self.vaxs = []
        self.caxs = []
        self.laxs = []
        self.posts = []
        self.bb_posts = []
        self.cbeams = []
        self.bb_cbeams = []
        self.lbeams = []
        self.bb_lbeams = []
        self.sec_plans = []
        self.sec_elevs = []
        self.sec_crosses = []
        self.all_sections = []
        self.whole_box = ''

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
        node_name = node.insert()
        self.nodes.append(node_name)
        if k + 1< self.plans.count :
            name = 'vax-'+ node_name
            from_p = vertex
            to_p = vertex[:]
            to_p[2]= plans[k+1]
            vax=RCC.fromto(name, from_p, to_p, axis_radius)
            vax_name = vax.insert()
            self.vaxs.append(vax_name)
            beam = self.find_beam(i,j,k,2,'p',sequances)
            beam_name,bbox_name = beam.insert()
            self.posts.append(beam_name)
            self.bb_posts.append(bbox_name)
        if j + 1< self.rows.count and k != 0:
            name ='cax-'+ node_name 
            from_p = vertex
            to_p = vertex[:]
            to_p[1]= rows[j+1]
            cax=RCC.fromto(name, from_p, to_p, axis_radius)
            cax_name = cax.insert()
            self.caxs.append(cax_name)
            beam = self.find_beam(i,j,k,1,'c',sequances)
            beam_name,bbox_name = beam.insert()
            self.cbeams.append(beam_name)
            self.bb_cbeams.append(bbox_name)
        if i + 1< self.collumns.count and k != 0:
            name ='lax-'+ node_name 
            from_p = vertex
            to_p = vertex[:]
            to_p[0]= collumns[i+1]
            lax=RCC.fromto(name, from_p, to_p, axis_radius)
            lax_name = lax.insert()
            self.laxs.append(lax_name)
            beam = self.find_beam(i,j,k,0,'l',sequances)
            beam_name,bbox_name =  beam.insert()
            self.lbeams.append(beam_name)
            self.bb_lbeams.append(bbox_name)

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

    def insert_base(self):
        sequences = self.get_sequences()
        base_name = 'base'
        extension = self.extension
        depth = 2000
        max_x = sequences[0][-1] + extension
        max_y = sequences[1][-1] + extension
        min_x = -extension
        min_y = -extension
        base = RPP(base_name,min_x,max_x,min_y,max_y,-depth,0)
        return base.insert()

    def make_sections(self):
        self.sec_plans = []
        self.sec_elevs = []
        self.sec_crosses = []
        sequences = self.get_sequences()
        ext = self.extension
        ext_seqs = []
        for seq in sequences:
            new_seq = [ seq[0]-ext ] + seq + [ seq[-1] + ext ]
            ext_seqs.append(new_seq)
        #print(ext_seqs)
        model_min_x = ext_seqs[0][0] 
        model_max_x = ext_seqs[0][-1] 
        model_min_y = ext_seqs[1][0] 
        model_max_y = ext_seqs[1][-1] 
        model_min_z = ext_seqs[2][0] 
        model_max_z = ext_seqs[2][-1] 
        whole_box=RPP('whole-box',model_min_x, model_max_x, model_min_y, model_max_y, model_min_z,model_max_z)
        self.whole_box = whole_box.insert()
        for i,val in enumerate(ext_seqs[2]):
            if i+1 > len(ext_seqs[2])-1:
                continue
            plan = RPP(
                    f'sec-plan-{i}',
                    model_min_x,model_max_x,
                    model_min_y,model_max_y,
                    val,ext_seqs[2][i+1],
                    )
            plan_name = plan.insert()
            self.sec_plans.append(plan_name)

        for i,val in enumerate(ext_seqs[1]):
            if i+1 > len(ext_seqs[1])-1:
                continue
            elev = RPP(
                    f'sec-elev-{i}',
                    model_min_x, model_max_x,
                    val, ext_seqs[1][i+1],
                    model_min_z, model_max_z,
                    )
            elev_name = elev.insert()
            self.sec_elevs.append(elev_name)


        for i,val in enumerate(ext_seqs[0]):
            if i+1 > len(ext_seqs[0])-1:
                continue
            cross = RPP(
                    f'sec-cross-{i}',
                    val, ext_seqs[0][i+1],
                    model_min_y,model_max_y,
                    model_min_z, model_max_z,
                    )
            cross_name = cross.insert()
            self.sec_crosses.append(cross_name)



    def insert(self):
        sequences = self.get_sequences()
        ranges = self.get_ranges()
        self.nodes = []
        self.vaxs = []
        self.caxs = []
        self.laxs = []
        self.posts = []
        self.cbeams = []
        self.lbeams = []
        for i,j,k in product(*ranges):
            print('#',i,j,k)
            self.insert_function(i,j,k,*sequences)
        base_name = self.insert_base()
        self.make_sections()

        nodes_group = 'node.g'
        vax_group = 'vax.g'
        cax_group = 'cax.g'
        lax_group = 'lax.g'
        post_group = 'post.g'
        bb_post_group = 'bb-post.g'
        cbeam_group = 'cbeam.g'
        bb_cbeam_group = 'bb-cbeam.g'
        lbeam_group = 'lbeam.g'
        bb_lbeam_group = 'bb-lbeam.g'
        ax_group = 'ax.g'
        skell_region = 'skell.r'
        all_group = 'all-skell.g'
        sec_plan_group = 'sec-plan.g'
        sec_elev_group = 'sec-elev.g'
        sec_cross_group = 'sec-cross.g'
        all_sec_c = 'all-sec.g'
        groups={
                nodes_group: self.nodes,
                vax_group: self.vaxs,
                cax_group: self.caxs,
                lax_group: self.laxs,
                post_group: self.posts,
                bb_post_group: self.bb_posts,
                cbeam_group: self.cbeams,
                bb_cbeam_group: self.bb_cbeams,
                lbeam_group: self.lbeams,
                bb_lbeam_group: self.bb_lbeams,
                ax_group: [vax_group, cax_group, lax_group],
                skell_region: [ post_group, cbeam_group, lbeam_group],
                all_group :[skell_region,base_name],
                sec_plan_group: self.sec_plans,
                sec_elev_group: self.sec_elevs,
                sec_cross_group: self.sec_crosses,
                }
        for key,alist in groups.items():
            concated = ' '.join(alist)
            print(f'g {key} {concated}')
        print(f'c -r {skell_region}')
        blue=color('blue')
        print(f'mater {skell_region} "plastic" {blue} 0')
        all_sections = (self.sec_plans+
                       self.sec_elevs+
                       self.sec_crosses)
        for secrpp in all_sections:       
            sec_name = secrpp[:-2]+'.c'
            #print(f'comb {sec_name} u {secrpp} + {all_group}')
            print(f'comb {sec_name} u {all_group} + {secrpp}')
            self.all_sections.append(sec_name)
        concated = ' '.join(self.all_sections)
        print(f'g {all_sec_c} {concated}')
        


                







if __name__ == '__main__':
    main()
