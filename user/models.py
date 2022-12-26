from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    choices = (
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol')
    )

    father = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_father',
                               related_query_name='father_query', limit_choices_to={'toifa': 'erkak'})
    mother = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_mother',
                               related_query_name='mother_query', limit_choices_to={'toifa': 'ayol'})
    pair = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_pair',
                             related_query_name='pair_query')
    toifa = models.CharField(max_length=10, choices=choices)
    photo = models.ImageField(upload_to='users/')
