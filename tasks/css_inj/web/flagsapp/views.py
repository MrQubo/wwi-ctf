from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.http import JsonResponse, HttpResponse, Http404, \
    HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect, \
    render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic

from flagsapp.models import Flag, Favourite


class FlagCreateForm(ModelForm):
    class Meta:
        model = Flag
        fields = ['flag', 'css']


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@method_decorator(login_required, name='dispatch')
class FlagCreate(generic.CreateView):
    form_class = FlagCreateForm
    success_url = reverse_lazy('thanks')
    template_name = 'create_flag.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.awaiting_check = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class FlagsList(generic.TemplateView):
    template_name = 'flags-home.html'

    def get_context_data(self, **kwargs):
        return {
            'flags_awaiting': Flag.objects.filter(owner=self.request.user,
                                                  awaiting_check=True),
            'flags_reviewed': Flag.objects.filter(owner=self.request.user,
                                                  reviewed=True),
        }


@login_required()
def set_favourite(request, id):
    flag = get_object_or_404(Flag, pk=id)
    if flag.owner != request.user or request.user.has_perm('flagsapp.can_review'):
        raise Http404()

    fav, created = Favourite.objects.get_or_create(user=request.user, defaults={'flag':flag})
    fav.flag = flag
    fav.save()

    return redirect('listflag')


@permission_required('flagsapp.can_review')
def flags_to_review(request):
    return JsonResponse({
        'urls': [reverse('show_flag', kwargs={'id': flag.id}) for flag in Flag.objects.filter(awaiting_check=True)]
    })


@login_required()
def show_flag(request, id):
    flag = get_object_or_404(Flag, id=id)
    if flag.owner != request.user:
        if not request.user.has_perm('flagsapp.can_review'):
            raise Http404()
    return render(request, 'flag-show.html', context={'flag': flag})


@login_required()
def css(request, id):
    flag = Flag.objects.get(id=id)
    if flag.owner != request.user:
        if not request.user.has_perm('flagsapp.can_review'):
            raise Http404()
        flag.awaiting_check = False
        flag.reviewed = True
        flag.save()
    return HttpResponse(flag.css, content_type='text/css')
