# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sadmin.models import Assets
from adminLTE.common.CommonPaginator import SelfPaginator
from sadmin.forms import AssetsListForm
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render,get_object_or_404,redirect
# Create your views here.

from django.contrib.auth.decorators import login_required

# @login_required
# def index(request):
#     kwvars = {
#         'request':request,
#     }
#     return render_to_response('index.html',kwvars,RequestContext(request))



##资产管理
@login_required
def AssetsList(request):

    all_assets = Assets.objects.all()
    #分页
    lst = SelfPaginator(request,all_assets, 10)
    return render_to_response('assets/assets_list.html', {'all_host_list': all_assets,'Page':lst},RequestContext(request))

@csrf_exempt
def CreateAssets(request):
    if request.method == 'POST':
        form = AssetsListForm(request.POST)
        if form.is_valid():
            form.save()
            #cd = form.cleaned_data
            return HttpResponseRedirect(reverse('sadmin:assetslist'))
        else:
            print '数据不符合要求'
    else:
        form = AssetsListForm()
    #return render(request, 'create_host.html', locals())
    #print form
    return render_to_response('assets/create_assets.html', {'form': form},RequestContext(request))

@csrf_exempt
def EditAssets(request,assets_id):
    try:
        a = get_object_or_404(Assets, pk=assets_id)
    except Assets.DoesNotExist:
        raise Http404("资产不存在..")
#    return render_to_response('create_assets.html', {'form': a})

    if request.method == "POST":
        form = AssetsListForm(request.POST, instance=a)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            return redirect('sadmin:assetslist',)
            #return HttpResponseRedirect(reverse('mtime:post_detail', args=(post.pk,)))
    else:
        form = AssetsListForm(instance=a)
    return render_to_response('assets/create_assets.html', {'form': form},RequestContext(request))

@login_required
def DelAssets(request,assets_id):
    a = get_object_or_404(Assets, pk=assets_id)
    a.delete()
    #a.objects.filter(id = assets_id).delete()
    return redirect('sadmin:assetslist',)





def jquery_1(request):
    #tem='JS_test/jquery_%s.html'%id
    return render(request,"JS_test/jquery_index.html")



def jquery_2(request,id):
    tem='JS_test/jquery_%s.html'%id
    return render(request,tem)



def jquery_3(request):
    tem='JS_test/demo_test.txt'
    return render(request,tem)



def test_yufa(request):
    tem = 'JS_test/edit.html'
    return render(request,tem)




def jquery_4(request):
    tem='JS_test/demo_test_post.asp'
    return render(request,tem)

#
# def ajax_1(request,id):
#     tem='ajax/ajax_%s.html'%id
#     return render(request,tem)




def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    #HttpResponse 返回一个结果传递给ret
    return HttpResponse(str(a+b))





import json

def ajax_list(request):
    a = range(100)
    #print json.dumps(a)
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    #print json.dumps(name_dict)
    return HttpResponse(json.dumps(name_dict), content_type='application/json')



def ajax_read_file(request):
    filename = '/data/1.txt'
    with open(filename,'r') as f:
        # data = f.read()
        return HttpResponse(f.read())
        # return  HttpResponse(f.readlines())




