from utils import *
from list_utils import*

# set centers, normals, heights, widths of fuselage
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


def nose_std():
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



def nose_sharp(length):
    start_dia = 0;
    end_dia  = 2; 
    start_center = geometry.CTiglPoint(0,0,0);
    end_center = geometry.CTiglPoint(length,0,0);
    
    return cone(start_dia,end_dia, start_center, end_center,6);
    
        
    
def middle_cylinder(last_center, length):
    number_of_section = 4;
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

    start_center= last_center+ geometry.CTiglPoint(1,0,0); 
    final_center_z = (start_dia/2 - end_dia) + (end_dia/2)
    end_center= last_center + geometry.CTiglPoint(length, 0,final_center_z);

    return cone(start_dia,end_dia, start_center, end_center, number_of_section)





def create_std_fuselage(aircraft,uid):
    fuselages = aircraft.get_fuselages()
   
    # parameters of the form centers, nomrals, heights, widths   
    parameters = nose_std()
    
    ret = middle_cylinder(get_last_center(parameters), 9)
    extend_lists(parameters, ret);
    
    ret = tail_std(get_last_center(parameters), 3.5);
    extend_lists(parameters, ret);
   
    section_count = len(parameters[0])
    print("requiered number of section: " + str(section_count))
    
    fuselages.create_fuselage(uid, section_count, "fuselageCircleProfileuID")  
    shape_fuselage(fuselages.get_fuselage(uid), parameters[0], parameters[1], parameters[2], parameters[3])
    

def create_space_ship_fuselage(aircraft,uid):
    
    cone_length =4
    
    fuselages = aircraft.get_fuselages()
    
    # parameters of the form centers, nomrals, heights, widths   
    parameters = nose_sharp(cone_length)
    
    ret = middle_cylinder(get_last_center(parameters), 9)
    extend_lists(parameters, ret);
    
    start_center= get_last_center(parameters)+ geometry.CTiglPoint(1,0,0); 
    end_center= start_center + geometry.CTiglPoint(cone_length, 0,0);
    ret = cone(2,0, start_center, end_center, 6)
    extend_lists(parameters, ret);
   
    section_count = len(parameters[0])
    print("requiered number of section: " + str(section_count))
    
    fuselages.create_fuselage(uid, section_count, "fuselageCircleProfileuID")  
    shape_fuselage(fuselages.get_fuselage(uid), parameters[0], parameters[1], parameters[2], parameters[3])
    
   
def main():
    tigltixi = open_cpacs("Data/empty.cpacs3.xml")
    tigl_h = tigltixi[0]
    tixi_h = tigltixi[1]
    
    aircraft = get_aircraft(tigl_h)
    
    create_std_fuselage(aircraft, "mainFuselage"); 
    create_space_ship_fuselage(aircraft, "mainFuselageShip");
    
    save(tixi_h, aircraft, "out-test.xml")
        
    tigl_h.close()
    tixi_h.close()

    
     
     

if __name__ == '__main__':
    main(); 
