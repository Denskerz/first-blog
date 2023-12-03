from django.urls import reverse_lazy
from django.views.generic import (
   ListView,
   DetailView,
   CreateView, #Импортируем дополнительное представление для создания записей.
   UpdateView, #Импортируем дополнительное представление для обновления записей.
   DeleteView, #Импортируем дополнительное представление для удаления записей.
)
 
from .models import Entry
 
class EntryListView(ListView):
   model = Entry
   queryset = Entry.objects.all().order_by("-date_created") #Это ключевой запрос — он возвращает все существующие записи по нашему первичному ключу, сортируя их по дате создания.
 
class EntryDetailView(DetailView): #Дополнительно создаём представление с подклассом DetailView. Будем использовать его позже.
   model = Entry
 
class EntryCreateView(CreateView):
   model = Entry
   fields = ["title", "content"] #Указываем на то, какие поля должны будут отображаться в форме при создании новой записи. Дату не указываем, так как она формируется автоматически.
   success_url = reverse_lazy("entry-list")
 
class EntryUpdateView(UpdateView):
   model = Entry
   fields = ["title", "content"] #Указываем на то, какие поля должны будут отображаться в форме при обновлении существующих записей.
 
   def get_success_url(self): #Создаём функцию, которая даёт возможность пользователю остаться на странице с подробным отображением записи после завершения её редактирования.
       return reverse_lazy(
           "entry-detail",
           kwargs={"pk": self.entry.id}
       )
 
class EntryDeleteView(DeleteView):
   model = Entry
   success_url = reverse_lazy("entry-list")
