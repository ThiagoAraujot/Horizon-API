from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order
from users.models import MecanicoProfile


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    try:
        # print(f'USER: {instance.mecanico.user.id}')
        if created:
            mecanico_profile = MecanicoProfile.objects.get(
                user=instance.mecanico.user.id)

            mecanico_profile.purchase_count += 1

            if mecanico_profile.purchase_count == 1:
                mecanico_profile.level = 'Bronze'
            elif mecanico_profile.purchase_count == 2:
                mecanico_profile.level = 'Prata'
            elif mecanico_profile.purchase_count >= 3:
                mecanico_profile.level = 'Ouro'

            mecanico_profile.save()
    except Exception as e:
        print(f"Error in signal: {e}")


@receiver(post_delete, sender=Order)
def order_post_delete(sender, instance, **kwargs):
    try:
        mecanico_profile = MecanicoProfile.objects.get(
            user=instance.mecanico.user.id)

        if mecanico_profile.purchase_count > 1:
            mecanico_profile.purchase_count -= 1

            if mecanico_profile.purchase_count == 1:
                mecanico_profile.level = 'Bronze'
            elif mecanico_profile.purchase_count == 2:
                mecanico_profile.level = 'Prata'
            elif mecanico_profile.purchase_count >= 3:
                mecanico_profile.level = 'Ouro'

            mecanico_profile.save()
    except Exception as e:
        print(f"Error in signal: {e}")
