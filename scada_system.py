import pySCADA
import time

# Define the SCADA system
scada_system = pySCADA.SCADASystem()

# Define the electrolyzer unit device
electrolyzer_device = pySCADA.Device('Electrolyzer Unit', 'electrolyzer')

# Define the tags for the electrolyzer unit
tags = [
    pySCADA.Tag('Pressure', 'pressure', 'bar', 0, 100),
    pySCADA.Tag('Flow Rate', 'flow_rate', 'L/min', 0, 100),
    pySCADA.Tag('Temperature', 'temperature', '°C', 0, 100),
    pySCADA.Tag('State', 'state', '', ['idle', 'electrolyzing'])
]

# Add the tags to the device
for tag in tags:
    electrolyzer_device.add_tag(tag)

# Add the device to the SCADA system
scada_system.add_device(electrolyzer_device)

# Define the HMI (Human-Machine Interface) screens
hmi_screens = [
    pySCADA.HMIScreen('Electrolyzer Unit Overview', [
        pySCADA.HMIWidget('Pressure', 'pressure', 'bar'),
        pySCADA.HMIWidget('Flow Rate', 'flow_rate', 'L/min'),
        pySCADA.HMIWidget('Temperature', 'temperature', '°C'),
        pySCADA.HMIWidget('State', 'state', '')
    ]),
    pySCADA.HMIScreen('Electrolyzer Unit Details', [
        pySCADA.HMIWidget('Pressure Trend', 'pressure_trend', 'bar'),
        pySCADA.HMIWidget('Flow Rate Trend', 'flow_rate_trend', 'L/min'),
        pySCADA.HMIWidget('Temperature Trend', 'temperature_trend', '°C')
    ])
]

# Add the HMI screens to the SCADA system
for screen in hmi_screens:
    scada_system.add_hmi_screen(screen)

# Start the SCADA system
scada_system.start()

# Simulate data updates
while True:
    time.sleep(1)
    electrolyzer_device.update_tag_value('Pressure', 50 + (10 * math.sin(time.time())))
    electrolyzer_device.update_tag_value('Flow Rate', 20 + (5 * math.cos(time.time())))
    electrolyzer_device.update_tag_value('Temperature', 30 + (5 * math.sin(time.time())))
    electrolyzer_device.update_tag_value('State', 'electrolyzing' if time.time() % 2 < 1 else 'idle')
