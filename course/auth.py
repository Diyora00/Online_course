from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from course.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from course.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from course.models import User


class Register(CreateView, SuccessMessageMixin):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)

        subject = "Verify Email"
        message = render_to_string('email/verify_email_message.html', {
            'request': self.request,
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(subject, message, to=[user.email])
        email.content_subtype = 'html'

        email.send()
        return redirect('verify-email-done')


# class LoginUserView(LoginView):
#     template_name = 'auth/login.html'
#     redirect_authenticated_user = True
#     authentication_form = LoginForm
#
#     def form_valid(self, form):
#         pass
#
#     def get_success_url(self):
#         return reverse_lazy('home')


class LogoutUserView(TemplateView):
    template_name = "auth/logout.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email has been verified.')
        return redirect('home')
    else:
        messages.warning(request, 'The link is invalid.')

    return render(request, 'email/verify_email_confirm.html')


def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'auth/login.html', context)
