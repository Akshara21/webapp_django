from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to= 'profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

# Overridin save method of a model
# why we override save method is that before we save any image we will have to check its conditions so that it wudn result in flaw while uploading the picture for us
# since, css is set at our end to accept only 125 pixels and such so if we upload large images ultimately it is scaled down to fit in. nstead it shud be resizing the dimensions
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # save is used as a function from parent class so we use super
        # motive of save func here is to resize the pixels like convert larger img into smaller one
        img = Image.open(self.image.path)
# for resizing the image we are using conditons to detect how big the given image and is there a necessity to rescale it down
# here thumbnail is used to resize and we pass the size and dimensions into output size then pass as args to thumbnail save the img by passign the path into it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
