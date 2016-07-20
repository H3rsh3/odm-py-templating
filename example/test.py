import templp




base_file1 = "config_base"
data_file1 = "config_data"
output_file1 = "testfile"


base_file2 = "config_base_2"
data_file2 = "config_data_2"
output_file2 = "testfile_2"

base_file3 = "config_base_3"
data_file3 = "config_data_3"
output_file3 = "testfile_3"


itembase = ([base_file1,base_file2,base_file3])
###
temp1 = templp.Import_conf(data_file1,base_file1)
temp1.generate_ic()
temp1.concat_ic(output_file1)
###
temp2 = templp.Import_conf(data_file2,base_file2)
temp2.generate_ic()
###
temp3 = templp.Import_conf(data_file3,base_file3)
temp3.generate_ic()
###
temp1.concat_h_ic(data_file1,itembase)

