from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'make_roi_images/(\d+)', views.make_roi_images,name='make_roi_images')
]