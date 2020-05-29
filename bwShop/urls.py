
from django.urls import path,include
from django.views.static import serve

import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework import routers

from bwShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet

router = routers.DefaultRouter()
router.register('goods',GoodsListViewSet)


schema_view = get_schema_view(title='corejson')
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    #文件上传路径
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # path('goods/',GoodsListView.as_view(),name='good-list'),
    path(r'',include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('docs/',include_docs_urls(title='DRF文档')),
    path('schema/',schema_view)
]
