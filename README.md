# reciPy

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/reciPy/blob/master/LICENSE)

:hamburger: reciPy: A simple tutorial on how to make your DRF tests easier using Faker and Factory Boy

In this repository is an example of how you can improve your testing on Django REST Framework using the Faker and Factory Boy libraries. You can read the full tutorial at: [https://medium.com/@mdcg.dev/melhorando-seus-testes-no-django-rest-framework-com-as-bibliotecas-faker-e-factory-boy-f9692bced7](https://medium.com/@mdcg.dev/melhorando-seus-testes-no-django-rest-framework-com-as-bibliotecas-faker-e-factory-boy-f9692bced7)

## Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

**Documentation:** [https://docs.djangoproject.com/en/2.2/](https://docs.djangoproject.com/en/2.2/)

## Django REST Framework

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

**Documentation:** [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

## Faker

Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

Faker is heavily inspired by PHP Faker, Perl Faker, and by Ruby Faker.

**Documentation:** [https://faker.readthedocs.io/en/stable/](https://faker.readthedocs.io/en/stable/)

## Factory Boy

factory_boy is a fixtures replacement based on thoughtbot’s factory_bot.

As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex object.

Instead of building an exhaustive test setup with every possible combination of corner cases, factory_boy allows you to use objects customized for the current test, while only declaring the test-specific fields.

factory_boy is designed to work well with various ORMs (Django, Mongo, SQLAlchemy), and can easily be extended for other libraries.

Its main features include:

- Straightforward declarative syntax
- Chaining factory calls while retaining the global context
- Support for multiple build strategies (saved/unsaved instances, stubbed objects)
- Multiple factories per class support, including inheritance

**Documentation:** https://factoryboy.readthedocs.io/en/latest/

## Contributing

Feel free to do whatever you want with this project. :-)