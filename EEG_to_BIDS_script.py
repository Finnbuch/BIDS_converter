import os
import glob
#ask for folder full of hdr files
class BIDS :
    
    def __init__(self, config_dict) :
        pass

    
    hdr_folder = input("Please enter the Path to the Folder containing the .hdr files\n")

    #read in list of all header files

    list_of_hdrs = []

    for hdr in glob.glob(hdr_folder + "\\*.vhdr") :
        list_of_hdrs.append(hdr)
    print(list_of_hdrs)

    #ask for destination folder
    destination_folder = input("Please enter a Destination Folder\n")

    #ask list of participants with codes and list of number of sessions per participant

    #enter authors name

    def authors_name():
        return ( " -aut " + input("Please enter the Authors Name/Names\n"))
        
    #enter license

    def license():
        return (" -lic " + input("Please enter the License\n"))

    #enter manufacturers

    def manufacturers():
        return (" -mnf " + input("Please enter the Name of the Manufacturer\n"))

    #enter power line freuquenzy

    def power_line_freuquenzy():
        return (" -plf " + input("Please enter the Power Line frequenzy\n"))

    #enter ref

    def ref():
        return (" -ref "+ input("Please enter the reference\n"))


    #ask if you want to enter addditional information
    final_list = []
    parameters_list = [authors_name, license, manufacturers, power_line_freuquenzy, ref]
    question_list = [" an authors name", "a license", "the name of a manufacturer", "the powerline frequency", "a reference"]

    #creating a list of Subjects 

    unique_subs = []
    list_of_sub_names = []
    for hdr in list_of_hdrs:
        list_of_sub_names.append((os.path.basename(hdr))[0:6])
        for element in list_of_sub_names:
            if element not in unique_subs:
                unique_subs.append(element)
    print(list_of_sub_names)
    print(unique_subs)


    for counter, parameter in enumerate(parameters_list):
        add_info = input("Do you want to enter " + str(question_list[counter]) + " ?\nPlease enter y for Yes or n for No\n" )
        if add_info == "y" :
            final_list.append(parameter())


    #call script with all info in loop
    counter = 0
    for sub_id in unique_subs:
        sub_string = " -sub " + sub_id 
        i = 1
        for session in list_of_sub_names:
            if session != sub_id:
                continue
            session_string = " -ses s0" + str(i)
            final_string = "Z:\\BV2BIDS\\BV2BIDS.exe" 
            final_string += " -hdr " + list_of_hdrs[counter] + " -dst " + destination_folder + sub_string + session_string
            print(final_list)
            for element in final_list :
                final_string += element
            print(final_string)
            os.system(final_string)
            i+=1
            counter+=1 
            print(counter)   	

