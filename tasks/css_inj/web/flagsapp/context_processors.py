from flagsapp.models import Favourite


def favourite_processor(request):
    try:
        if request.user.is_anonymous:
            return {}
        flag = Favourite.objects.get(user=request.user).flag
        return {'favourite': flag}
    except Favourite.DoesNotExist:
        return {}
