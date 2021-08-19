from django.db import models
from django.contrib.auth.models import CustomUser as User

# Create your models here.


class SingleImage(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    input_image1 = models.ImageField(upload_to = 'MultiInputImages/')
    input_image2 = models.ImageField(upload_to = 'MultiInputImages/')
    input_image3 = models.ImageField(upload_to = 'MultiInputImages/')
    input_image4 = models.ImageField(upload_to = 'MultiInputImages/')

    result_image1 = models.ImageField(upload_to = 'MultiResultImages/')
    result_image2 = models.ImageField(upload_to = 'MultiResultImages/')
    result_image3 = models.ImageField(upload_to = 'MultiResultImages/')
    result_image4 = models.ImageField(upload_to = 'MultiResultImages/')

    created_at = models.DateTimeField(auto_now_add = True)

    # result from VahanAPI
    vehicle_no = models.CharField(max_length=15)


    def __str__(self):
        return '{}'.format(self.user+" "+self.vehicle_no)

    class Meta:
        verbose_name = 'Uploaded Single Image'
        verbose_name_plural = 'Uploaded Single Images'
        ordering = ('-created_at',)

    def get_url(self):
        pass
        # return reverse()

    def upload_single_image(instance, self):
