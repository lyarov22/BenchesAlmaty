from django.shortcuts import render, redirect

from django.db.models import Count

from benches.models import Bench, BenchDistrict, BenchType
from .forms import BenchForm, BenchImageForm

def create_bench(request):
    benches = Bench.objects.all()
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

    return render(request, 'benches/create_bench.html', {'benches': benches, 'bench_form': bench_form, 'image_form': image_form})

def bench_count():
    benches = Bench.objects.all()
    return benches

def bench_list(request):
    benches = Bench.objects.all()
    districts = BenchDistrict.objects.annotate(districtBenchesCount=Count('bench')).all()
    bench_types = BenchType.objects.annotate(bench_typesCount=Count('bench')).all()

    # Фильтрация по району
    district_slug = request.GET.get('district')
    if district_slug:
        benches = benches.filter(district__slug=district_slug)
        
    # Фильтрация по типу
    type_slug = request.GET.get('type')
    if type_slug:
        benches = benches.filter(type__slug=type_slug)

    # Фильтрация по наличию/отсутствию урны
    has_bin = request.GET.get('has_bin')
    if has_bin:
        benches = benches.filter(has_bin=True)
    elif has_bin == '0':
        benches = benches.filter(has_bin=False)

    # Фильтрация по наличию/отсутствию спинки
    has_backrest = request.GET.get('has_backrest')
    if has_backrest:
        benches = benches.filter(has_backrest=True)
    elif has_backrest == '0':
        benches = benches.filter(has_backrest=False)

    benches = benches.annotate(districtBenchesCount=Count('id'))

    return render(request, 
        'benches/bench_list.html', 
        {'benches': benches, 'districts': districts, 'bench_types': bench_types, 
        'benchesAll':  bench_count().count,

        'hasBackrestNow': benches.filter(has_backrest=True).count, 
        'hasBinNow': benches.filter(has_bin=True).count,
         
        'hasBackrestAll': bench_count().filter(has_backrest=True).count,
        'hasBinAll': bench_count().filter(has_bin=True).count,
        })
    