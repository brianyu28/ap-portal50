from django.conf.urls import url
from . import views, api

app_name = 'curriculum'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/', views.register, name='register'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^login/', views.login_view, name='login'),

	url(r'^customize/$', views.customize, name='customize'),
	url(r'^customize/(?P<chapter>[^ ])/$', views.chapter_customize, name='chapter_customize'),
	url(r'^customize/(?P<chapter>[^ ])/(?P<slug>[\w.@+-]+)/$', views.module_customize, name='module_customize'),
    
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^settings/$', views.settings, name='settings'),

	url(r'^curriculum/$', views.curriculum_page, name='curriculum_page'),
	url(r'^curriculum/(?P<chapter>[^ ])/$', views.curriculum_page_chapter, name='curriculum_page_chapter'),
	url(r'^curriculum/(?P<chapter>[^ ])/(?P<slug>[\w.@+-]+)/$', views.curriculum_page_module, name='curriculum_page_module'),
    
    url(r'^page/(?P<pagename>[\w.@+-]+)/$', views.show_page, name='show_page'),
    
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    
    url(r'^api/modinfochange/$', api.update_modinfo, name='update_modinfo'),
    url(r'^api/resource-toggle/$', api.resource_toggle, name='resource_toggle'),
    url(r'^api/module-toggle/$', api.module_toggle, name='module_toggle'),
    url(r'^api/chapter-toggle/$', api.chapter_toggle, name='chapter_toggle'),
    url(r'^api/update-settings/$', api.update_settings, name='update_settings'),
    url(r'^api/add-resource/$', api.add_resource, name='add_resource'),
    url(r'^api/remove-resource/$', api.remove_resource, name='remove_resource'),
    url(r'^api/access-resource/$', api.access_resource, name='access_resource'),
    url(r'^api/edit-resource/$', api.edit_resource, name='edit_resource'),

	# both /brian and /u/brian will go to the user's curriculum page
	url(r'^(?P<username>[\w.@+-]+)/$', views.teacher_page, name='teacher_page'),
	url(r'^(?P<username>[\w.@+-]+)/(?P<chapter>[^ ])/$', views.teacher_page_chapter, name='teacher_page_chapter'),
	url(r'^(?P<username>[\w.@+-]+)/(?P<chapter>[^ ])/(?P<slug>[\w.@+-]+)/$', views.teacher_page_module, name='teacher_page_module'),
	url(r'^u/(?P<username>[\w.@+-]+)/$', views.teacher_page, name='teacher_page_u'),
	url(r'^u/(?P<username>[\w.@+-]+)/(?P<chapter>[^ ])/$', views.teacher_page_chapter, name='teacher_page_chapter_u'),
	url(r'^u/(?P<username>[\w.@+-]+)/(?P<chapter>[^ ])/(?P<slug>[\w.@+-]+)/$', views.teacher_page_module, name='teacher_page_module_u'),
]