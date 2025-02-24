from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

#Book - Object
class Book(models.Model):
    titulo = models.CharField(_("Title"), max_length=50)
    author = models.CharField(_("Author"), max_length=50)
    publication_date = models.DateTimeField(_("Publication date"), auto_now=False, auto_now_add=True)
    available = models.BooleanField(_("Available"),default=True)
    
    def __str__(self):
        return f'{self.titulo}-{self.author}'
    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
#Even though django has a user model, i will create one o myself
class User(models.Model):
    name = models.CharField(_("User name"), max_length=50)
    #Settings E-mail to be unique
    email = models.EmailField(_("User e-mail"), max_length=254,unique=True)
    registration_date = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")