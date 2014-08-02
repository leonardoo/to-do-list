from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'todo.views.list', name="lista"),
    url(r'^add/$', 'todo.views.add', name="add"),
    url(r'^edit/(?P<pk>\d+)/$', 'todo.views.edit', name="edit"),
    url(r'^delete/(?P<pk>\d+)/$', 'todo.views.delete', name="delete"),
)
