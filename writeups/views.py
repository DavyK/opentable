import calendar, datetime

from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from opentable.views import get_writeup_archive, get_summary_archive
from writeups.models import Writeup, Comment, SessionSummary
from writeups.forms import WriteupForm, CommentForm, SummaryForm
from characters.models import Character


########################################################################################################################
# Writeup Views
########################################################################################################################

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
    data = {'characters': characters, 'writeups': writeups,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

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

    data = {'this_writeup': this_writeup, 'this_writeup_comments':this_writeup_comments, 'characters': characters,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

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

            this_writeup = Writeup.objects.order_by('-last_edited')[0]
            redirect_to_url = '/writeups/showWriteup/{0}/'.format(this_writeup.id)

            return HttpResponseRedirect(redirect_to_url)

    else:
        if writeup_id is not None:
            writeup_form = WriteupForm(instance=this_writeup)
        else:
            writeup_form = WriteupForm(None)

    if writeup_id is not None:
        writeup_form.helper.form_action = '/writeups/editWriteup/' + writeup_id + '/'

    characters = Character.objects.all()
    writeups = Writeup.objects.all()
    data = {'writeup_form': writeup_form, 'characters': characters, 'writeups': writeups,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

    return render_to_response('writeups/add_writeup.html', data, context_instance=RequestContext(request))


def delete_writeup(request, writeup_id):

    this_writeup = Writeup.objects.get(pk=writeup_id)
    this_writeup.delete()

    return HttpResponseRedirect('/writeups/listWriteups/')


########################################################################################################################
# Comment Views
########################################################################################################################

def add_comment(request, writeup_id, comment_id=None):
    characters = Character.objects.all()
    writeups = Writeup.objects.all()
    data = { 'characters': characters, 'writeups': writeups,
             'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

    url_to_render = '/writeups/showWriteup/' + writeup_id + '/'

    return render_to_response(url_to_render, data, context_instance=RequestContext(request))


def delete_comment(request, writeup_id, comment_id):
    this_comment = Comment.objects.get(pk=comment_id)
    this_comment.delete()
    redirect_url = '/writeups/showWriteup/' + writeup_id + '/'
    return HttpResponseRedirect(redirect_url)


########################################################################################################################
# SessionSummary Views
########################################################################################################################

def list_summaries(request, query_set=None):
    """
    View the most 5 recently submitted session along with number of comments in paginated view.
    """
    page = request.GET.get('page')

    if query_set is None:
        summary_queryset = SessionSummary.objects.all()
    else:
        summary_queryset = query_set

    paginator = Paginator(summary_queryset, 10)

    try:
        summaries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        summaries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        summaries = paginator.page(paginator.num_pages)

    characters = Character.objects.all()
    data = {'characters': characters, 'summaries': summaries,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

    return render_to_response('writeups/index_summaries.html', data, context_instance=RequestContext(request))


def archive_list_summaries(request, s_month, s_year):

    year = int(s_year)
    month = int(s_month)
    month_range = calendar.monthrange(year, month)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=year, month=month, day=month_range[1])

    summary_queryset = SessionSummary.objects.filter(session_date__range=(start.date(), end.date()))
    return list_summaries(request, query_set=summary_queryset)


def character_list_summaries(request, character_id):
    summary_queryset = SessionSummary.objects.filter(session_characters__pk=character_id)
    return list_summaries(request, query_set=summary_queryset)


def show_summary(request, summary_id):
    this_summary = SessionSummary.objects.get(pk=summary_id)
    characters = Character.objects.all()
    data = {'this_summary': this_summary, 'characters': characters,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}
    return render_to_response('writeups/show_summary.html', data, context_instance=RequestContext(request))

@login_required
def add_summary(request, summary_id=None):
        
    if summary_id is not None:
        this_summary = SessionSummary.objects.get(pk=summary_id)

    if request.method == "POST":
        if summary_id is not None:
            summary_form = SummaryForm(request.POST,  instance=this_summary)
        else:
            summary_form = SummaryForm(request.POST)

        if summary_form.is_valid():
            save_it = summary_form.save(commit=False)
            save_it.save()
            summary_form.save_m2m()

            return HttpResponseRedirect('/writeups/listSummaries/')

    else:
        if summary_id is not None:
            summary_form = SummaryForm(instance=this_summary)
        else:
            summary_form = SummaryForm(None)

    if summary_id is not None:
        summary_form.helper.form_action = '/writeups/editSummary/' + summary_id + '/'

    characters = Character.objects.all()
    summaries = SessionSummary.objects.all()
    data = {'summary_form': summary_form, 'characters': characters, 'summaries': summaries,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

    return render_to_response('writeups/add_summary.html', data, context_instance=RequestContext(request))


def delete_summary(request, summary_id):
    this_summary = SessionSummary.objects.get(pk=summary_id)
    this_summary.delete()
    redirect_url = '/writeups/listSummaries/'
    return HttpResponseRedirect(redirect_url)










