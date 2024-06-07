import XPlaneUdp as xplib
import time

def continuously_print_airspeed():
    xp = xplib.XPlaneUdp()
    xp.defaultFreq = 10

    # Find the IP of the X-Plane server
    beacon = xp.FindIp()
    print(beacon)
    if not beacon:
        print("X-Plane server not found.")
        return

    # Add the airspeed data reference
    xp.AddDataRef("sim/flightmodel/position/indicated_airspeed", freq=10)
    xp.AddDataRef("sim/flightmodel/wing/aileron1_deg", freq=10)


    try:
        # Continuously print the indicated airspeed
        while True:
            values = xp.GetValues()
            airspeed = values.get("sim/flightmodel/position/indicated_airspeed", None)
            aileron = values.get("sim/flightmodel/wing/aileron1_deg", None)
            if airspeed is not None:
                print(f"Indicated Airspeed: {airspeed}")
                print(f"Aileron left: {aileron}")

            else:
                print("Indicated Airspeed data not available.")
            time.sleep(1)  # Sleep for a second before the next fetch
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("Exiting...")
    finally:
        # Cleanup
        xp = None

if __name__ == "__main__":
    continuously_print_airspeed()


#sim/operation/failures/rel_tire1