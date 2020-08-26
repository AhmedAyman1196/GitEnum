import os , sys , re , subprocess , shlex
from termcolor import colored

# ~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~

def run_command(command):
	res= [] 
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=None)
	while True:
		output = process.stdout.readline()
		if output == b'' and process.poll() is not None:
			break
		if output:
			res.append(output.decode("utf-8").strip())
	rc = process.poll()
	return res

def gitCheck(sub):
	print("checking " , sub)
	command = "python3 /opt/git-dumper/git-dumper.py " +sub+ " ./git/"+sub[8:]
	#print(command)
	res = run_command(command)
	print(colored("-------------","red"))
	# print("--------------\n" , res , "-----------\n")


# ~~~~~~~~~~~~~~~~~~~~~ Argument Check ~~~~~~~~~~~~~~~~~~~~~

# check number of arguments
if len(sys.argv) != 2:
	print(colored("Please Enter only one argument"))
	sys.exit()

print(colored("\n------------------------------", 'red'))
print(colored("Started Git Checking",'green'))
print(colored("------------------------------\n",'red'))

# Reading file 
filename = sys.argv[1]

with open(filename) as f:
    sublist = f.readlines()

for i in sublist:
	i = i.split(" ")
	gitCheck(i[0])





