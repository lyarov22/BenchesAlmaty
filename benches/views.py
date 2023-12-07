from django.shortcuts import render, redirect

from benches.models import Bench
from .forms import BenchForm, BenchImageForm

def create_bench(request):
    if request.method == 'POST':
        bench_form = BenchForm(request.POST, request.FILES)
        image_form = BenchImageForm(request.POST, request.FILES)

        if bench_form.is_valid() and image_form.is_valid():
            bench = bench_form.save(commit=False)
            bench.author = request.user  # Устанавливаем автора скамейки текущим пользователем
            bench.save()

            image = image_form.save(commit=False)
            image.bench = bench
            image.save()

            return redirect('mySite:index')  # Укажите URL, куда перенаправить после успешного создания
    else:
        bench_form = BenchForm()
        image_form = BenchImageForm()

    return render(request, 'benches/create_bench.html', {'bench_form': bench_form, 'image_form': image_form})


def bench_list(request):
    benches = Bench.objects.all()
    return render(request, 'benches/bench_list.html', {'benches': benches})