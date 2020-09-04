#Uses getpass for userautodetection when using default file paths
import getpass
user = getpass.getuser()

#Determines in/out locations for files
answerin = input("Full path to input file:\n")
if answerin == "default":
	if user == "root":
		user = input("What is your username:\n")
	pathin = "/home/%s/Downloads/in.txt"%(user)
else:
        pathin = answerin
answerout = input("Full path to output file\n")
if answerout == "default":
	if user == "root":
		user = input("What is your username:\n")
	pathout = "/home/%s/Downloads/out.txt"%(user)
else:
        pathout = answerout
f=open(pathin, "r")
strings = f.read()
strings = strings.split("\n")

#Removes all brackets and text inside brackets and writes result to new file as determined above
for each in strings:
	search = each
	amount =  search.count("[")
	for i in range(amount):
		bracket1 = search.find("[")
		bracket2 = search.find("]")
		bracket2 = bracket2 + 1
		remove = search[bracket1:bracket2]
		search = search.replace(remove, "")
	y=open(pathout, "a+")
	y.write("%s\n" % (search))
y.close()
f.close()
print("Done!")

