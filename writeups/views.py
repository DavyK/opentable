import calendar
import datetime


from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Count

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

    pages = [i+1 for i in range(paginator.num_pages)]

    try:
        writeups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        writeups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        writeups = paginator.page(paginator.num_pages)

    tmp = Comment.objects.values('writeup').annotate(the_count=Count('writeup'))
    counts = {}
    for c in tmp:
        counts[c['writeup']] = c['the_count']

    comment_counts = []
    for w in writeups.object_list:
        try:
            comment_counts.append(counts[w.id])
        except KeyError:
            comment_counts.append(0)

    writeups_and_comment_counts = zip(writeups, comment_counts)

    data = {'writeups': writeups,'pages': pages, 'writeups_and_comment_counts': writeups_and_comment_counts}

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

    data = {'this_writeup': this_writeup, 'this_writeup_comments':this_writeup_comments}

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


    data = {'writeup_form': writeup_form}

    return render_to_response('writeups/add_writeup.html', data, context_instance=RequestContext(request))


def delete_writeup(request, writeup_id):

    this_writeup = Writeup.objects.get(pk=writeup_id)
    this_writeup.delete()

    return HttpResponseRedirect('/writeups/listWriteups/')


########################################################################################################################
# Comment Views
########################################################################################################################

def add_comment(request, writeup_id, comment_id=None):

    data = {}
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

    pages = [i+1 for i in range(paginator.num_pages)]

    try:
        summaries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        summaries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        summaries = paginator.page(paginator.num_pages)


    data = {'summaries': summaries, 'pages': pages}

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
    data = {'this_summary': this_summary}
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

    data = {'summary_form': summary_form}

    return render_to_response('writeups/add_summary.html', data, context_instance=RequestContext(request))


def delete_summary(request, summary_id):
    this_summary = SessionSummary.objects.get(pk=summary_id)
    this_summary.delete()
    redirect_url = '/writeups/listSummaries/'
    return HttpResponseRedirect(redirect_url)










