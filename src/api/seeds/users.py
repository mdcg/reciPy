import factory
from faker import Factory

from django.contrib.auth.models import User


faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    first_name = faker.name()
    email = username = faker.email()
    password = factory.PostGenerationMethodCall('set_password', faker.md5())
