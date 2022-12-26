from django.urls import path

from user.views import AmakiView, AmmaView, TogaView, XolaView, AmakivachchaView,\
    AmmavachchaView, TogavachchaView, XolavachchaView, JiyanView, PochchaView, KenayiView

urlpatterns = [
    path('amakilar/', AmakiView.as_view(), name='amakilar'),
    path('ammalar/', AmmaView.as_view(), name='ammalar'),
    path('togalar/', TogaView.as_view(), name='togalar'),
    path('xolalar/', XolaView.as_view(), name='xolalar'),
    path('amakivachchalar/', AmakivachchaView.as_view(), name='amakivachchalar'),
    path('ammavachchalar/', AmmavachchaView.as_view(), name='ammavachchalar'),
    path('togavachchalar/', TogavachchaView.as_view(), name='togavachchalar'),
    path('xolavachchalar/', XolavachchaView.as_view(), name='xolavachchalar'),
    path('jiyanlar/', JiyanView.as_view(), name='jiyanlar'),
    path('pochchalar/', PochchaView.as_view(), name='pochchalar'),
    path('kenayilar/', KenayiView.as_view(), name='kenayilar')
]



# from django.urls import path
#
# from user.views import amaki_view, amma_view, toga_view, xola_view, amakivachcha_view,\
#     ammavachcha_view, togavachcha_view, xolavachcha_view, jiyan_view, pochcha_view, kenayi_view
#
# urlpatterns = [
#     path('amakilar/', amaki_view, name='amakilar'),
#     path('ammalar/', amma_view, name='ammalar'),
#     path('togalar/', toga_view, name='togalar'),
#     path('xolalar/', xola_view, name='xolalar'),
#     path('amakivachchalar/', amakivachcha_view, name='amakivachchalar'),
#     path('ammavachchalar/', ammavachcha_view, name='ammavachchalar'),
#     path('togavachchalar/', togavachcha_view, name='togavachchalar'),
#     path('xolavachchalar/', xolavachcha_view, name='xolavachchalar'),
#     path('jiyanlar/', jiyan_view, name='jiyanlar'),
#     path('pochchalar/', pochcha_view, name='pochchalar'),
#     path('kenayilar/', kenayi_view, name='kenayilar')
# ]
