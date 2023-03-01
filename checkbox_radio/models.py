from django.db import models


class Check_box(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Radio(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    name_post = models.CharField(max_length=500)
    category = models.ForeignKey(Radio, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Check_box)

    def __str__(self) -> str:
        return self.name_post
    

# 1- Criar o model Post

# 2- fazer as migrações

# 3- cadastrar no admin

# 4- ir ate o admin e cadastrar os posts

# 5- ir ate o form e criar o formulario do Post

# 6- criar as urls

# 7- ir ate a views e fazer um crud.

# 8- Criar as paginas html



