from tixi3 import tixi3wrapper
from tigl3 import tigl3wrapper
from tigl3 import geometry

import tigl3.configuration



def print_point(p):
   print( "(" + str(p.x) + ";" + str(p.y) + ";" + str(p.z) + ")" )
  

def create_round_wing(wings, newWingUid, numberOfSection, diameter,sym):
  # parameters 
  deltaRotX = 180.0  / (numberOfSection - 1.0) 
  firstPosition = geometry.CTiglPoint(0,0,-diameter /2.0);
  firstNormal = geometry.CTiglPoint(0,-1,0);
  rot = geometry.CTiglTransformation();
  
  # create the wing
  wings.create_wing(newWingUid, numberOfSection , "NACA0012");
  wing = wings.get_wing(newWingUid);
  
  wing.set_symmetry(sym)

  
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

  
    
def save(tixi_h, aircraft, filename):
  aircraft.write_cpacs(aircraft.get_uid())
  configAsString = tixi_h.exportDocumentAsString();
  text_file = open(filename, "w")
  text_file.write(configAsString)
  text_file.close()
  
def create_space_shipe():
  tixi_h = tixi3wrapper.Tixi3()
  tigl_h = tigl3wrapper.Tigl3()
  tixi_h.open("Data/simpletest.cpacs.xml")
  tigl_h.open(tixi_h, "")
 
  # get the configuration manager
  mgr =  tigl3.configuration.CCPACSConfigurationManager_get_instance()
  aircraft = mgr.get_configuration(tigl_h._handle.value)
  wing0 = aircraft.get_wing(1);
  sym = wing0.get_symmetry(); 
  wings = aircraft.get_wings(); 
 
  create_round_wing(wings, "roundW", 29, 10,sym); 
  create_round_wing(wings, "roundW2", 13, 7,sym);
  create_round_wing(wings, "roundW3", 3, 8,sym);
  
  wing3 = aircraft.get_wing("roundW3")
  wing3.set_root_leposition(geometry.CTiglPoint(10,0,-4))
  
  save(tixi_h, aircraft, "out-test.xml")
  
  
def main():
  create_space_shipe(); 
  
if __name__ == '__main__':
  main(); 

