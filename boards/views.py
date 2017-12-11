from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from boards.models import Board, Topic, Post
from django.contrib.auth.models import User
from boards.forms import NewTopicForm
from django.contrib.auth.decorators import login_required


# Create your views here.



def index(request):
	
	boards = Board.objects.all()

	context = {'boards': boards}

	boards_list = []

	# for board in boards:
	# 	boards_list.append(board.name)

	# msg = '<br>'.join(boards_list)

	return render(request, 'home.html', context)



def board_topics(request, pk):
	
	board = get_object_or_404(Board, pk=pk)
	
	# try:
	# 	board = Board.objects.get(pk=pk)
	# except Board.DoesNotExist:
	# 	raise Http404

	context = {'board': board}

	return render(request, 'topics.html', context)


@login_required
def new_topic(request, pk):

	board = get_object_or_404(Board, pk=pk)

	# user = User.objects.first()
	# print (user, "gotten user")

	# Form implementation crud way 
	# board = get_object_or_404(Board, pk=pk)

	# if request.method == 'POST':
	# 	subject = request.POST['subject']
	# 	message = request.POST['message']

	# 	user = User.objects.first()

	# 	topic = Topic.objects.create(
	# 		subject=subject,
	# 		board=board,
	# 		starter=user
	# 		)

	# 	post = Post.objects.create(
	# 		message=message,
	# 		topic=topic,
	# 		created_by=user
	# 		)

	# 	return redirect('board_topics', pk=board.pk)

	if request.method == 'POST':
		form = NewTopicForm(request.POST)

		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = request.user

			topic = form.save()

			post = Post.objects.create(
				topic=topic,
				message=form.cleaned_data['message'],
				created_by=request.user
				)

			return redirect('board_topics', pk=board.pk)

	else:
		form = NewTopicForm()


	context = {'board': board, 'form': form}

	return render(request, 'new_topic.html', context)











