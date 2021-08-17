from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models
from PIL import Image, ImageDraw


class Client(models.Model):
    GENDERS = (("male", "erkak"), ("female", "ayol"))
    VERSIONS = (("Qirgiziston", "Qirgiziston"), ("Boshqa", "Boshqa"))
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDERS)
    passport = models.CharField(max_length=255, unique=True)
    telfon = models.CharField(max_length=255)
    qayerga = models.CharField(max_length=255, choices=VERSIONS)
    test_olindi = models.DateTimeField()
    natija_chiqdi = models.DateTimeField()
    qrcode = models.ImageField(upload_to="qrcode/", blank=True)

    def __str__(self):
        return self.full_name


    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f"http://172.20.10.2:8000/people/{self.id}")
        canvas = Image.new('RGB',  (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.full_name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)


class Info(models.Model):
    research_method = models.CharField(max_length=255)
    name_of_labaratory = models.CharField(max_length=255)
    head_of_labaratory = models.CharField(max_length=255)
