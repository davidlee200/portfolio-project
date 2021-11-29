from django.urls import path, include
# from django.conf.urls.static import static
from . import views


urlpatterns = [
                # path('scores',views.scores_view, name='scores'),
                # path('create', views.create_course, name='create_course'),
                # path('enter-score', views.enter_score, name='enter_scores'),
                path('home', views.ScoreList.as_view(), name='home'),
                path('details/<int:pk>/', views.ScoreDetail.as_view(), name='details'),
                path('create-play/', views.ScoreCreate.as_view(), name='create-play'),
                path('create-lesson/', views.LessonCreate.as_view(), name='create-lesson'),
                path('create-course/', views.CourseCreate.as_view(), name='create-course'),
                # path('create-generice/', views.CourseCreate.as_view(), name='create-course'),
                path('update-play/<int:pk>/', views.scoreUpdate.as_view(), name='update-round'),
                path('update-lesson/<int:pk>/', views.lessonUpdate.as_view(), name='update-lesson'),
                path('update-course/<int:pk>/', views.courseUpdate.as_view(), name='update-course'),
                path('delete-play/<int:pk>/', views.scoreDelete.as_view(), name='delete-round'),
                path('delete-lesson/<int:pk>/', views.lessonDelete.as_view(), name='delete-lesson'),
                path('delete-course/<int:pk>/', views.courseDelete.as_view(), name='delete-course'),
              ]
