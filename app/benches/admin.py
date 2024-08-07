from django.contrib import admin
from .models import BenchType, BenchDistrict, BenchEnvironment, Bench, BenchImage


@admin.register(BenchType)
class BenchTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BenchDistrict)
class BenchDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BenchEnvironment)
class BenchEnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BenchImageInline(admin.TabularInline):
    model = BenchImage


@admin.register(Bench)
class BenchAdmin(admin.ModelAdmin):
    list_display = ('id', 'location_latitude', 'location_longitude', 'created_date', 'author')
    list_filter = ('type', 'district', 'environment')
    inlines = [BenchImageInline]
    search_fields = ['id']


@admin.register(BenchImage)
class BenchImageAdmin(admin.ModelAdmin):
    list_display = ('bench', 'image')
