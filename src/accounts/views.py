# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Company, Comment
from .forms import CommentForm

def company_detail(request, slug):
    template_name = 'company_detail.html'
    company = get_object_or_404(Company, slug=slug)
    comments = company.comments.filter(active=True)
    new_comment = None 
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        # if comment_form.is_valid(): this can be used to add CSRF token validation
 
        # Create Comment object but don't save to database yet
        new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        new_comment.company = company
            # Save the comment to the database
        new_comment.save()
    else:
        comment_form = CommentForm()  
 
    return render(request, template_name, {'company': Company,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class companyListView(ListView):
    model = Company
    template_name = 'company_list.html' 

class companyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'