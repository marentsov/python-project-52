### Hexlet tests and linter status:
[![Actions Status](https://github.com/marentsov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/marentsov/python-project-52/actions)
[![Coverage](https://github.com/marentsov/python-project-52/actions/workflows/project-check.yml/badge.svg)](https://github.com/marentsov/python-project-52/actions/workflows/project-check.yml)
### Code quality checks by [qlty.sh](https://qlty.sh): 
[![Maintainability](https://qlty.sh/badges/401c869e-d0bf-4e80-93c4-2a5901989072/maintainability.svg)](https://qlty.sh/gh/marentsov/projects/python-project-52)
[![Code Coverage](https://qlty.sh/badges/401c869e-d0bf-4e80-93c4-2a5901989072/test_coverage.svg)](https://qlty.sh/gh/marentsov/projects/python-project-52)
### Code quality checks by [SonarQube](https://www.sonarsource.com/products/sonarqube/?ref=secjuice.com):
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=marentsov_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=marentsov_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=marentsov_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=marentsov_python-project-52)


### [Демонстрация проекта](https://python-project-52-hiri.onrender.com) на render.com
****
## Менеджер задач
****
##### Менеджер задач — это веб-приложение для управления задачами, разработанное на Python. Оно позволяет пользователям создавать, отслеживать и управлять задачами, назначать исполнителей, устанавливать статусы и добавлять метки.

### Технологии

Данный проект создан с помощью данных инструментов:

|                                                   | Описание                                                                                           |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Django](https://www.djangoproject.com/)          | "A high-level Python web framework that encourages rapid development and clean, pragmatic design." |
| [Bootstrap 5](https://getbootstrap.com/)          | "A popular CSS framework for building responsive and mobile-first web projects."                   |
| [PostgreSQL](https://www.postgresql.org/)         | "A powerful, open-source relational database management system."                                   |
| [Gunicorn](https://gunicorn.org/)                 | "A WSGI server for Unix, used to deploy Python applications."                                      |
| [Docker](https://www.docker.com/)                 | "A platform for developing, shipping, and running applications in containers."                     |
| [uv](https://docs.astral.sh/uv/)                  | "An extremely fast Python package and project manager, written in Rust"                            |
| [dj-database-url](https://pypi.org/project/dj-database-url/)| "A Django utility that allows you to configure databases using URL-style strings."                 |
| [Whitenoise](http://whitenoise.evans.io/en/latest/) | "A library for serving static files in Python applications."                                       |
| [Rollbar](https://rollbar.com/)                   | "A tool for error monitoring and real-time issue tracking."                                        |
| [ruff](https://docs.astral.sh/ruff/)              | "An extremely fast Python linter and code formatter, written in Rust"                              |
| [Flake8](https://flake8.pycqa.org/en/latest/)     | "A tool for checking Python code style and quality."                                               |
| [Coverage.py](https://coverage.readthedocs.io/en/7.6.12/) | "A tool for measuring code coverage of Python programs."                                           |

****

### Установка: 

```
make setup
```
### Запуск dev-сервера:
```
make dev
```
### Запуск продакшн сервера 
```
make render
```

****

После запуска приложения, зарегистрируйтесь, создавайте метки и статусы, используйте их при создании задач, назначайте исполнителей, редактируйте пользовательские данные, наслаждайтесь!
