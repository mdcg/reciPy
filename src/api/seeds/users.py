import factory
from faker import Factory

from django.contrib.auth.models import User


faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = username = faker.email()
    password = factory.PostGenerationMethodCall(
        'set_password',
        faker.password(
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    )
