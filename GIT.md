## All about Git 

GIT is a software which is called version control tool.
Git and github both are different thing; Github is a git hosting website; where we can host our git repository after creating github account.
working process for GIT:
There are three ways to work with git:

    1. creating new local repository and then creating new remote repository and adding local repository to remote repository.
	2. creating new local repository and then adding this local repository to the already existing remote repository.
	3. pulling code from already existing remote repository

	
--------------------------------------
#### creating new local git repository
--------------------------------------	   
1. install git in local computer
2. create one new folder anywhere in local computer
3. open git bash in that folder and initialize that folder as git folder (using command "git init")and 
   work whtever you want to work like creating files, editing files, creating feature branch etc.
   This is called our local git repository . Now we will need to push this local git repository into remote git repository

#### Creating new remote git repository in github 
- go to github and create new git repository from GitHub console.

#### Adding remote repository to the local git repository:

`command : git remote add origin <remote_repository_url>` 

(example remote_repository_url : https://github.com/pathakch/Sample_Repo.git)

This command says name the remote repository with name 'origin' and add this remote origin 
so that we can push our local repository to this origin;
so this command will add the remote repository.

### pushing local git repository to the remote git repository : 
>NOTE : -->> (we can push our local git repository either to the newly created remote repository or already existing remote repository. )

`command : git push origin <branch_name>`

(if our remote repository is public then will not get any error , but, will get error if it's private repository.)
(when we are creating loacal git repo , may be we have created any feature branch also that's why <branch_name> is given in command
we can push both 'master' branch or any other 'feature' branch also.)

#### important git commands :  

`git diff` : compare working tree from staging area.--if working directory and staging area are same it won't return anything.

`git diff --staged` : compare staging area to last commit.

`git checkout -f` : match working directory to the last commit 
  (if someone changes something and save but we want to be in the last commit state)

`git rm <filename>` : delete file from staging area, 
- means if we did git commit and then we realize we need to remove this file from thn we use this command.

`git rm --cached` : does the same thing as above but does not delete the file , it just remove from staging area.

`git status -s` : provide some more visibility about git status-- do practice and understand this command.

`touch .gitignore` : creates gitignore file which, will be helpful if you do not want some files to be tracked then we can put those 
files/*.extension_name inside the gitignore , then git will not track those files anymore.
   
`git branch -v` : shows branch name,last commit hash and commit messages

`git branch --merged`: shows which branches has been merged 

`git branch --no-merged` : shows which branches have not been merged

`git branch -d branch_name` : deletes given branch  

`rm -rf .git` : removes `.git` file from a folder so that the folder will not remain git repository.

`git remote` :to check whether we r on remote directory or not 

`git remote -v` : to check whether we r on remote directory or not

`git remote -v`

     origin  https://github.com/pathakch/Sample_Repo.git (fetch)
     origin  https://github.com/pathakch/Sample_Repo.git (push)

`git push origin branch_name`(bugfix):pushesh the new branch on remote git repo.

`git push origin bugfix:mybugfix`  => will push new branch named bugfix with a different name "mybugfix"

`git push -d origin branch_name` : deletes branch from remote  repository

`git merge branch_name` : merge other branches with master(give this command when u r on master branch)
 