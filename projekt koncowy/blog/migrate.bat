flask db init
flask db migrate -m "Added published column"
flask db upgrade
