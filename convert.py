import cc_dat_utils
import json
import test_json_utils
import cc_json_utils


#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data

# print(cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat"))

#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
file = open(input_json_file) #Open the file specified by input_json_file
json_data = json.load(file) #Use the json module to load the data from the file
game_library_data = test_json_utils.make_game_library_from_json(json_data) #convert the data to GameLibrary data
print (game_library_data) #^Print out the resulting GameLibrary data
### End Add Code Here ###


#Part 3
input_json_levels_file = "data/jsprong_cc1.json" #Load your custom JSON file
json_file = open(input_json_levels_file)
json_file_data = json.load(json_file)
json_game_data = cc_json_utils.make_cc_data_from_json(json_file_data) #Convert JSON data to cc_data
cc_dat_utils.write_cc_data_to_dat(json_game_data, "data/jsprong_cc1.dat") #Save converted data to DAT file
cc_test = cc_dat_utils.make_cc_data_from_dat("data/jsprong_cc1.dat")
print(cc_test)