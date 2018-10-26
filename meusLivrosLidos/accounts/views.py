from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .forms import SignUpForm
from meusLivrosLidos.core.tasks import send_mail_template


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('livro:livro-list')
            #Usuário deverá ser inativado para que sua ativação seja via e-mail.
            #Envio de email (celery)
            # redirecionar para página indicando que um e-mail foi enviado para validar usuário                                    
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})