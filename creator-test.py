from utils import *


def create_round_wing(wings, newWingUid, numberOfSection, diameter,sym):
  # parameters 
  deltaRotX = 180.0  / (numberOfSection - 1.0) 
  firstPosition = geometry.CTiglPoint(0,0,-diameter /2.0);
  firstNormal = geometry.CTiglPoint(0,-1,0);
  rot = geometry.CTiglTransformation();
  
  # create the wing
  wings.create_wing(newWingUid, numberOfSection , "NACA0012");
  wing = wings.get_wing(newWingUid);  
  wing.set_symmetry(tigl3.core.TIGL_X_Z_PLANE)

  # set the wing section elements  
  for idx  in range(1,wing.get_section_count() + 1) :
    rotX = (idx - 1) * deltaRotX;
    rot.set_identity(); 
    rot.add_rotation_x(rotX); 
    
    p = rot.transform(firstPosition);
    n = rot.transform(firstNormal); 
      
    s = wing.get_section(idx);
    e = s.get_section_element(1);
    ce = e.get_ctigl_section_element();
      
    ce.set_center(p);
    ce.set_normal(n); 
    if rotX >= 90:
      ce.set_rotation_around_normal(180); 


    



def main():
  tigltixi = open_cpacs("Data/empty.cpacs.xml")
  tigl_h = tigltixi[0]
  tixi_h = tigltixi[1]
  aircraft = get_aircraft(tigl_h)
  
  print_aircraft_info(aircraft)  
  wing0 = aircraft.get_wing(1);
  sym = wing0.get_symmetry();
  help(wing0)
  help(wing0.get_symmetry)
  print("sym: " + str(sym) )
  print("sym-type:" + str(type(sym)))
  
  
  wings = aircraft.get_wings(); 
    
  create_round_wing(wings, "roundW", 29, 10,sym); 
  create_round_wing(wings, "roundW2", 13, 7,sym);
  create_round_wing(wings, "roundW3", 3, 8,sym);


  wing3 = aircraft.get_wing("roundW3")
  wing3.set_root_leposition(geometry.CTiglPoint(10,0,-4))
    
  save(tixi_h, aircraft, "out-test.xml")
    

  tigl_h.close()
  tixi_h.close()

  

if __name__ == '__main__':
  main(); 

