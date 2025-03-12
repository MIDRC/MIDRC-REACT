REM Description: Build the documentation
REM Author: @rtomek
REM Date: 2025-03-10

sphinx-apidoc --maxdepth 7 -f -o source/ ../src/

make html

REM cd ..

REM ghp-import -n -p -f docs/build/html

REM cd docs
