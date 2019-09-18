from utils import *



def shape_fuselage(fuselage, centers, normals, heights, width):
    
    # set the wing section elements  
    for idx  in range(0,fuselage.get_section_count()) :
        
        s = fuselage.get_section(idx+1);
        e = s.get_section_element(1);
        ce = e.get_ctigl_section_element();
        
        ce.set_center(centers[idx]);
        ce.set_normal(normals[idx]); 
        ce.set_height(heights[idx])
        ce.set_width(width[idx])


def noose_std():
    number_of_section = 7; 
    centers = points_list_delta(number_of_section);
    centers[0] = geometry.CTiglPoint(0,0,-0.4)
    centers[1] = geometry.CTiglPoint(0.1,0,-0.4)
    centers[2] = geometry.CTiglPoint(0.4,0,-0.36)
    centers[3] = geometry.CTiglPoint(0.9,0,-0.09)
    centers[4] = geometry.CTiglPoint(1.6,0,0)
    centers[5] = geometry.CTiglPoint(1.8,0,0)
    centers[6] = geometry.CTiglPoint(2,0,0)
   

    normals = points_list_const(number_of_section, geometry.CTiglPoint(1,0,0) )    
  
    heights = double_list_const(number_of_section,2)
    heights[0] = 0;     
    heights[1] = 0.6;
    heights[2] = 1
    heights[3] = 1.7
    
    widths = double_list_const(number_of_section,2)
    widths[0] = 0; 
    widths[1] = 0.6
    widths[2] = 1
    widths[3] = 1.7
    
    return [centers, normals, heights, widths];
    
def middle_cylinder(last_center, length):
    number_of_section = 3;
    delta = geometry.CTiglPoint(length/number_of_section,0,0);
    centers = points_list_delta(number_of_section, last_center + delta, delta );
    normals = points_list_const(number_of_section, geometry.CTiglPoint(1,0,0) )    
    heights = double_list_const(number_of_section, 2.0)
    widths = double_list_const(number_of_section, 2.0)
    
    return [centers, normals, heights, widths];

def tail_std(last_center, length):
    
    start_dia = 2;
    end_dia  = 0.5; 
    number_of_section = 6; 
    final_center_z = (start_dia/2 - end_dia) + (end_dia/2)
    delta_center_x = length/(number_of_section-1)
    delta_center_z = final_center_z/(number_of_section-2) # we do not translate in z the first tail section 
    delta = geometry.CTiglPoint(delta_center_x,0,delta_center_z)
    centers = points_list_delta(number_of_section, last_center + geometry.CTiglPoint(delta_center_x,0, 0) , delta);
    
    normals = points_list_const(number_of_section, geometry.CTiglPoint(1,0,0) )    
    
    delta_h = (start_dia -end_dia)/(number_of_section-1)
    heights = double_list_delta(number_of_section, start_dia, -delta_h)
    delta_w = (start_dia - end_dia)/(number_of_section-1)
    widths = double_list_delta(number_of_section, start_dia, -delta_w)
    
    return [centers, normals, heights, widths];
        
        
def tail_std2(last_center, length):
    
    start_dia = 2;
    end_dia  = 0.5; 
    number_of_section = 6; 
    final_center_z = (start_dia/2 - end_dia) + (end_dia/2)
    delta_center_x = length/number_of_section
    delta_center_z = final_center_z/number_of_section # we do not translate in z the first tail section 
    delta = geometry.CTiglPoint(delta_center_x,0,delta_center_z)
    centers = points_list_delta(number_of_section, last_center + delta, delta);
    
    normals = points_list_const(number_of_section, geometry.CTiglPoint(1,0,0) )    
    
    delta_h = (start_dia -end_dia)/number_of_section
    heights = double_list_delta(number_of_section, start_dia -delta_h , -delta_h)
    delta_w = (start_dia - end_dia)/number_of_section
    widths = double_list_delta(number_of_section, start_dia -delta_w, -delta_w)
    
    return [centers, normals, heights, widths];
        
def points_list_const(number_of_points, init_point = geometry.CTiglPoint(0,0,0)):
    l = [] 
    for i in range(0, number_of_points):
         l.append(init_point);
    return l


        
def points_list_delta(number_of_points, start_point = geometry.CTiglPoint(0,0,0), delta = geometry.CTiglPoint(1,0,0) ):
    l = [] 
    temp = start_point; 
    for i in range(0, number_of_points):
         l.append(temp);
         temp = temp + delta;
    return l


def double_list_const(number_of_points, init_double = 1.0):
    l = [] 
    for i in range(0, number_of_points):
         l.append(init_double);
    return l

def double_list_delta(number_of_points, strat_d, delta_d):
    l = [] 
    for i in range(0, number_of_points):
         l.append(strat_d + (i * delta_d ));
    return l


def main():
    tigltixi = open_cpacs("Data/empty.cpacs3.xml")
    tigl_h = tigltixi[0]
    tixi_h = tigltixi[1]
    
    aircraft = get_aircraft(tigl_h)
    fuselages = aircraft.get_fuselages()
    wings = aircraft.get_wings()
    
    
    centers = []
    normals = []
    heights = []
    widths = []
    
    ret = noose_std()
    centers.extend(ret[0])
    normals.extend(ret[1])
    heights.extend(ret[2])
    widths.extend(ret[3])
    
    ret = middle_cylinder(centers[len(centers)-1], 9)
    centers.extend(ret[0])
    normals.extend(ret[1])
    heights.extend(ret[2])
    widths.extend(ret[3])
    
    ret = tail_std2(centers[len(centers)-1], 2);
    centers.extend(ret[0])
    normals.extend(ret[1])
    heights.extend(ret[2])
    widths.extend(ret[3])
    
    print("centers:")
    for p in centers:
        print_point(p)
        
    print("normals:")
    for p in normals:
        print_point(p)
        
    print("heights:")
    for d in heights:
        print(d)
        
    print("widths:")
    for d in widths:
        print(d)
        
   
    section_count = len(centers)
    print("requiered number of section: " + str(section_count))
    
    fuselages.create_fuselage("mainFuselage", section_count, "fuselageCircleProfileuID")  
        
   
    shape_fuselage(fuselages.get_fuselage("mainFuselage"), centers, normals, heights, widths)
    
    save(tixi_h, aircraft, "out-test.xml")
        
    tigl_h.close()
    tixi_h.close()

    
     
     

if __name__ == '__main__':
    main(); 
