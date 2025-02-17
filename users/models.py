from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from products.models import Pairing


class BaseUserManager(BaseUserManager):
    def get_all_users(self):
        return self.objects.all()


class UserInfoManager(models.Manager):
    # def get_user_info(self, id):
    #     return self.filter(id=id)
    
    def get_by_natural_key(self, username):
        return self.get(username = username)


#AbstractUser = classe de base qui contient tous les champs et méthodes de User mais n'est pas elle-même un modèle concret
#AbstractUser est conçu spécifiquement pour ce cas d'usage : créer un modèle User personnalisé

#override sur classe AbstractUser pour rendre champs email obligatoire
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True, blank=False)
    # Manager #
    objects = BaseUserManager()
    user_info = UserInfoManager()
    
    def __str__(self):
        return self.username
    
    def natural_key(self):
        return (self.username)
    
    class Meta:
        verbose_name = "custom user"
        verbose_name_plural = "custom users"


class BaseFavouriteManager(models.Manager):
    def get_all_favourites(self):
        return self.objects.all()


class FavouriteManager(models.Manager):
    def get_user_favourites(self, user):
        # utilisation de select_related pour éviter n+1 query problem
        # une seule query plus complexe; amélioration des performances 
        # select_related sélectionne les objets en relation ForeignKeys dans le modèle Favourite
        return self.filter(user=user).select_related('pairing__cheese', 'pairing__wine').order_by('pairing__cheese__family')


class Favourite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favourites")
    pairing = models.ForeignKey(Pairing, on_delete=models.CASCADE, related_name="favourited_by")
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)  
    # Manager #
    user_favourites = FavouriteManager()
    objects = BaseFavouriteManager()
    
    def __str__(self):
        return f"{self.user} 's favourite : {self.pairing}"   
    
    class Meta:
        verbose_name = "favourite"
        verbose_name_plural = "favourites"
        # pour empêcher les doublons:
        unique_together = ['user', 'pairing']



          