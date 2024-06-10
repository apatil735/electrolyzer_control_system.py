# Import necessary libraries
import pyplc

# Connect to the PLC device
vice.connect()

# Create a data access service to access the process data
data_access_service = IDataAccessService(device)

# Read a single variable
read_item = data_access_service.ReadSingle("Arp.Plc.Eclr/test_in2")
value = read_item.Value.GetValue()
print(f"Value of test_in2: {value}")

# Read multiple variables
read_items = data_access_service.Read(("Arp.Plc.Eclr/test_in1", "Arp.Plc.Eclr/test_in2", ))
read_item1 = read_items[0]
read_item2 = read_items[1]
print(f"Value of test_in1: {read_item1.Value.GetValue()}")
print(f"Value of test_in2: {read_item2.Value.GetValue()}")

# Write data to a variable
write_item = data_access_service.WriteSingle("Arp.Plc.Eclr/test_out1", 10)
print("Wrote value 10 to test_out1")

# Write data to multiple variables
write_items = data_access_service.Write(("Arp.Plc.Eclr/test_out1", "Arp.Plc.Eclr/test_out2", ), (10, 20, ))
print("Wrote values 10 and 20 to test_out1 and test_out2")
