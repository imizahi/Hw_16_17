echo Run db migrate
flask db upgrade
echo Run application
flask run -h 0.0.0.0 -p 5000