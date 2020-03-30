from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Book object: {self.title}, {self.author}>"

class Review(models.Model):
    review=models.CharField(max_length=255)
    rating=models.IntegerField()
    user=models.ForeignKey('log_reg.User', related_name='reviews', on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Review object: {self.review}, {self.rating}>"