from django.db import models
# import qrcode
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File

class Museum(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Slot(models.Model):
    museum = models.ForeignKey(Museum, related_name='slots', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    seat_limit = models.PositiveIntegerField()
    # seat_left=models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.museum.name} - {self.start_time} to {self.end_time}"

class Ticket(models.Model):
    slot = models.ForeignKey(Slot, related_name='tickets', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    # qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    # def save(self, *args, **kwargs):
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     qr.add_data(f'Ticket for {self.user_name} | Slot: {self.slot}')
    #     qr.make(fit=True)
        
    #     img = qr.make_image(fill='black', back_color='white')
    #     buffer = BytesIO()
    #     img.save(buffer)
    #     self.qr_code.save(f'qr_{self.pk}.png', File(buffer), save=False)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket for {self.user} | Slot: {self.slot}"
