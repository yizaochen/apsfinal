echo "Start"
jb=/home/yizaochen/miniconda3/envs/apsfinal/bin/jupyter-book
cd /home/yizaochen/courses/apsfinal

cp notebooks/multiplecategorical.ipynb ./ourfinalreport/
cp notebooks/numerical.ipynb ./ourfinalreport/
cp notebooks/cond_prob_given_stroke_nonstroke.ipynb ./ourfinalreport/
cp notebooks/age_confounder.ipynb ./ourfinalreport/
cp notebooks/simplecategorical.ipynb ./ourfinalreport/
cp notebooks/regression_categorical.ipynb ./ourfinalreport/
cp notebooks/regression_numerical.ipynb ./ourfinalreport/
cp notebooks/regression_mix.ipynb ./ourfinalreport/


#$jb build ourfinalreport
$jb build ourfinalreport --builder pdfhtml
cp ourfinalreport/_build/pdf/book.pdf ./
echo "Done!"