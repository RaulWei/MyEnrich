# system import
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse,Http404
from enrich.models import Milestone
import datetime

# Create your views here.

def enrich(request):
    if request.method == "POST":
        ms = Milestone()
        ms.Content = request.POST['msContent']
        today = datetime.date.today()
        ms.Date = today
        ms.save()

    milestones = Milestone.objects.all()
    return render(request, "milestone.html", {'milestones': milestones})
    # t = loader.get_template("milestone.html")
    # c = Context({'milestones': milestones})
    # return HttpResponse(t.render(c))

def milestone_history(request):
    t = loader.get_template("milestone_history.html")
    if request.method == "POST":
        select = request.REQUEST["select_day"]
        ms = Milestone.objects.filter(Date=select)
        #milestones = Milestone.objects.all()
        c = Context({'milestones': ms})
        tt = loader.get_template("milestone.html")
        return HttpResponse(tt.render(c))
        #return HttpResponse("ok")
    c = Context({})
    return  HttpResponse(t.render(c))

def milestone_history_msBox_record(request):
    select_day = request.GET["select_day"]
    ms = Milestone.objects.filter(Date=select_day)
    t = loader.get_template("milestone_history_msBox_record.html")
    c = Context({'milestones': ms})
    return HttpResponse(t.render(c))



def delete_milestone(request):
    id = request.REQUEST["id"]
    Milestone.objects.filter(id = id).delete()
    return HttpResponse('true')


def update_milestone(request):
    id = request.REQUEST["id"]
    content = request.REQUEST["content"]
    Milestone.objects.filter(id = id).update(Content = content)
    return HttpResponse('true')
