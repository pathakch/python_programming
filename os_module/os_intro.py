"""
Project : Requirement :
There are files with '.txt' and '.docx' extensions inside folder_1 , 
we have to create two folder inside os_module with txt_only and docx_only
and cut files from folder_1 and paste those inside these new folders.
current folder structure:

python_programming
>os_module
    >folder_1

required structure:
python_programming
>os_module
    >folder_1
    >txt_only
    >docx_only
"""
import os

# print current working directory
print(f"\n{os.getcwd()} is the current working directory\n")

# change current working directory to the below path (inside 'os_module') 
os.chdir("C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module")

# check current working directory after changing from previous path to new path.
current_path = os.getcwd()
print(f"\n{current_path} is the current working directory now\n")

# join paths to go to folder_1 inside os_module folder.
myfolder_path = os.path.join(current_path, "folder_1")

# create function to create new paths/folders inside os_module if not exist already.
def path_maker(ext_name):
    path = os.path.join(current_path, ext_name)

    # check folders already exist or not,if not then create one with given extension name.
    if not os.path.exists(path):
        os.mkdir(path)

    return path    

text_path = path_maker("text_only")
jpg_path = path_maker("docx_only")

for dir_paths, dir_names, filenames in os.walk(myfolder_path):

    # loop through each file inside myfolder_path
    for file in filenames:

        # check the extension of file if it is .txt
        if os.path.splitext(file)[-1] == '.txt':
            # cut file from previous path and paste it into new path
            os.rename(os.path.join(dir_paths,file),f"{text_path}/{file}")

        # check the extension of file if it is .docx
        elif os.path.splitext(file)[-1] == '.docx':
            # cut file from previous path and paste it into new path
            os.rename(os.path.join(dir_paths,file),f"{jpg_path}/{file}")    
    