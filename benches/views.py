from django.shortcuts import render, redirect

from benches.models import Bench, BenchDistrict, BenchType
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
    districts = BenchDistrict.objects.all()
    bench_types = BenchType.objects.all()

    # Фильтрация по району
    district_slug = request.GET.get('district')
    if district_slug:
        benches = benches.filter(district__slug=district_slug)

    # Фильтрация по типу
    type_slug = request.GET.get('type')
    if type_slug:
        benches = benches.filter(type__slug=type_slug)

    # Если запрос делается через AJAX, вернуть только HTML-код результатов
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'benches/bench_list_results.html', {'benches': benches})

    return render(request, 'benches/bench_list.html', {'benches': benches, 'districts': districts, 'bench_types': bench_types})
    