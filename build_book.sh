echo "Start"
jb=/home/yizaochen/miniconda3/envs/apsfinal/bin/jupyter-book
cd /home/yizaochen/courses/apsfinal

cp notebooks/simplecategorical.ipynb ./ourfinalreport/

#$jb build ourfinalreport
$jb build ourfinalreport --builder pdfhtml
cp ourfinalreport/_build/pdf/book.pdf ./
echo "Done!"