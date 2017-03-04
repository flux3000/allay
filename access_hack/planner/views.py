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

    return redirect('/welcome/')


def welcome(request):

	context = {}
	return render(request, 'planner/welcome.html', context)

def intake(request):

	context = {}
	return render(request, 'planner/intake.html', context)

def options(request):

	context = {}
	return render(request, 'planner/options.html', context)


def timeline_ca(request):

	context = {}
	return render(request, 'planner/timeline-CA.html', context)


def timeline_tx(request):

	context = {}
	return render(request, 'planner/timeline-TX.html', context)





