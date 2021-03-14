from django.db import models

# add to settings
# create a migration
# migrate
# add to admin



class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
