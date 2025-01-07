from django.db import models

class Cheese(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    type_of_milk = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "cheese"
        verbose_name_plural = "cheeses"
        
        
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
    
    def __str__(self):
        return f"{self.name}, {self.year}" 
    
    class Meta:
        verbose_name = "wine"
        verbose_name_plural = "wines"


class Pairing(models.Model):
    cheese_id = models.ManyToManyField(Cheese)        
    wine_id = models.ManyToManyField(Wine)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pairing: {self.cheese_id} - {self.wine_id}"
    
    class Meta:
        verbose_name = "pairing"
        verbose_name_plural = "pairings"