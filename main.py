import templp
#from main_mod import *

base_file = "config_base"
data_file = "config_data"
output_file = "testfile"


def main(data_file,base_file,output_file):
	main_file1 = templp.Import_conf(data_file,base_file)
	main_file1.generate_ic()
	main_file1.concat_ic(output_file)


if __name__ == "__main__":
	main(data_file,base_file,output_file)