from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            # podemos usar o form.save direto ou então usar o commit=False para fazer alterações e depois salvar
            # contact = form.save(commit=False)
            # contact.show = False
            # as duas linhas anteriores são um exemplo desse uso
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
        return render(request, 'contact/create.html', context)
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            # podemos usar o form.save direto ou então usar o commit=False para fazer alterações e depois salvar
            # contact = form.save(commit=False)
            # contact.show = False
            # as duas linhas anteriores são um exemplo desse uso
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
        return render(request, 'contact/create.html', context)
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request, 'contact/contact.html',
       {
           'contact': contact,
           'confirmation': confirmation,
           }
    )
