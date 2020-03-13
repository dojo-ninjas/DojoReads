from django.db import models

class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors={}
        if '@' not in postData['email'] or '.' not in postData['email']:
            errors['email']= 'Invalid Email'
        if len(postData['password'])<8:
            errors['password']= 'Password needs to be at least 8 characters'
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email must be unique."
        if postData['password'] != postData['confirmPassword']:
            errors['password']= 'Password and Confirm Password do not match'
        return errors
    def loginValidator(self, postData):
        errors={}
        if len(User.objects.filter(email=postData['email']))== 0:
            errors['email'] = "Email does not exist"
        
        user= User.objects.filter(email=postData['email'])
        if user[0].password != postData['password']:
            errors['password']= 'Incorrect Email/Password combination'
        return errors
class User(models.Model):
    name= models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    objects=UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Movie object: {self.name}, {self.alias}, {self.email}>"
