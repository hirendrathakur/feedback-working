from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Student, Subject, Question, Course, Professor, Result, Done
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import string
import random
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'feedback/getmail.html')


def index(request,key):
    #user = get_object_or_404(User,first_name=key)
    #user=User.objects.get(first_name=key)
    student = Student.objects.get(key = key)
    done_list = student.done_set.all()
    return render(request, 'feedback/course2.html', {'student': student, 'done_list': done_list, 'key':key})


def polls(request, prof_pk, stud_roll, sub_pk, key):
    #student = get_object_or_404(Student, roll_no=stud_roll)
    #professor = get_object_or_404(Professor,id=prof_pk)
    #subject = get_object_or_404(Subject, id=sub_pk)
    student = Student.objects.get(roll_no = stud_roll)
    professor  = Professor.objects.get(id = prof_pk)
    subject = Subject.objects.get(id = sub_pk)
    #user = get_object_or_404(User, first_name=key)
    #key=user.first_name
    course = Course.objects.filter(subject=subject, professor=professor)
    course = course[0]
    d = student.done_set.all()
    result_list = course.result_set.all()

    for done in d:
        if done.course == course:
            if done.student == student:
                key = done.done
    if not key:
        if request.method == "POST":
            for result in result_list:
                choice = request.POST.get(result.question.question_text)
                if choice == 'excellent':
                    result.excellent_votes += 1
                    result.save()
                elif choice == 'verygood':
                    result.verygood_votes += 1
                    result.save()
                elif choice == 'good':
                    result.good_votes += 1
                    result.save()
                elif choice == 'fair':
                    result.fair_votes += 1
                    result.save()
                elif choice == 'poor':
                    result.poor_votes += 1
                    result.save()

                result.total_votes = (
                        result.excellent_votes + result.verygood_votes + result.good_votes + result.fair_votes + result.poor_votes)
                result.save()

            comment_text1 = request.POST.get("comment_1")
            comment_text2 = request.POST.get("comment_2")
            comment_text3 = request.POST.get("comment_3")
            comment_text4 = request.POST.get("comment_4")
            course.comment_set.create(comment_1=comment_text1,
                                      comment_2=comment_text2,
                                      comment_3=comment_text3,
                                      comment_4=comment_text4, )

            for done in d:
                if done.course == course:
                    if done.student == student:
                        done.done = 1
                        done.save()
            #return HttpResponseRedirect(reverse("/feedback/"+str(user.first_name)+"/"))
            #return HttpResponseRedirect(reverse("{% url 'feedback:index' user.first_name %}"))
            return render(request, 'feedback/submitted.html',{'key':student.key,})
        else:
            return render(request, 'feedback/questions2.html', {'result_list1': result_list[:5],
                                                                    'result_list2': result_list[5:10],
                                                                    'result_list3': result_list[10:14],
                                                                    'result_list4': result_list[14:19],
                                                                    'result_list5': result_list[19:21],
                                                                    'course': course,
                                                                    'professor': professor,
                                                                    'subject': subject,})
    else:
        return render(request, 'feedback/submitted.html',{'key':student.key,})



@login_required(login_url='/login/')
def analyse(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            professor_list = Professor.objects.all()
            return render(request, 'feedback/analyse.html', {'professor_list': professor_list})
        else:
            return HttpResponse("Not a valid memeber")
    else:
        return HttpResponse("Please Login First")


@login_required(login_url='/login/')
def courseanalyse(request, prof_pk):
    if request.user.is_authenticated():
        if request.user.is_staff:
            professor = Professor.objects.get(pk=prof_pk)
            course_list = professor.course_set.all()

            return render(request, 'feedback/courseanalyse.html', {'course_list': course_list, 'professor': professor})
        else:
            return HttpResponse("Not a valid memeber")
    else:
        return HttpResponse("Please Login First")


def getmail(request):
    email = request.POST.get('email')
    if not email in [user.username for user in User.objects.all()]:
        return render(request, 'feedback/invalid.html')
    else:
        s = Student.objects.filter(email = email)
        key = s[0].key
        text = "Submit the coursefeedback form by clicking this link: http://10.1.1.239/feedback/"+key+"/ or http://14.139.41.172/feedback/"+key+"/"
        send_mail('Course Feedback Portal', text, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        #return HttpResponse("<b>An email has been sent to your email address.Please Follow the link in the email</b>")
        return render(request, 'feedback/sentmail.html')
