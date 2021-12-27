from django.db import models
from Property.models import BaseModel,Property,User
from django.db.models.deletion import CASCADE

class Notification(BaseModel):
    property = models.ForeignKey(Property,on_delete=CASCADE)
    receiver = models.ForeignKey(User,on_delete=CASCADE,related_name='Notification_receiver')
    sender = models.ForeignKey(User,on_delete=CASCADE,related_name='Notification_sender')
    text_preview = models.CharField(max_length=50,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.text_preview[:50]
