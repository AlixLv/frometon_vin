from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Pairing


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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favourites")
    pairing = models.ForeignKey(Pairing, on_delete=models.CASCADE, related_name="favourited_by")
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)  
    
    def __str__(self):
        return f"{self.user} 's favourite : {self.pairing}"   
    
    class Meta:
        verbose_name = "favourite"
        verbose_name_plural = "favourites"
        # pour empêcher les doublons:
        unique_together = ['user', 'pairing']



          