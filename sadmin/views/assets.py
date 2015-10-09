# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,render_to_response,RequestContext
from sadmin.models import Assets
from adminLTE.common.CommonPaginator import SelfPaginator
from sadmin.forms import AssetsListForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render,get_object_or_404,redirect
# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    kwvars = {
        'request':request,
    }
    return render_to_response('index.html',kwvars,RequestContext(request))



##资产管理
@login_required
def AssetsList(request):

    all_assets = Assets.objects.all()
    #分页
    lst = SelfPaginator(request,all_assets, 10)
    return render_to_response('assets/assets_list.html', {'all_host_list': all_assets,'Page':lst})

@csrf_exempt
def CreateAssets(requst):
    if requst.method == 'POST':
        form = AssetsListForm(requst.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            return HttpResponseRedirect(reverse('sadmin:assetslist'))
        else:
            print '数据不符合要求'
    else:
        form = AssetsListForm()
    #return render(request, 'create_host.html', locals())
    #print form
    return render_to_response('assets/create_assets.html', {'form': form})

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
    return render_to_response('assets/create_assets.html', {'form': form})

def DelAssets(request,assets_id):
    a = get_object_or_404(Assets, pk=assets_id)
    a.delete()
    #a.objects.filter(id = assets_id).delete()
    return redirect('sadmin:assetslist',)







