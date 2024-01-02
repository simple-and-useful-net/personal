
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator

class PersonalDataModel(models.Model):

    tel_regex = RegexValidator( regex=r'^[0-9]+$', 
                message = ("電話番号は数字で入力してください"))

    name = models.CharField( max_length=20 )
    tel = models.CharField( max_length=11, 
                           validators=[tel_regex, MinLengthValidator(11)])
    email = models.EmailField()

    sex         = models.CharField( max_length=10 )
    prefecture  = models.CharField( max_length=20 )
    hobby       = models.JSONField()
    food        = models.JSONField()

