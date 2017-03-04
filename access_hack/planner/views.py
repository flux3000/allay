from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, PermissionDenied


def index(request):
    
    # if request.user.is_authenticated():
    #     return redirect('/planner/')
    
    # return redirect('login_view')
    return redirect('/planner/')


def planner(request):

	context = {}
	return render(request, 'planner/index.html', context)