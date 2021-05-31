
import json
import math
from sys import stderr, argv, exit

# Factors for align the comma values of the JSON file
WEIGHT_FACTOR   =   1000
CAPACITY_FACTOR = 10000000
DEMAND_FACTOR   = 10000000
# Please note: CAPACITY_FACTOR and DEMAND_FACTOR should ALWAYS be the same value!!!
if CAPACITY_FACTOR != DEMAND_FACTOR:
    stderr.write("WARNING: CAPACITY_FACTOR does not match DEMAND_FACTOR!")



# CONVERT TO OCTAVE function
# This snipped extracts the demands in the JSON file to a matrix, readable in Octave or Matlab
if len(argv) >= 2 and argv[1] == "--octave":
    filename = "/dev/stdin"
    if len(argv) == 3:
        filename = argv[2]
    # Parse JSON file
    with open(filename) as json_file:
        data = json.load(json_file)

    for demand in data["demands"]:
        print(f'D({demand["src"] + 1},{demand["dst"] + 1}) = {int(demand["demand_size"] * DEMAND_FACTOR)};')

    exit(0)
# END CONVERT TO OCTAVE function


filename = "/dev/stdin"
topo_name = "Thomas"
if len(argv) >= 2:
    filename = argv[1]
if len(argv) >= 3:
    topo_name = argv[2]

nodes = []
destination_nodes = []

# Parse JSON file
with open(filename) as json_file:
    data = json.load(json_file)

output = f"""
#!/usr/bin/env python
from node import *

class {topo_name}(Topo):
    def build(self):
"""

# Get all node names and create the nodes
for node in data["links"]:
    nodes.append(node["i"])
    nodes.append(node["j"])
nodes = list(set(nodes))

# get destinations
for node in data["demands"]:
    destination_nodes.append(node["dst"])
destination_nodes = list(set(destination_nodes))

for n in nodes:
    output += \
f"""\
        self.add_node("{n}")
"""

# Make edges unidirectional
# as required from nanonet
for edge1 in data["links"]:
    for edge2 in data["links"]:
        if( edge1["i"] == edge2["i"] and edge1["j"] == edge2["j"] ):
            continue
        if(edge1["i"] == edge2["j"] and edge1["j"] == edge2["i"]):
            # TODO: Remove round()
            if(round(edge1["weight"]) != round(edge2["weight"]) or edge1["capacity"] != edge2["capacity"]):
                raise Exception(f'Wrong input format -- link {edge1["i"]} -- {edge2["j"]} -- properties differ.')
            data["links"].remove(edge2)

for edge in data["links"]:
    output += \
f"""\
        self.add_link_name("{edge["i"]}", "{edge["j"]}", cost={math.ceil(edge["weight"]*WEIGHT_FACTOR)}, delay=0.2, bw={edge["capacity"]*CAPACITY_FACTOR})
"""

output += \
f"""\
    
    def dijkstra_computed(self):
"""
# Create routes out of the demands
for routes in data["demands"]:
    segs = ""
    # We do not want the last element
    for s in routes["segments"][1:-1]:
        segs += f"{{{s}}},"
    if len(routes["segments"]) >= 2:
        if routes['segments'][-1] == routes["dst"]:
            segs += f"{{{routes['segments'][-2]}}}"
        else:
            segs += f"{{{routes['segments'][-1]}}}"
    if segs:
        output += \
f"""\
        # Demand from {routes["src"]} to {routes["dst"]}
        self.add_command("{routes["src"]}", "ip -6 route add {{{routes["dst"]}}} {f'encap seg6 mode encap segs {segs}' if segs else ''} via "+self.get_dijkstra_route_by_name("{str(routes["src"])}","{str(routes['segments'][0])}")[0].nh+" metric 1 src {{{routes["src"]}}}")
"""

# Start nuttcp at destination nodes
for n in destination_nodes:
    output += \
f"""\
        self.add_command("{n}", "nuttcp -6 -S")
"""
for demand in data["demands"]:
    output += \
f"""\
        self.add_command("{demand["src"]}", 'echo bash -c \\\\\\\"START=\\\\\\\\\\$SECONDS\; while \! ip netns exec {demand["src"]} nuttcp -T300 -i1 -R{int(demand["demand_size"]*DEMAND_FACTOR)} {{{demand["dst"]}}} \>\>flow-{demand["src"]}-{demand["dst"]}.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\\\\\\$SECONDS \>\>flow-{demand["src"]}-{demand["dst"]}.txt\; done\\\\\\\" | at now+2min')
"""

output += """
        self.enable_throughput()
"""

output += f"""
topos = {{'{topo_name}': (lambda: {topo_name}())}}
"""

print(output)