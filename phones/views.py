from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    qs = Phone.objects.all()

    sort = request.GET.get('sort', False)
    if 'name' == sort:
        qs = qs.order_by('name', )
    elif 'min_price' == sort:
        qs = qs.order_by('price', )
    elif 'max_price' == sort:
        qs = qs.order_by('-price', )
    context = {
        'phones': qs
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {
        'phone': phone
    }
    if phone:
        return render(request, template, context)
    # TODO create template
    return render(request, 'notfound.html', context)
