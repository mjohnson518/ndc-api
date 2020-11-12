# ndc-api

This app follows an API-first design, and is intended to provide interested parties with the information needed to analyze the similarities and differences between Nationally Determined Contributions. Using data compiled by the German Development Institute, each NDC is evaluated by 138 ranking qualifiers and metrics, which practitioners can utilize to gain insights, assess progress, gauge ambition levels, and craft policy.

This is a Dockerized Django app, witha PostgreSQL db, that utilizes Heroku for deployment. I'm currently struggling to connect my populated PostgreSQL db (which I can access and view w/ pgAdmin) to my Django project.

I've reviewed multiple [Docker & PostgreSQL tutorials](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial) and I've posted abt my issues to the [Django Forum](https://groups.google.com/g/django-users/c/0nKJUHuzxGk/m/J1y8VSsgAQAJ), but I have not been able to solve the issue yet. 

From the Django Forum, and the [Heroku DevCenter](https://devcenter.heroku.com/articles/heroku-postgresql), I've gathered that I need to use [dj-database-url](https://pypi.org/project/dj-database-url/), but everytime I set the config vars &/or envrion vars for dj-database-url, I get error messages.

How can I solve this pestering issue!?
