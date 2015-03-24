import calendar, datetime

from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from opentable.views import get_writeup_archive
from writeups.models import Writeup, Comment
from writeups.forms import WriteupForm, CommentForm
from characters.models import Character


def list_writeups(request, query_set=None):

    """
    View the most 5 recently submitted posts along with number of comments in paginated .
    """
    page = request.GET.get('page')

    if query_set is None:
        writeup_queryset = Writeup.objects.all()
    else:
        writeup_queryset = query_set

    paginator = Paginator(writeup_queryset, 10)

    try:
        writeups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        writeups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        writeups = paginator.page(paginator.num_pages)

    characters = Character.objects.all()
    data = {'characters': characters, 'writeups': writeups, 'archive': get_writeup_archive()}

    return render_to_response('writeups/index_writeups.html', data, context_instance=RequestContext(request))


def archive_list_writeups(request, w_month, w_year):

    year = int(w_year)
    month = int(w_month)
    month_range = calendar.monthrange(year, month)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=year, month=month, day=month_range[1])

    writeup_queryset = Writeup.objects.filter(submission_date__range=(start.date(), end.date()))
    return list_writeups(request, query_set=writeup_queryset)


def character_list_writeups(request, character_id):
    writeup_queryset = Writeup.objects.filter(author_character__id=character_id)
    return list_writeups(request, query_set=writeup_queryset)


def show_writeup(request, writeup_id, comment_id=None):

    this_writeup = Writeup.objects.get(pk=writeup_id)
    this_writeup_comments = Comment.objects.filter(writeup__id=writeup_id).order_by('submission_date')
    
    if comment_id is not None:
        this_comment = Comment.objects.get(pk=comment_id)

    if request.method == "POST":
        if comment_id is not None:
            comment_form = CommentForm(request.POST, instance=this_comment)
        else:
            comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
                save_it = comment_form.save(commit=False)
                save_it.author = request.user
                save_it.writeup = this_writeup
                save_it.save()

                redirect_to_url = '/writeups/showWriteup/' + writeup_id + '/'
                return HttpResponseRedirect(redirect_to_url)
    else:
        if comment_id is not None:
            comment_form = CommentForm(instance=this_comment)
        else:
            comment_form = CommentForm(None)

    comment_form.helper.form_action = '/writeups/addComment/' + writeup_id + '/'

    if comment_id is not None:
        comment_form.helper.form_action = '/writeups/editComment/' + writeup_id + '/' + comment_id + '/'

    characters = Character.objects.all()

    data = {'this_writeup': this_writeup, 'this_writeup_comments':this_writeup_comments, 'characters': characters, 'archive': get_writeup_archive()}

    if request.user.is_authenticated():
        data['comment_form'] = comment_form

    return render_to_response('writeups/show_writeup.html', data, context_instance=RequestContext(request))


@login_required
def add_writeup(request, writeup_id=None):
    
    if writeup_id is not None:
        this_writeup = Writeup.objects.get(pk=writeup_id)

    if request.method == "POST":
        if writeup_id is not None:
            writeup_form = WriteupForm(request.POST,  instance=this_writeup)
        else:
            writeup_form = WriteupForm(request.POST)

        if writeup_form.is_valid():
            save_it = writeup_form.save(commit=False)
            save_it.save()

            return HttpResponseRedirect('/writeups/listWriteups/')

    else:
        if writeup_id is not None:
            writeup_form = WriteupForm(instance=this_writeup)
        else:
            writeup_form = WriteupForm(None)

    if writeup_id is not None:
        writeup_form.helper.form_action = '/writeups/editWriteup/' + writeup_id + '/'

    characters = Character.objects.all()
    writeups = Writeup.objects.all()
    data = {'writeup_form': writeup_form, 'characters': characters, 'writeups': writeups, 'archive': get_writeup_archive()}

    return render_to_response('writeups/add_writeup.html', data, context_instance=RequestContext(request))


def delete_writeup(request, writeup_id):

    this_writeup = Writeup.objects.get(pk=writeup_id)
    this_writeup.delete()

    return HttpResponseRedirect('/writeups/listWriteups/')


def add_comment(request, writeup_id, comment_id=None):
    characters = Character.objects.all()
    writeups = Writeup.objects.all()
    data = { 'characters': characters, 'writeups': writeups, 'archive': get_writeup_archive()}

    url_to_render = '/writeups/showWriteup/' + writeup_id + '/'

    return render_to_response(url_to_render, data, context_instance=RequestContext(request))


def delete_comment(request, writeup_id, comment_id):
    this_comment = Comment.objects.get(pk=comment_id)
    this_comment.delete()
    redirect_url = '/writeups/showWriteup/' + writeup_id + '/'
    return HttpResponseRedirect(redirect_url)









