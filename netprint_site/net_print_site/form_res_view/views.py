from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from main.models import Offers
from django.http import HttpResponse
from django.conf import settings
import os

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin, login_url='/non_admin')
def show_results(request):
    data = Offers.objects.all()
    return render(request, 'res_page/res_page.html', {"data" : data})

def show_not_admin(response):
    return render(response, 'res_page/error_admin.html')

def download_file(request, file_path):
    # Полный путь к файлу на сервере
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Проверка существования файла
    if os.path.exists(file_path):
        # Открыть файл для чтения в бинарном режиме
        with open(file_path, 'rb') as file:
            # Создать HttpResponse с заголовком, указывающим на скачивание файла
            response = HttpResponse(file.read(), content_type='application/force-download')
            
            # Получить имя файла из полного пути
            file_name = os.path.basename(file_path)
            
            # Установить заголовок Content-Disposition для указания имени файла при скачивании
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            
            return response
    else:
        # Если файл не существует, вернуть 404 Not Found
        return HttpResponse(status=404)