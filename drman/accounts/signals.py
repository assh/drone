from django.db.models.signals import post_save, pre_save
from .models import *
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=Mission)
def update_launch(sender, instance, created, **kwargs):
    #print("P1")
    if created == False:
        #print("P2")
        if instance.launch_now == True:
            #print("P3")
            Launch.objects.create(mission=instance, now='1', drone=instance.drone)
        if instance.launch_now == False:
            #print("P4")
            try:
                inst = Launch.objects.get(mission=instance)
                inst.delete()
            except:
                pass

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")

@receiver(pre_save,sender = Mission)
def setVerbose(sender,instance,**kwargs):
    print("P7")
    if instance._state.adding is True:
        print("P6")
        instance.vds = instance.state
        instance.vda = instance.drone
        instance.vc = instance.customer
        instance.vm = instance.manager
        print("P7")
    else:
        print("P8")
        instance.vds = str(instance.state)
        instance.vda = str(instance.drone)
        instance.vc = str(instance.customer)
        instance.vm = str(instance.manager)
        print("P9")

@receiver(pre_save,sender = Drone)
def setDroneVerbose(sender,instance,**kwargs):
    print("P7")
    if instance._state.adding is True:
        print("P6")
        instance.vl = instance.locale
        print("P7")
    else:
        print("P8")
        instance.vl = str(instance.locale)
        print("P9")
    