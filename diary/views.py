from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(LoginRequiredMixin,generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


def update(request, pk):
    # urlのpkを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # フォームに、取得したDayを紐付ける
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request, pk):
    # urlのpkを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'diary/day_confirm_delete.html', context)


def detail(request, pk):
    # urlのpkを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'diary/day_detail.html', context)
