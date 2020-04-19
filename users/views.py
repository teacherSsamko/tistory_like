from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)  # 아직은 저장하지 않고, 메모리에만 만들어 놓음
            user.set_password(user_form.cleaned_data['password'])
            user.save()  # 패스워드 저장 후 db에 저장
            return render(request, 'registration/login.html', {'user_form': user_form})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form': user_form})
