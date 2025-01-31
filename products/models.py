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
    
    def get_by_natural_key(self, name):
        return self.get(name = name)
    
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
    
    def get_by_natural_key(self, name):
        return self.get(name = name)
    
    class Meta:
        verbose_name = "wine"
        verbose_name_plural = "wines"


class Pairing(models.Model):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, blank=True, null=True)        
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pairing: cheese: {self.cheese_id} - wine: {self.wine_id}"
    
    class Meta:
        verbose_name = "pairing"
        verbose_name_plural = "pairings"


 