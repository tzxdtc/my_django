from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'employee/employee_list.html'
