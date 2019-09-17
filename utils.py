
from tixi3 import tixi3wrapper
from tigl3 import tigl3wrapper
from tigl3 import geometry

import tigl3.configuration

def open(filename):
  
  tixi_h = tixi3wrapper.Tixi3()
  tigl_h = tigl3wrapper.Tigl3()
  tixi_h.open(filename)
  tigl_h.open(tixi_h, "")
  return tigl_h
  
   
def save(aircraft, filename):
  aircraft.write_cpacs(aircraft.get_uid())
  tixi_h = aircraft.get_tixi_document_handle; 
  configAsString = tixi_h.exportDocumentAsString();
  text_file = open(filename, "w")
  text_file.write(configAsString)
  text_file.close()
   
  
def get_aircraft(tigl_h):

  mgr =  tigl3.configuration.CCPACSConfigurationManager_get_instance()
  aircraft = mgr.get_configuration(tigl_h._handle.value)

  return aircraft  
  
  
def print_point(p):
   print( "(" + str(p.x) + ";" + str(p.y) + ";" + str(p.z) + ")" )
  
  
def print_aircraft_info(aircraft):
  print("aircraft: " + aircraft.get_uid())
  print("  wing count: " + str(aircraft.get_wing_count() ) );
  print("  fuselage count: " + str(aircraft.get_fuselage_count() ));
   

def main():
  tigl_h1 = open("Data/simpletest.cpacs.xml")
  aircraft1 = get_aircraft(tigl_h1)
  print_aircraft_info(aircraft1)  
  
  tigl_h2 = open("Data/concorde.xml")
  aircraft2 = get_aircraft(tigl_h2)
  print_aircraft_info(aircraft2)  
 
 
if __name__ == '__main__':
  main(); 

