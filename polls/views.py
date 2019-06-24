from django.contrib import messages #lec 33
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse #lec 34
from .models import Choice,Polls

# Create your views here.
def poll_list(request):
    polls=Polls.objects.all()
    return render(request,'polls/list.html',{'polls':polls})
'''
showing the polls saved in the admin page for now we
have 2 polls in the admin panel if we put 1 or 2 on browser besided the details url
we have get the two sentance( for every santance ) we entered in the model in admin panel
if we put 3 or more like 4,5,6,...etc we will have an error becuse this
doesnt matched in the Polls class
    pass
'''


def poll_detail(request, poll_id):
    #poll=Polls.objects.get(id=poll_id)
    poll=get_object_or_404(Polls,id=poll_id)
    '''
    lec 29
    the next 6 line its just for testing the post and get
    when we want to check the get from termanal we just add
    to browser link --> exampel like this(?name='join'&age=9) beside our url
    '''
    if request.method =="POST":
        print(request.POST)
        print("you post")


    if request.method =="GET":
        print(request.GET)
        print("you Got ME")

    context={'poll':poll}
    return render(request, 'polls/poll_detail.html',context)
    #return HttpResponse('the url is : {}'.format(poll_id))


def poll_vote(request,poll_id):
    #print(request.POST) #print the query in cmd terminal
    #print('Sparator ************************')# print statment just for sparate the sentance above and below
    #choice_id=request.POST['choice'] # lec 30 give the choice readable value from the poll_detail.html in the form that have post method
    #print(choice_id)# print the location of choice in [] function its 1 in the cmd termanal
    poll=get_object_or_404(Polls,id=poll_id) #lec 33
    choice_id=request.POST.get('choice')#add in lec 31
    if choice_id: # to check the choice if we have >> save the votes
        choice = Choice.objects.get(id=choice_id)#grap the content of choice_id
        #poll = choice.question # lec 32
        #print(choice)#print the value of chioce parameter we decleare
        choice.votes += 1 # (call votes parameter from the models.py)incremment the vote --> plus vote
        choice.save()# save the vote we add in the above decleare>> then test that by admin page -- add vote by browser then check the admin page
    else: #lec 33
        messages.error(request,'thies in no Choice') #lec 33
        return HttpResponseRedirect(reverse('poll:detail', args=(poll_id,))) #lec 34 to reverse error msg in the same of the page ==> detail page
        #return HttpResponse('the vote is:{}'.format(poll_id))
    return render(request,'polls/poll_results.html', {'poll':poll}) #lec  32
    #lec 31 if we not have a vote print the next HttpResponse
    #return HttpResponse('theres no votes'.format(poll_id))
    #return render(request,'polls/poll_results.html',{'error':True}) #lec 32




'''
# NOTE: the print statment in the views.py just print there result in cmd compiler
we can ignor it from our views.py

'''
