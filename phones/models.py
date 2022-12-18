from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    image = models.URLField(verbose_name='Картинка', null=True)
    release_date = models.DateField(verbose_name='Data relyse', null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}/{self.slug}'

    class Meta:
        verbose_name = 'Телефоны'
        verbose_name_plural = u'Телефоны'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['slug', ]),
            models.Index(fields=['price', 'lte_exists']),
        ]