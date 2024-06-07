import XPlaneUdp as xplib
import time
import struct



def set_failure():
    xp = xplib.XPlaneUdp()
    xp.defaultFreq = 10

    # Find the IP of the X-Plane server
    beacon = xp.FindIp()
    print(beacon)
    if not beacon:
        print("X-Plane server not found.")
        return

    
    # Set the tire failure data reference
    failure_dataref = "sim/operation/failures/rel_tire1"
    failure_dataref_wing_1r = "sim/cockpit2/controls/flap_ratio"
    failure_dataref_wing_2r = "sim/operation/failures/rel_ail_R"
    failure_value = 1
    weather_value = 2
    
    # Use WriteDataRef to set the tire failure
    xp.WriteDataRef(failure_dataref, failure_value, vtype='int')
    print(f"Set {failure_dataref} to {failure_value}")

    xp.WriteDataRef(failure_dataref_wing_1r, failure_value, vtype='int')
    print(f"Set {failure_dataref_wing_1r} to {weather_value}")

    xp.WriteDataRef(failure_dataref_wing_2r, failure_value, vtype='int')
    print(f"Set {failure_dataref_wing_2r} to {failure_value}")

   

if __name__ == "__main__":
    set_failure()
