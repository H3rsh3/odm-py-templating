import pandas as pd
import numpy as np
import shutil
import fileinput
import sys
import time
import subprocess


class Import_conf():

	def __init__(self,i_data,i_base):
		self.i_data = i_data
		self.i_base = i_base

	def generate_ic(self):
		#--import config_data file
		config_data = pd.read_csv("{0}".format(self.i_data), index_col='host')
		#--get the list of all hosts#
		# create ouput dir
		mkdir_o = subprocess.Popen("mkdir {0}_output".format(self.i_base), shell=True)
		# wilt untill dir is created
		mkdir_ow = mkdir_o.communicate()[0]
		xhostconfig_hosts = config_data.index
		for host in xhostconfig_hosts:
			print "generating config for {0}".format(host)
			#--geenerate a copy of a the base file
			shutil.copy2("{0}".format(self.i_base), "{0}_output/{1}".format(self.i_base,host))
			#--get the row for the host, ie the host to genereate conig for
			xhostconfig = config_data.loc["{0}".format(host)]
			#--get the columns of the host, ie the items to replace
			xhostconfig_item = config_data.columns
			#--for each config_item(column) replace the config file
			for config_item in xhostconfig_item:
				#--get the "find" item to replace
				replace_item = config_item
				#--get the replacement value
				replace_item_with = xhostconfig["{0}".format(config_item)]
				#--find the config item to replace
				#--replace the config item
				hostconfig_file = fileinput.input(files=("{0}_output/{1}".format(self.i_base,host)),inplace=1)
				for line in hostconfig_file:
					replace = line.replace("<{0}>".format(replace_item), "{0}".format(replace_item_with))
					print replace,
					#time.sleep(.50)
				hostconfig_file.close()
			print "{0} done".format(host)
			print "======================"

	def file_list(self):
		filelist = subprocess.check_output(['ls -l {0}_output | awk -F\' \' \'{{ print $9 }}\' | sort -n '.format(self.i_base)], shell=True)
		filelist = filelist.split()
		return filelist
	
	def concat_ic(self,o_file):
		# clear out the file
		open("{0}".format(o_file), 'w').close()
		# open file to append
		with open("{0}".format(o_file), "a") as base_file:
			for file in Import_conf.file_list(self):
				print ("starting {0}".format(file))
				with open("{0}_output/{1}".format(self.i_base,file), "r") as source_file:
						for line in source_file:
							base_file.write(line)
							#print line,
						source_file.close()
		base_file.close()