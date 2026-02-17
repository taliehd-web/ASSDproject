import os
import time

print("=== ASSD Smoke Detection System Demo (Updated from Github Pt2)===")
print("Running on Raspberry Pi")
print()

# Get CPU temperature
temp = os.popen("vcgencmd measure_temp").readline()
print("CPU Temperature:", temp)

print("Starting system heartbeat...\n")

for i in range(5):
    print(f"System Active - Cycle {i+1}")
    time.sleep(1)

print("\nSystem operational. Ready for sensor integration.")
