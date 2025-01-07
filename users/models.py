from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Wine, Cheese, Pairing

#AbstractUser = classe de base qui contient tous les champs et méthodes de User mais n'est pas elle-même un modèle concret
#AbstractUser est conçu spécifiquement pour ce cas d'usage : créer un modèle User personnalisé

#override sur classe AbstractUser pour rendre champs email obligatoire
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True, blank=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "custom user"
        verbose_name_plural = "custom users"


class Favourite(models.Model):
    user_id = models.ManyToManyField(CustomUser)
    wine_id = models.ManyToManyField(Wine)
    cheese_id = models.ManyToManyField(Cheese)
    created_at = models.DateField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.user_id}'s favourite: {self.cheese_id} - {self.wine_id}"   
    
    class Meta:
        verbose_name = "favourite"
        verbose_name_plural = "favourites"



          