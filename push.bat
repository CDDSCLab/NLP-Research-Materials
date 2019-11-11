@echo off
echo "generating path"
python genDirectory.py
git pull origin master
set /p input=please enter commit:
git add .
git commit -m "%input%"
git push -u origin master
