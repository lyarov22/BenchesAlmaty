from django.shortcuts import get_object_or_404, render, redirect
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

    return render(
        request,
        'benches/create_bench.html',
        {'benches': benches, 'bench_form': bench_form, 'image_form': image_form}
    )


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

    benches_all_count = Bench.objects.count()
    has_backrest_now_count = benches.filter(has_backrest=True).count()
    has_bin_now_count = benches.filter(has_bin=True).count()
    has_backrest_all_count = Bench.objects.filter(has_backrest=True).count()
    has_bin_all_count = Bench.objects.filter(has_bin=True).count()

    return render(
        request,
        'benches/bench_list.html',
        {
            'benches': benches,
            'districts': districts,
            'bench_types': bench_types,
            'benchesAll': benches_all_count,
            'hasBackrestNow': has_backrest_now_count,
            'hasBinNow': has_bin_now_count,
            'hasBackrestAll': has_backrest_all_count,
            'hasBinAll': has_bin_all_count,
        }
    )


def bench_detail(request, bench_id):
    bench = get_object_or_404(Bench, id=bench_id)
    return render(
        request,
        'benches/bench_detail.html',
        {'bench': bench}
    )
