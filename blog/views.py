from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext, Context
from django.http import HttpResponse, Http404
from .models import Article, Comment, Tag, Image
# for the contact page email form:
from .forms import ContactForm, SubscribeForm, CommentForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

def about(request):
  return render(request, 'about/about.html')

def article(request, article_id):
  article = get_object_or_404(Article, pk=article_id)
  image = Image.objects.get(article=article_id)
  comments = Comment.objects.filter(article=article_id).order_by('-date_posted')
  comment_form_class = CommentForm
  if request.method == "POST":
    comment_form = comment_form_class(data=request.POST)
    new_comment = comment_form.save(commit=False)
    new_comment.article = article
    new_comment.save()
    messages.add_message(request, messages.INFO, 'Your comment has been added')
  return render(request, 'article/article.html', {
    'article': article,  
    'image': image,
    'comments': comments, 
    'comment_form': comment_form_class, 
  })

# This is for the subscription form on the sidebar
def base(request):
  tag = get_list_or_404(Tag)
  form_class = SubscribeForm
  if request.method == 'POST':
    form = form_class(data=request.POST)
    if form.is_valid():
      contact_email = request.POST.get('contact_email', '')
      template = get_template('main/subscription_request_template.txt')
      context = Context({'contact_email': contact_email})
      content = template.render(context)
      email = EmailMessage(
        "New subscription request",
        content,
        "Jenn's Little Island Blog" +'',
        ['jennifertigner@gmail.com']
      )
      email.send()
  return render(request, 'main/base.html', {
    'tag': tag,
    'form': form_class
  })

def browse(request, tag_word):
  tag = get_object_or_404(Tag, tag_text=tag_word)
  article_list = tag.article_set.all()
  all_images = Image.objects.all()
  return render(request, 'browse/browse.html', {
    'tag': tag,
    'article_list': article_list, 
    'all_images': all_images
  })

def contact(request):
  form_class = ContactForm
  if request.method == 'POST':
    form = form_class(data=request.POST)
    # checks if info is valid
    if form.is_valid():
      # puts email template together
      contact_name = request.POST.get('contact_name', '')
      contact_email = request.POST.get('contact_email', '')
      form_content = request.POST.get('content', '')
      template = get_template('contact/contact_email_template.txt')
      context = Context({
        'contact_name': contact_name,
        'contact_email': contact_email,
        'form_content': form_content,
      })
      content = template.render(context)
      # Email the profile with the contact information
      email = EmailMessage(
        "New contact form submission",
        content,
        "Jenn's Little Island Blog" +'',
        ['jennifertigner@gmail.com'],
        headers = {'Reply-To': contact_email }
      )
      email.send()
      messages.add_message(request, messages.INFO, 'Thanks for the message!')
      return redirect('contact')
  return render(request, 'contact/contact.html', {
    'form': form_class
  })

def index(request):
  all_articles = get_list_or_404(Article)
  all_comments = Comment.objects.all()
  all_images = Image.objects.all()
  return render(request, 'main/index.html', {
    'all_articles': all_articles,
    'all_comments': all_comments, 
    'all_images': all_images
  })

# ERRORS:

def handler400(request):
  response = render(request, 'error/400.html',
  context_instance=RequestContext(request))
  response.status_code = 400
  return response

def handler403(request):
  response = render(request, 'error/403.html',
  context_instance=RequestContext(request))
  response.status_code = 403
  return response

def handler404(request):
  response = render(request, 'error/404.html',
  context_instance=RequestContext(request))
  response.status_code = 404
  return response

def handler500(request):
  response = render(request, 'error/500.html',
  context_instance=RequestContext(request))
  response.status_code = 500
  return response
