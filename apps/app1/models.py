from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review=models.CharField(max_length=255)
    rating=models.IntegerField()
    user=models.ForeignKey('log_reg.User', related_name='reviews')
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)