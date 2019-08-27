from django.contrib.auth.models import User, Permission
from django.core.management.base import BaseCommand, CommandError

from flagsapp.models import Flag, Favourite


class Command(BaseCommand):
    help = 'Setup'

    def handle(self, *args, **options):
        user = User.objects.create_user('bot', 'bot@bot.bot',
                                 'SkjwYOSuOps39gjvHIckEw')
        user.user_permissions.add(Permission.objects.get(name='can_review'))
        user.save()
        flag = Flag.objects.create(owner=user, awaiting_check=False, flag="wwi{C55-Runn1ngCod3With0utRunn1ngCOd3}", css="")
        flag.save()
        fav = Favourite.objects.create(flag=flag, user=user)
        fav.save()
