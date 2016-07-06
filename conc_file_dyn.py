import shutil
import time
import subprocess

dst_file = "conc_output"

def file_list():
	filelist = subprocess.check_output(['ls -l config_output | awk -F\' \' \'{ print $9 }\' | sort -n '], shell=True)
	filelist = filelist.split()
	#print filelist
	return filelist
	#print filelist
	#for item in filelist:
	#	print item
    #	print "==item"

def concat():
	# clear out the file
	open("{0}".format(dst_file), 'w').close()
	# open file to append
	with open("{0}".format(dst_file), "a") as base_file:
		for file in file_list():
			print ("starting {0}".format(file))
			with open("config_output/{0}".format(file), "r") as source_file:
					for line in source_file:
						base_file.write(line)
						#print line,
					source_file.close()
	base_file.close()

def main():
	concat()

if __name__ == '__main__':
	main()