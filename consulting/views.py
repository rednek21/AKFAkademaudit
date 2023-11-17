from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonContextMixin, CommonFormsMixin
from consulting.forms import IndexForm, LetsTalkForm, ContactForm

from common.tasks import self_email

pages = ['Домой', 'О нас', 'Услуги', 'Контакты']


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'consulting/index.html'
    title = 'Академ-аудит - Домой'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['index_view'] = 'index_view'

        page_list = pages.copy()
        page_list.remove('Домой')
        context['page_list'] = page_list

        i_form = IndexForm()
        lt_form = LetsTalkForm()
        context['if'] = i_form
        context['ltf'] = lt_form
        return context

    def post(self, request, *args, **kwargs):
        i_form = IndexForm(request.POST)
        lt_form = LetsTalkForm(request.POST)

        if i_form.is_valid():
            name = i_form.cleaned_data['name']
            email = i_form.cleaned_data['email']
            phone = i_form.cleaned_data['text']

            message = f'\nОтправитель: {name} \n\nEmail: {email} \n\nText: {phone} \n\n'
            self_email.delay('Home page', message)

        if lt_form.is_valid():
            name = lt_form.cleaned_data['name']
            email = lt_form.cleaned_data['email']
            phone = lt_form.cleaned_data['phone_number']

            message = f'\nОтправитель: {name} \n\nEmail: {email} \n\nPhone: {phone} \n\n'
            self_email.delay('Let\'s Talk', message)

        context = self.get_context_data(**kwargs)
        context['if'] = IndexForm()
        context['ltf'] = LetsTalkForm()

        return render(request, self.template_name, context)


class AboutView(CommonContextMixin, CommonFormsMixin, TemplateView):
    template_name = 'consulting/about.html'
    title = 'Академ-аудит - О нас'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['about_view'] = 'about_view'

        page_list = pages.copy()
        page_list.remove('О нас')
        context['page_list'] = page_list

        return context


class ContactView(CommonContextMixin, CommonFormsMixin, TemplateView):
    template_name = 'consulting/contact.html'
    title = 'Академ-аудит - Контакты'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['contact_view'] = 'contact_view'

        page_list = pages.copy()
        page_list.remove('Контакты')
        context['page_list'] = page_list

        contact_form = ContactForm()
        lt_form = LetsTalkForm()
        context['cf'] = contact_form
        context['ltf'] = lt_form

        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        lt_form = LetsTalkForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            msg = contact_form.cleaned_data['text']

            message = f'\nОтправитель: {name} \n\nEmail: {email} \n\nMessage: {msg} \n\n'
            self_email.delay('Home page', message, subject=subject)

        if lt_form.is_valid():
            name = lt_form.cleaned_data['name']
            email = lt_form.cleaned_data['email']
            phone = lt_form.cleaned_data['phone_number']

            message = f'\nОтправитель: {name} \n\nEmail: {email} \n\nPhone: {phone} \n\n'
            self_email.delay('Let\'s Talk', message)

        context = self.get_context_data(**kwargs)
        context['cf'] = ContactForm()
        context['ltf'] = LetsTalkForm()

        return render(request, self.template_name, context)


class ServiceView(CommonContextMixin, CommonFormsMixin, TemplateView):
    template_name = 'consulting/service.html'
    title = 'Академ-аудит - Услуги'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['service_view'] = 'service_view'

        page_list = pages.copy()
        page_list.remove('Услуги')
        context['page_list'] = page_list

        return context
