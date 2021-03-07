# Blog Django

Welcome to the website of the company blog. The website enables the creation, segregation and publication of messages on the website.

### Requirements and technical details:

- Python 3.9
- Django 3.1.7
- Psycopg2-binary 2.8.6
- Django-ckeditor 6.0.0
- Pillow 8.1.1
- Django-taggit 1.2.0

Functionalities:

- Add an article, show list of articles and articles segregate by categories and tags
- Absolute urls, properly for google robot indexing
- Filtering content in admin views
- An advanced edition of body text in admin views
- Segregation by a category and tags 
- Recommendation of similar articles in sidebar (based on tags)
- Native Comments 

## Install

1. git...
2. Pipenv install
3. sudo docker-compose up --build
3. (meanwhile) sudo docker-compose exec backend python manage.py makemigrations
4. (meanwhile) sudo docker-compose exec backend python manage.py migrate

(optional, it s easy to make migration by migration.sh file)

If migration is not correct try `` makemigrations comments article users``

5. ctrl + C and again sudo docker-compose up


## Admin:

![admin](<static/images/readme_img/admin_views.png>)

![admin2](<static/images/readme_img/admin2_views.png>)

