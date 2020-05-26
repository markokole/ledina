sleep 20 && \
python3 manage.py runscript create_database && \
python3 manage.py migrate && \
python3 manage.py makemigrations && \
python3 manage.py runscript create_users && \
python3 manage.py runscript create_testdata && \
python3 manage.py runserver 0.0.0.0:8000