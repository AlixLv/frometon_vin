from django.db import models



class AllCheesesManager(models.Manager):
    def get_all_cheeses(self):
        return self.objects.all()


class CheeseDetailManager(models.Manager):
    def get_detail_cheese_product(self, id):
        return self.filter(id = id)


class CheeseCategoryManager(models.Manager):
    def get_cheese_by_category(self):
     # values_list pour retourner une liste de valeurs sur le champs "type_of_milk"
    # argument flat=True pour indiquer qu'on veut une liste simple de valeurs, pas de tuples
    # distinct() pour garantir des valeurs uniques
        return self.values_list('type_of_milk', flat=True).distinct()


class Cheese(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    type_of_milk = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Manager #
    objects = AllCheesesManager()
    category_cheese = CheeseCategoryManager()
    detail_cheese = CheeseDetailManager()
    
    def __str__(self):
        return self.name
    
    def get_by_natural_key(self, name):
        return self.get(name = name)
    
    class Meta:
        verbose_name = "cheese"
        verbose_name_plural = "cheeses"
        

class WineDetailManager(models.Manager):
    def get_detail_wine_product(self, id):
        return self.filter(id = id)

        
class Wine(models.Model):
    name = models.CharField(max_length=200)
    appellation = models.CharField(max_length=200)
    vineyard = models.CharField(max_length=200)
    grape_variety = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  
    
    objects = WineDetailManager()
    
    def __str__(self):
        return f"{self.name}, {self.year}" 
    
    def get_by_natural_key(self, name):
        return self.get(name = name)
    
    class Meta:
        verbose_name = "wine"
        verbose_name_plural = "wines"


class CheesePairingManager(models.Manager):
    def get_cheese_pairing(self, cheese_id, wine_id):
        return self.get_queryset().filter(cheese=cheese_id, wine=wine_id)

    def get_list_cheese_pairings(self, cheese):
        return self.get_queryset().filter(cheese=cheese)


class WinePairingManager(models.Manager):
    def get_list_wine_pairings(self, wine):
        return self.get_queryset().filter(wine=wine)


class PairingManager(models.Manager):
    def get_pairing_object(self, id):
        return self.filter(id=id)


class Pairing(models.Model):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, blank=True, null=True)        
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    cheese_objects = CheesePairingManager() 
    wine_objects = WinePairingManager()
    pairing_objects = PairingManager()
    
    def __str__(self):
        return f"Pairing: cheese: {self.cheese_id} - wine: {self.wine_id}"
    
    class Meta:
        verbose_name = "pairing"
        verbose_name_plural = "pairings"


 