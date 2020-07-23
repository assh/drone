from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver

@receiver(post_save,sender=Mission)
def update_launch(sender, instance, created, **kwargs):
    print("P1")
    if created == False:
        print("P2")
        if instance.launch_now == True:
            print("P3")
            Launch.objects.create(mission=instance,now='1')
        if instance.launch_now == False:
            print("P4")
            try:
                inst = Launch.objects.get(mission=instance)
                inst.delete()
            except:
                pass
        
