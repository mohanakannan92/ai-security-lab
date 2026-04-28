saving configs created

(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git config --global user.name "Mohanakannan M"
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git config --global user.email "mohanthehacker92@gmail.com"
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git config --global --list
user.name=Mohanakannan M
user.email=mohanthehacker92@gmail.com
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git add .
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git commit -m "Completed prompt injection lab and documentation"
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git branch
* master
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> git push origin master


To push new changes to github
git add .
git commit -m "Added new folder with files"
git push



cmd to get into venv
 (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Mohanakannan\AI\source\repo\ai-security-lab\venv\Scripts\Activate.ps1)

or 

python -m venv venv 

first run ollama
 ollama run tinyllama  

then run uvicorn
uvicorn main:app --reload 
   
to run main.py via cmd
 & c:/Mohanakannan/AI/source/repo/ai-security-lab/venv/Scripts/python.exe c:/Mohanakannan/AI/source/repo/ai-security-lab/main.py

