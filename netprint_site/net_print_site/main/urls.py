from django.urls import path
from . import views
from form_res_view import views as vw_frm
urlpatterns = [ 
    path('', views.index, name='home'),
    path('contacts', views.cont, name='contacts'), 
    path('supa', views.show_success, name='success_page'),
    path('res_page', vw_frm.show_results, name='res_page'),
    path('download/<path:file_path>/', vw_frm.download_file, name='download_file'),
    path('non_admin', vw_frm.show_not_admin, name="not_admin_page")
]
