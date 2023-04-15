
#### These are the various functions of OS module in python
```
1.  os.name
2.  os.uname()
3.  os.getlogin()
4.  os.makedirs()
5.  os.getcwd()
6.  os. walk()
7.  os. chdir()
8.  os.fstat()
9.  os.stat()  :-->>>> file descriptor
10. os.path.join()
11. os.path.exists()
12. os.path.split()
13. os.path.splitext()
14. os.rename()
15. os.remove()
16. os.removedirs()
17. os.rmdir()
```
>`os.name` :-> return name of operating system.

    print(f"Name of windows OS system is {os.name}")
    output:-> Name of windows OS system is nt


>`os.sep` :-> method is useful when we don't want to hardcode the separator
 means we want to write os independent path.

    print(f"separator in windows system is {os.sep}")
    Output:-->> separator in windows system is \


>`os.getcwd()` :-> get current working directory

    print(os.getcwd())
>`os.mkdir()` :-> create a folder named 'new_folder' in current working directory.

    os.mkdir("new_folder")

>Important method :-->> `os.walk`
 os.walk will return a tuple of folders and files
 first it enters in root folder (here `os_module` )
 then it gives all folders if any inside root folder and then folders and files inside those folders

    for dirpaths, dirnames, filenames in os.walk("os_module"):
        print(f"these are directory paths : {dirpaths}")
        print(f"These are directory names in above path : {dirnames}")
        print(f"These are file names in above directory : {filenames}")
        print(f'\n')

    Output :-->>
    these are directory paths : os_module
    These are directory names in above path : ['folder_1', 'my_folder']
    These are file names in above directory : ['os_intro.py']


    these are directory paths : os_module\folder_1
    These are directory names in above path : []
    These are file names in above directory : ['f1.jpg', 'f1.txt', 'f2.jpg', 'f2.txt']


    these are directory paths : os_module\my_folder
    These are directory names in above path : ['jpg_folder', 'txt_folder']
    These are file names in above directory : []


    these are directory paths : os_module\my_folder\jpg_folder
    These are directory names in above path : []
    These are file names in above directory : []


    these are directory paths : os_module\my_folder\txt_folder
    These are directory names in above path : []
    These are file names in above directory : ['t2.txt']


>*`os.chdir()`*

    current_path = os.getcwd()
    print(f"This is the current working directory before : {current_path}\n")

    Output :-->
    This is the current working directory before : C:\Users\ckp43_000\python_programming\python_programming

    here original path is : C:\Users\ckp43_000\python_programming\python_programming\os_module\folder_1

    we will put one more backward slash in this path this is the rule of python.

    os.chdir("C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module\\folder_1")
    current_path = os.getcwd()
    print(f"current working directory has been changed to : {current_path}")
    otput :->
    current working directory has been changed to : C:\Users\ckp43_000\python_programming\python_programming\os_module\folder_1
```

os.chdir("C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module")
print(os.getcwd())

os.chdir("C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module")
#print(os.getcwd())

>important function *os.path.join()*

    current_path = os.getcwd()
    print(current_path)
C:\Users\ckp43_000\python_programming\python_programming\os_module
>now we want to enter into 'my_folder' inside current working directory
```
new_folder_path = os.path.join(current_path,"my_folder")
print(new_folder_path)
output : C:\Users\ckp43_000\python_programming\python_programming\my_folder
```

>now suppose we want to create a file inside the folder 'my_folder' and write something.
creating a file inside 'my_folder'
```
file_name = os.path.join(new_folder_path,"sample_file.txt")
with open(file_name, "w") as f:
    f.write("Hello this is sample file inside 'my_older'")
```
> *os.path.exists()*
```
print(f"current working path : {os.getcwd()}")
outpt:-->> current working path : C:\Users\ckp43_000\python_programming\python_programming

print(os.path.exists("my_folder"))
output :-->> False 

means above folder is not present in current working path
now we can create a folder inside current working directory if the folder is not present

if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
```    
> `os.chdir()` changes the working directory.
``` 
os.chdir("C:\\Users\ckp43_000\\python_programming\\python_programming\\os_module\my_folder\\txt_folder")

current_path = os.getcwd()

file_name = os.path.join(current_path,"t2.txt")

'os.split()' segregate path and file name , it returns  tuple of pathname and filename

print(os.path.split(file_name))
output :-> ('C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module\\my_folder\\txt_folder', 't2.txt')

print(os.path.splitext(file_name))
output :--> ('C:\\Users\\ckp43_000\\python_programming\\python_programming\\os_module\\my_folder\\txt_folder\\t2', '.txt')
```
os.rename : works for renaming and cut and paste.
```
```
changing current working directory 

os.chdir("C:\\Users\ckp43_000\\python_programming\\python_programming\\os_module\\my_folder\\txt_folder")

current_path = os.getcwd()

There is a file named t2.txt in above path

file_name  = os.path.join(current_path,"t2222.txt")

below function will rename the file name 't2.txt' to 't2222.txt'

print(os.rename(file_name,"t2222.txt"))

changing current working directory to the path where 'folder_1' is present so that 
we will paste the file 't2222.txt' after cutting from previous folder

os.chdir("C:\\Users\ckp43_000\\python_programming\\python_programming\\os_module")

current_path_1 = os.getcwd()

new_folder_path = os.path.join(current_path_1,"folder_1")

print(os.rename(file_name,f"{new_folder_path}/t2222.txt"))



















