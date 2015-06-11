from django.contrib import admin
from .models import Student, Course, Question, Result, Subject, Professor, Done, Comment

class DoneInline(admin.TabularInline):
    model = Done

class QuestionInline(admin.TabularInline):
    model = Question

class CourseInline(admin.TabularInline):
    model = Course


class ResultInline(admin.TabularInline):
     model = Result

class CommentInline(admin.TabularInline):
    model = Comment

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('roll_no', 'student_date', 'was_published_recently')
    list_filter = ['roll_no']
    search_fields = ['roll_no']
    inlines = [DoneInline,]

class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    filter_horizontal = ('students',)
    list_display = ('subject_code', 'subject_date', 'was_published_recently')
    list_filter = ['subject_date']
    search_fields = ['subject_code']
    inlines = [CourseInline,]

class CourseAdmin(admin.ModelAdmin):
    model = Course
    #inlines = [DoneInline,ResultInline,CommentInline]
    inlines = [ResultInline,CommentInline]

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ResultInline,]
    list_display = ('question_text', 'question_date', 'was_published_recently')
    list_filter = ['question_date']
    search_fields = ['question_text']

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ('prof_name','prof_date', 'was_published_recently')
    list_filter = ['prof_date']
    search_fields = ['prof_name']
    inlines = [CourseInline,]

class DoneAdmin(admin.ModelAdmin):
    search_fields = ['course']

class ResultAdmin(admin.ModelAdmin):
    search_fields = ['']

admin.site.register(Done,DoneAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Comment)

