echo "BUILD START"
python3.12.2 -m pip install -r requirements.txt
python3.12.2 manage.py collectstatic --noinput --clear
echo "BUILD END"
