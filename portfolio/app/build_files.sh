echo "BUILD START"
python5.0.3 -m pip install -r requirements.txt
python5.0.3 manage.py collectstatic --noinput --clear
echo "BUILD END"
