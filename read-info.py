from utils import *


def main():
    
  tigltixi = open_cpacs("Data/simpletest.cpacs.xml")
  tigl_h = tigltixi.pop()
  tixi_h = tigltixi.pop()
  aircraft = get_aircraft(tigl_h)
  print_aircraft_info(aircraft)  
  tigl_h.close()
  tixi_h.close()
  
  
  tigltixi = open_cpacs("Data/concorde.xml")
  tigl_h = tigltixi.pop()
  tixi_h = tigltixi.pop()
  aircraft = get_aircraft(tigl_h)
  print_aircraft_info(aircraft)  
  tigl_h.close()
  tixi_h.close()
 
 
 
if __name__ == '__main__':
  main(); 
