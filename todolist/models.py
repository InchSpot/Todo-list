from django.utils import timezone #мы будем получать дату создания todo
from django.db import models 

class Status(models.Model): # Таблица категория которая наследует models.Model
	PENDING = 'Pn'
	DONE = 'D'
	IN_PROCESS = 'IP'
	PROCESSING_STATUS = [
		(PENDING, 'В ожидании выполнения'),
		(DONE, 'Выполнено'),
		(IN_PROCESS, 'Выполняется'),
		]
	name = models.CharField(max_length=100, choices = PROCESSING_STATUS, default = PENDING) #varchar.Нам потребуется только имя категории
	class Meta:
		verbose_name = ("Status") # человекочитаемое имя объекта
		verbose_name_plural = ("Statuses")  #человекочитаемое множественное имя для Категорий
	def __str__(self):
		return self.name # __str__ применяется для отображения объекта в интерфейсе

class Priority(models.Model): # Таблица категория которая наследует models.Model
	HIGH_PRIORITY = 'HP'
	MED_PRIORITY = 'MP'
	LOW_PRIORITY = 'LP'
	TASK_PRIORITY = [
		(HIGH_PRIORITY, 'Высокий приоритет'),
		(MED_PRIORITY, 'Средний приоритет'),
		(LOW_PRIORITY, 'Низкий приоритет'),
	]	
	name = models.CharField(max_length=100, choices = TASK_PRIORITY, default=HIGH_PRIORITY) #varchar.Нам потребуется только имя категории
	class Meta:
		verbose_name = ("Priority") # человекочитаемое имя объекта
		verbose_name_plural = ("Priorities")  #человекочитаемое множественное имя для Категорий
	def __str__(self):
		return self.name  # __str__ применяется для отображения объекта в интерфейсе

class TodoList(models.Model):	
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True) #текстовое поле
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #до какой даты нужно было сделать дело
	status = models.ForeignKey(Status,on_delete=models.PROTECT)
	priority = models.ForeignKey(Priority,on_delete=models.PROTECT)	
	class Meta: #используем вспомогательный класс мета для сортировки наших дел
		ordering = ["-due_date"] #сортировка дел по времени их создания
	def __str__(self):
		return self.title