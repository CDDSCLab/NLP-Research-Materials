@echo off
echo "pull origin"
git pull origin master

echo "generating path"
python genDirectory.py

git add .
set /p input=please enter commit message:

git commit -m "%input%"
echo "pushing the latest commit"

git push -u origin master
echo "success"
