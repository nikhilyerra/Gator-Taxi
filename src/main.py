import sys
import re
from rbtree import RedBlackTree
from minheap import minheap

# Create a RedBlackTree and a minHeap
r = RedBlackTree()
m = minheap()

# Get the input file name from the command line argument
input_file_name = sys.argv[1]

# Open the input and output files
with open(input_file_name, 'r') as input_file, open('output_file.txt', 'w') as output_file:
  
  # Process each line in the input file
  for line in input_file:
    
    # Extract the arguments from the line
    args = re.findall('\((.*?)\)', line)
    
    if "Insert" in line:
      # Parse the arguments
      rn, rc, td = [int(arg) if arg.isdigit() else arg for arg in args[0].split(',')]

      # Insert the data into the RedBlackTree and the minHeap
      for insert_func in [m.insert, r.insert]:
        error = insert_func(rn, rc, td)
        if error:
          # If there's an error, print it and write it to the output file, then exit
          print(error)
          output_file.write(error)
          sys.exit(0)

    elif "GetNextRide" in line:
      # Get the next ride from the minHeap
      next_ride = m.GetNextRide()

      if next_ride:
        # If there's a next ride, delete it from the RedBlackTree and print and write its details
        ride_id, ride_start, ride_end = next_ride
        r.delete(ride_id)
        ride_details = (ride_id, ride_start, ride_end)
        print(ride_details)
        output_file.write(f"{ride_details}\n")
      else:
        # If there's no next ride, print and write a message
        no_rides_msg = "No active ride requests"
        print(no_rides_msg)
        output_file.write(f"{no_rides_msg}\n")

    elif "UpdateTrip" in line:
      # Parse the arguments
      rn, new_td = [int(arg) if arg.isdigit() else arg for arg in args[0].split(',')]

      # Update the trip in both the minHeap and the RedBlackTree
      m.updateTrip(rn, new_td)
      r.UpdateTrip(rn, new_td)

    elif "CancelRide" in line:
      # Parse the ride number from the arguments
      ride_num = int(args[0])

      # Cancel the ride in both the minHeap and the RedBlackTree
      m.cancelRide(ride_num)
      r.delete(ride_num)

  


    elif "Print" in line:
      printargs = [
        int(arg) if arg.isdigit() else arg for arg in args[0].split(',')
      ]
      if len(printargs) == 1:
        node = r.search(printargs[0])
        if node == r.NIL:
          print((0, 0, 0))
          output_file.write("(0, 0, 0)\n")
        else:
          print((node.rn, node.rc, node.td))
          output_file.write(str((node.rn, node.rc, node.td)) + '\n')
      else:
        nodes = r.Print(printargs[0], printargs[1])
        if len(nodes) == 0:
          output_file.write("(0, 0, 0)\n")
        else:
          print(nodes)
          outline = ",".join(str(node) for node in nodes)
          output_file.write(outline + '\n')
