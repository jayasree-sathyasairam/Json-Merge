import json
import re
import os
import collections


def file_exists(base_name,folder_path,counter):
    try:
        with open(folder_path+"\\"+base_name+str(counter)+".json") as fo:
            data1 = json.load(fo)
        return True
    except FileNotFoundError:
        return False

def delete_all(base_name,folder_path):
    i=1
    while(file_exists(base_name,folder_path,i)):
        os.remove(folder_path+"\\"+output_base_name+str(i)+".json")
        i=i+1

def check_output_name(output_base_name,folder_path,i):
    if(file_exists(output_base_name,folder_path,i)):
        print("The output file with the same name exists.\nIf you wish to overwrite, enter ( 1 ) or if you would like to enter a new name enter ( 2 )\n")
        flag=input()
        if(flag=="1"):
            delete_all(output_base_name,folder_path)
            return output_base_name
        else:
            output_base_name=input("Enter new name for output file base name:\n")
            output_base_name=check_output_name(output_base_name,folder_path,i)
            return output_base_name
    else:
        return output_base_name

def check_input_name(input_base_name,folder_path,i):
    if(file_exists(input_base_name,folder_path,i)):
        return input_base_name
    else:
        input_base_name=input("The file does not exist. Enter a valid base name:\n")
        input_base_name=check_input_name(input_base_name,folder_path,i)
        return input_base_name

def get_max_file_size(input_base_name,folder_path):
    i=1
    max=0
    while(file_exists(input_base_name,folder_path,i)):
        if(max<os.path.getsize(folder_path+"\\"+input_base_name+str(i)+".json")):
            max=os.path.getsize(folder_path+"\\"+input_base_name+str(i)+".json")
            #print(type(max))
        i=i+1
    return max

def check_max_file_size(max,max_file_size):
    if(max>max_file_size):
        x=input("Please enter a larger file size (atleast larger than the largest input file ["+str(max)+"]):\n")  
        max_file_size=int(x)
        max_file_size=check_max_file_size(max,max_file_size)
        return max_file_size      
    else:
        return max_file_size

def merge(source,destination):
    merged_dict = collections.defaultdict(dict)
    merged_dict.update(destination)
    key_list = []
    for keys in merged_dict.keys():
        key_list.append(keys)
    for key, nested_dict in source.items():
        if key in key_list:
            for val in nested_dict:
                merged_dict[key].append(val)
        else:
            merged_dict[key]=nested_dict
    return dict(merged_dict)

def merge_util(folder_path, input_base_name, output_base_name, max_file_size):
    iterator=1
    counter=1
    while(iterator>=1):
        try:
            with open(folder_path+"\\"+input_base_name+str(iterator)+".json") as fo:
                data1 = json.load(fo)
        except FileNotFoundError:
            break
        if (iterator!=1):
            data2=merge(data1,data2)
            #print(data2)
            #print('\n')
            with open(folder_path+"\\"+output_base_name+".json", "w") as fo:
                #fo.seek(max_file_size-1)
                fo.truncate()
                json.dump(data2, fo)
            #print(os.path.getsize(folder_path+"\\"+output_base_name+".json"))
            if(os.path.getsize(folder_path+"\\"+output_base_name+".json")>max_file_size):
                with open(folder_path+"\\"+output_base_name+str(counter+1)+".json", "w") as fo:
                    #fo.seek(max_file_size-1)
                    fo.truncate()
                    json.dump(data1, fo)
                if(os.path.getsize(folder_path+"\\"+output_base_name+str(counter+1)+".json")>max_file_size):
                    os.remove(folder_path+"\\"+output_base_name+".json")
                    os.remove(folder_path+"\\"+output_base_name+str(counter+1)+".json")
                    print("Please enter a bigger maximum size for output file (atleast larger than the largest input file size)\n")
                    break
                with open(folder_path+"\\"+output_base_name+".json", "w") as fo:
                    #fo.seek(max_file_size-1)
                    fo.truncate()
                    json.dump(data1, fo)
                counter=counter+1
                iterator=iterator+1
                data2=data1             
                continue
            with open(folder_path+"\\"+output_base_name+str(counter)+".json", "w") as fo:
                #fo.seek(max_file_size-1)
                fo.truncate()
                json.dump(data2, fo)
            #print(data2)
        else:
            data2=data1
            with open(folder_path+"\\"+output_base_name+".json", "w") as fo:
                fo.truncate()
                json.dump(data2, fo)
            #print(os.path.getsize(folder_path+output_base_name+".json"))
            if(os.path.getsize(folder_path+"\\"+output_base_name+".json")>max_file_size):
                os.remove(folder_path+"\\"+output_base_name+".json")
                print("Please enter a bigger maximum size for output file (atleast larger than the largest input file size)\n")
                break
            with open(folder_path+"\\"+output_base_name+str(counter)+".json", "w") as fo:
                #fo.seek(max_file_size-1)
                fo.truncate()
                json.dump(data2, fo)
            #print(data2)
        iterator=iterator+1
    try:
        with open(folder_path+"\\"+output_base_name+".json") as fo:
            data1 = json.load(fo)
        os.remove(folder_path+"\\"+output_base_name+".json")
    except FileNotFoundError:
        print("END")


#'C:\\Users\\Saahithya\\Desktop\\json_repo'
folder_path=input('Enter Folder Path\n')

input_base_name=input('Enter input file base name:\n')
input_base_name=check_input_name(input_base_name,folder_path,1)
#'data'
output_base_name=input('Enter output file base name:\n')
output_base_name=check_output_name(output_base_name,folder_path,1)
#print(output_base_name)
#'merge'
x=input("Enter maximum file size for output (in bytes):\n")
max_file_size=int(x)
max=get_max_file_size(input_base_name,folder_path)
#print(type(max))
max_file_size=check_max_file_size(max,max_file_size)
#122

merge_util(folder_path, input_base_name, output_base_name, max_file_size)

#print(data1)
# with open("F:\\temp1.json") as fo:
#     data1 = json.load(fo)

# with open("F:\\temp2.json") as fo:
#     data2 = json.load(fo)

# for i in data2:
#     data1.append(i)

# for i in data1:
#     print
#     print(i)

# with open("F:\\merge.json", "w") as fo:
#     json.dump(data1, fo)
