from django.db import models

# Create your models here.

class User(models.Model):

    pronouns = (
        ('they', "They/Them"),
        ('he', "He/Him"),
        ('she', "She/Her"),
        ('ot', 'Other'),
        ('na', "Rather not say"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    pronoun = models.CharField(max_length=32, choices=pronouns, default="they")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "User"
        verbose_name_plural = "User"