from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    def description_less(self):
        return self.description[:50]

    def pub_date_only(self):
        return self.pub_date.strftime('%b %e %Y')

