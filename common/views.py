from django.shortcuts import render

from consulting.forms import LetsTalkForm

from common.tasks import self_email


class CommonContextMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class CommonFormsMixin:
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ltf'] = LetsTalkForm()
        # context['ff'] = FeedbackForm()
        # context['searchform'] = SearchbarForm()
        return context

    def post(self, request, *args, **kwargs):
        lt_form = LetsTalkForm(request.POST)

        if lt_form.is_valid():
            name = lt_form.cleaned_data['name']
            email = lt_form.cleaned_data['email']
            phone = lt_form.cleaned_data['phone_number']

            message = f'\nОтправитель: {name} \n\nEmail: {email} \n\nPhone: {phone} \n\n'
            self_email.delay('Let\'s Talk', message)

        context = self.get_context_data(**kwargs)
        context['ltf'] = LetsTalkForm()

        return render(request, self.template_name, context)

