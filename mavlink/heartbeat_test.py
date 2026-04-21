from pymavlink import mavutil

mav = mavutil.mavlink_connection('/dev/serial0', baud=57600)
print('Waiting for heartbeat...')
mav.wait_heartbeat()
print(f'Heartbeat received! System: {mav.target_system}, Component: {mav.target_component}')
