import os

# going inside folder 'os_module' 
os.chdir("C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module")
current_path = os.getcwd()
myfolder_path = os.path.join(current_path, "folder_1")
#print(os.listdir(destination_path))

def path_maker(ext_name):
    path = os.path.join(current_path, ext_name)
    if not os.path.exists(path):
        os.mkdir(path)

    return path    


text_path = path_maker("text_only")
jpg_path = path_maker("jpg_only")

for dir_paths, dir_names, filenames in os.walk(myfolder_path):
    for file in filenames:
        if os.path.splitext(file)[-1] == '.txt':
            os.rename(os.path.join(dir_paths,file),f"{text_path}/{file}")

        elif os.path.splitext(file)[-1] == '.docx':
            os.rename(os.path.join(dir_paths,file),f"{jpg_path}/{file}")    
        







