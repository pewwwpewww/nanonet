#!/usr/bin/env python3
import json
from subprocess import run, PIPE
from os import mkdir, chdir
from shutil import copy2
from sys import stdout, stderr, exit
from time import sleep

OUTPUT_FILE = '../batch_result.csv'

class Tests:
	def __init__(self):
		self.TESTFILES = ["TE_Joint.topo.sh", "TE_Weight.topo.sh", "TE_Waypoints.topo.sh"]
		self.TEST_ID = 0
		self.is_in_test = False
		self.TIME = 300
		self.DEMAND_FACTOR = 10000
		self.BYTES_TO_KBITS = 125
		self.CAPACITY = 100

	def create_test_case(self, test_name : str):
		self.TEST_ID = self.TEST_ID + 1
		self.is_in_test = True
		# Create new folder
		# Copy file there
		folder_name = str(self.TEST_ID) + "_" + test_name
		print("\nCreate test case "+folder_name)
		mkdir(folder_name)
		copy2(test_name, folder_name+"/")
		copy2("./throughput.py", folder_name + "/")
		chdir(folder_name)

	def run_test_case(self, test_name : str):
		if not self.is_in_test:
			stderr.write("ERROR in run_test_case: Not in a testcase. " + test_name)
			exit(1)
		# 1 Start scripts
		# One script takes about 5 minutes. But we wait 10, just to be sure ...
		print("Start script "+test_name)
		p = run(['at', 'now', '+', '1', 'minute'],
					stdout=PIPE,
					stderr=PIPE,
					input='./'+test_name+' >>'+str(self.TEST_ID)+"_"+test_name+".log",
					encoding='ascii')
		print(f"Process test {self.TEST_ID} returned with {p.returncode}.")
		with open(str(self.TEST_ID)+"_"+test_name+".log", "a") as logfile:
			print(p.stdout, file=logfile)
			print(p.stderr, file=logfile)

		# Wait 8 minutes so that all tests are finished ...
		sleep(8 * 60)
		print("Test should be finished ...")

	def finish_test_case(self, test_name : str):
		if not self.is_in_test:
			stderr.write("ERROR in run_test_case: Not in a testcase. " + test_name)
			exit(1)

		# Kill dead processes, if any ...
		p = run(['pkill', '-9', '-f', 'nuttcp'],
				stdout=PIPE,
				stderr=PIPE)
		with open(str(self.TEST_ID) + "_" + test_name+".log", "a") as logfile:
			print("\nKill all nuttcp commands", file=logfile)
			print(p.stdout, file=logfile)
			print(p.stderr, file=logfile)

		print("Stop script " + test_name)
		p = run(['bash', './'+test_name, '--stop'],
				stdout=PIPE,
				stderr=PIPE)
		print(f"Process test {self.TEST_ID} STOP returned with {p.returncode}.")
		with open(str(self.TEST_ID) + "_" + test_name+".log", "a") as logfile:
			print(p.stdout, file=logfile)
			print(p.stderr, file=logfile)

	def end_of_test(self):
		chdir("..")
		self.is_in_test = False

	@staticmethod
	def get_all_if_names(script_filename : str):
		MIN_NODE = 0
		MAX_NODE = 8
		interfaces = {}
		# query interface names
		for i in range(MIN_NODE,MAX_NODE+1):
			for j in range(MIN_NODE,MAX_NODE+1):
				process1 = run(
					['bash', script_filename, '--query', f'ifname ({i},{j}) at {i}'],
					stdout=PIPE)
				process2 = run(
					['bash', script_filename, '--query', f'ifname ({i},{j}) at {j}'],
					stdout=PIPE)
				ifname1 = process1.stdout.strip().decode('ascii')
				ifname2 = process2.stdout.strip().decode('ascii')
				interfaces[str(i) + "->" + str(j)] = ifname1
				interfaces[str(j) + "->" + str(i)] = ifname2
		return interfaces

	@staticmethod
	def parse_throughput_files():
		array = []
		for i in range(0,8+1):
			with open(f'{i}.throughput.json') as throughputfile:
				throughput1 = json.load(throughputfile)
				array.append(throughput1)
		return array

	def find_maximum_valid_recv_bytes(self, array, interfaces):
		max = 0.0
		for subarray in array:
			for interface_throughput in subarray:
				if interface_throughput in interfaces.values():
					if subarray[interface_throughput]['recv_bytes']/(self.CAPACITY*self.TIME*self.DEMAND_FACTOR*self.BYTES_TO_KBITS) > max:
						max = subarray[interface_throughput]['recv_bytes']/(self.CAPACITY*self.TIME*self.DEMAND_FACTOR*self.BYTES_TO_KBITS)
		return max

	def get_results(self, test_name):
		interfaces_names = self.get_all_if_names(test_name)
		throughput_files = self.parse_throughput_files()
		max = self.find_maximum_valid_recv_bytes(throughput_files, interfaces_names)
		return max


tests = Tests()
for i in range(1,101):
	for script in tests.TESTFILES:
		tests.create_test_case(script)
		tests.run_test_case(script)
		tests.finish_test_case(script)

		max = str(tests.get_results(script))
		print("MAX="+max)
		with open(OUTPUT_FILE, "a") as result_file:
			print(tests.TEST_ID,';',script,';',max,file=result_file)

		tests.end_of_test()