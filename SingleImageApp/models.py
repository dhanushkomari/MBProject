from django.db import models
from django.contrib.auth.models import CustomUser as User

# Create your models here.


class SingleImage(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    input_image = models.ImageField(upload_to = 'SingleInputImages/')
    result_image = models.ImageField(upload_to = 'SingleResultImages/')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = 'Uploaded Single Image'
        verbose_name_plural = 'Uploaded Single Images'
        ordering = ('-created_at',)

    def get_url(self):
        pass
        # return reverse()

