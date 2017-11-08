from django.conf.urls import url
from . import views

urlpatterns	=	[
				url(r'^$',	views.equipo_list, name='equipo_list'),
				url(r'^equipo/$',	views.equipo_list, name='equipo_list'),
                url(r'^equipo/(?P<pk>\d+)/$',	views.equipo_detail,	name='equipo_detail'),
                url(r'^equipo/new/$',	views.equipo_new,	name='equipo_new'),
                url(r'^equipo/(?P<pk>\d+)/edit/$',views.equipo_edit,name='equipo_edit'),
                url(r'^equipo/(?P<pk>\d+)/remove/$',	views.equipo_remove,	name='equipo_remove'),
				url(r'^equipo/(?P<pk>\d+)/publish/$',	views.equipo_publish,	name='equipo_publish'),
				url(r'^medics/$',	views.medic_list, name='medic_list'),
                url(r'^medic/(?P<pk>\d+)/$',	views.medic_detail,	name='medic_detail'),
                url(r'^medic/new/$',	views.medic_new,	name='medic_new'),
                url(r'^medic/(?P<pk>\d+)/edit/$',views.medic_edit,name='medic_edit'),
                url(r'^medic/(?P<pk>\d+)/remove/$',	views.medic_remove,	name='medic_remove'),
				url(r'^drafts/$',	views.equipo_draft_list,	name='equipo_draft_list'),
				url(r'^accounts/profile/$',	views.equipo_list, name='profile_list'),
				#url(r'^reservacion/$',	views.reservacion_list, name='reservacion_list'),
                #url(r'^reservacion/(?P<pk>\d+)/$',	views.reservacion_detail,	name='reservacion_detail'),
                #url(r'^reservacion/new/$',	views.reservacion_new,	name='reservacion_new'),
                #url(r'^reservacion/(?P<pk>\d+)/edit/$',views.reservacion_edit,name='reservacion_edit'),
                #url(r'^reservacion/(?P<pk>\d+)/remove/$',	views.reservacion_remove,	name='reservacion_remove'),
]
