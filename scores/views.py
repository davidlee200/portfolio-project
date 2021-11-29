from django.shortcuts import render
from .models import Scores_Out,lesson,Course_model
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class ScoreList(ListView):
    model = Scores_Out
    context_object_name = 'rounds'
    template_name = 'scores/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input =self.request.GET.get('search-area') or ''
        if search_input:
            context['rounds'] = context['rounds'].filter(
                        course_played__startswith = search_input)

        context['search_input'] = search_input
        context['lessons'] = lesson.objects.all()
        context['Course_model'] = Course_model.objects.all()
        return context



class GenericCreateView(CreateView):
    model = Scores_Out
    context_object_name = 'rounds'
    fields = '__all__'
    template_name = 'scores/addData.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input =self.request.GET.get('search-area') or ''
        if search_input:
            context['rounds'] = context['rounds'].filter(
                        course_played__startswith = search_input)

        context['search_input'] = search_input
        context['lessons'] = lesson.objects.all()
        context['Course_model'] = Course_model.objects.all()
        return context



class ScoreDetail(DetailView):
    model = Scores_Out
    context_object_name = 'rounds_detail'
    template_name = 'scores/roundDetail.html'
    def get_context_data(self, **kwargs):
        context = super(ScoreDetail,self).get_context_data(**kwargs)
        context['Course_model'] = Course_model.objects.all().filter(
                    course_played__startswith = 'Blarney')

        # context['cards'] = Scores_Out.objects.filter(pk=self.kwargs.get('pk')).select_related('course_played')

        context['cards'] = Scores_Out.objects.all().select_related('course_played')
        return context

class ScoreCreate(CreateView):

    model = Scores_Out
    template_name = 'scores/addData.html'
    fields = '__all__'

class LessonCreate(CreateView):

    model = lesson
    template_name = 'scores/addData.html'
    fields = '__all__'

class CourseCreate(CreateView):
    model = Course_model
    template_name = 'scores/addCourse.html'
    fields = '__all__'

class scoreUpdate(UpdateView):
    template_name = 'scores/addData.html'
    model = Scores_Out
    fields = '__all__'

class lessonUpdate(UpdateView):
    model = lesson
    template_name = 'scores/addData.html'
    fields = '__all__'

class courseUpdate(UpdateView):
    model = Course_model
    template_name = 'scores/addData.html'
    fields = '__all__'


class scoreDelete(DeleteView):
    template_name = 'scores/detele_comfirm.html'
    success_url = reverse_lazy('home')
    model = Scores_Out

class lessonDelete(DeleteView):
    template_name = 'scores/detele_comfirm.html'
    success_url = reverse_lazy('home')
    model = lesson

class courseDelete(DeleteView):
    template_name = 'scores/detele_comfirm.html'
    success_url = reverse_lazy('home')
    model = Course_model
