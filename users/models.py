from django.contrib.auth.models import AbstractUser
from django.db import models

#AbstractUser = classe de base qui contient tous les champs et méthodes de User mais n'est pas elle-même un modèle concret
#AbstractUser est conçu spécifiquement pour ce cas d'usage : créer un modèle User personnalisé

#override sur classe AbstractUser pour rendre champs email obligatoire
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True, blank=False)
    
    def __str__(self):
        return self.username