from utils import *



def cone(start_dia, end_dia, start_center, end_center, number_of_section):
    delta = (end_center-start_center) * (1/ (number_of_section-1))
    
    centers = points_list_delta(number_of_section, start_center, delta);
    
    normals = points_list_const(number_of_section, geometry.CTiglPoint(1,0,0) )    
    
    delta_h = (end_dia - start_dia)/(number_of_section-1)
    heights = double_list_delta(number_of_section, start_dia, delta_h)
    delta_w = (end_dia - start_dia)/(number_of_section-1)
    widths = double_list_delta(number_of_section, start_dia, delta_w)
    
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

def extend_lists(lists_to_extend, list_to_add):
    # need to be the same length
    c = 0;
    for l in lists_to_extend:
        l.extend(list_to_add[c])
        c = c+1


def get_last_center(parameters):
    return parameters[0][len(parameters[0])-1]
 
