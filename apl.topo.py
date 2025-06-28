
#!/usr/bin/env python3
from node import *

class apl(Topo):
    def build(self):
        self.add_node("0")
        self.add_node("1")
        self.add_node("2")
        self.add_node("3")
        self.add_node("4")
        self.add_node("5")
        self.add_node("6")
        self.add_node("7")
        self.add_node("8")
        self.add_node("9")
        self.add_node("10")
        self.add_link_name("0", "1", cost=1000, delay=0.2, bw=12000000000000, directed=True)
        self.add_link_name("1", "0", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("1", "2", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("2", "1", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("1", "4", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("4", "1", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("1", "5", cost=10000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("5", "1", cost=10000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("2", "3", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("3", "2", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("2", "5", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("5", "2", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("2", "6", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("6", "2", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("3", "6", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("6", "3", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("4", "5", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("5", "4", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("4", "7", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("7", "4", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("4", "8", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("8", "4", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("5", "6", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("6", "5", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("5", "8", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("8", "5", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("5", "9", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("9", "5", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("6", "9", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("9", "6", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("7", "8", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("8", "7", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("8", "9", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("9", "8", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("9", "10", cost=1000, delay=0.2, bw=12000000000000, directed=True)
        self.add_link_name("10", "9", cost=1000, delay=0.2, bw=12000000000000, directed=True)
    
    def dijkstra_computed(self):
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","8")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {8} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","8")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {8} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","8")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {8} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","8")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {8} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","3")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {3} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 10
        build_str = ""
        self.add_command("0", f"ip -6 route add {{10}} metric 1 table 1 src {{0}}  {build_str}")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {10/} iif lo table 1")
        self.add_command("10", "nuttcp -6 -S")
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R400000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R800000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R1000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R4000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R8000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R10000000 -N32 {10} \>\>flow_0-10.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-10.txt\; done\\\" | at now+2min')

        self.enable_throughput()
        self.add_command("0", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("1", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("2", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("3", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("4", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("5", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("6", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("7", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("8", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("9", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("10", "sysctl net.ipv6.fib_multipath_hash_policy=1")

topos = {'apl': (lambda: apl())}

