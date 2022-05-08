from logging import exception
from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import BookForm, ContactForm
from .models import *
from django.contrib import messages #Library for alert messages
from django.core.mail import send_mail #Library for sending mail
from datetime import datetime
#For Pdf Generation
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# Create your views here.
def homepage(request):
    #@desc The first few lines of code is to search an element from the database.
    #In case the user haven't searched anything, all the books are listed
    #https://www.youtube.com/watch?v=CPXe3MI8uiE
    if 'searchbar' in request.GET:
        items = request.GET['searchbar']
        books = Book.objects.filter(book_name__icontains = items) #Fetching books from the database and displays in home based on search argument
        print(books)
        if not books:
            books = Book.objects.filter(author_name__icontains = items)
    else:
        books = Book.objects.all()
    context = {'books':books}
    return render(request,'crud_operation/homepage.html',context)


def book_register(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.info(request, "Book has been successfully uploaded.")
            return redirect('/')
        else :
            return render(request, 'crud_operation/book_form.html', context) 
    else:
        form = BookForm()
        context = {'form':form}
        return render(request,'crud_operation/book_form.html',context)


def book_delete(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('/')
    if request.method == 'POST':
        book.delete()
        messages.info(request, "Book has been removed.")
        return redirect('/')
    return render(request, 'crud_operation/delete.html')


def book_update(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('/')
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.info(request, "Book has been successfully updated")
            return redirect('/')
    else:
        context = {'form':form}
        return render(request, 'crud_operation/book_form.html',context)


def book_details(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('/')
    context = {'book':book}
    return render(request, 'crud_operation/book_details.html',context)

def book_download(request,pk):
    # Create the HttpResponse object 
    response = HttpResponse(content_type='application/pdf')
    book = Book.objects.get(id=pk)
    bookname = book.book_name
    publisheddate = datetime.date(book.published_on)
    generated_on = datetime.today()
    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(bookname) 
    # READ Optional GET param
    #get_param = request.GET.get('name', 'World')
    p = canvas.Canvas(response)
    # Write content on the PDF 
    cm=100
    p.drawString(240, 800, bookname)
    p.drawString(100, 360, "Description: ")
    p.drawString(100,340,'{} is an {} novel, Written by {}'.format(bookname,book.Language,book.author_name))
    p.drawString(100,320,'The book was published on {} through {} publishers.'.format(publisheddate,book.publisher))
    p.drawString(370,10,'Timestamp: {}'.format(generated_on))
    #Render Image on the pdf
    bookimage = book.image
    logo = ImageReader(bookimage)
    p.drawImage(logo,100,380,mask='auto', width=4*cm,height=4*cm)
    # Close the PDF object. 
    p.showPage() 
    p.save() 
    # Show the result to the user    
    return response

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_no = form.cleaned_data.get('phone_no')
            description = form.cleaned_data.get('description')
            subject = 'Regarding Contact information'
            send_mail(subject,description,'mohammedsaleek123@gmail.com',[email],fail_silently=False) #Email
            form.save()
            return redirect('/')
        else:
            return render(request,'crud_operation/contact_us.html',context)
    else:
        form = ContactForm()
        context = {'form':form}
        return render(request, 'crud_operation/contact_us.html',context)