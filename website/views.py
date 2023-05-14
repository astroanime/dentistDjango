from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,OfferMediaForm,ReviewForm,ServiceForm
from io import BytesIO
from PIL import Image
from .models import Appointment, Stuff,Servise,Offer,Review,Doctor,Article
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.core.files.images import ImageFile
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .utils import average_rating
from django.http import HttpResponseRedirect
#def appointment_list(request):
	#return render(request, 'appointment_list.html', {})
class AppointmentList(ListView):
	model = Appointment
def regis(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Accaunt was created for ' + user)

			return redirect('login')
	context = {'form':form}
	return render(request, 'auth/regis.html', context)
def home(request):
    offers= Offer.objects.all()
    offerss= []
    for offer in offers:
        offerss.append({"service": offer})
    services= Servise.objects.all()
    servises = []
    for service in services:
        servises.append({"service": service})
    doctors= Doctor.objects.all()
    doctor_list = []
    for doc in doctors:
        doctor_list.append({"doc": doc})
    return render(request, "home.html", {"servise_list": servises,"doctor_list": doctor_list, "offer_list": offerss})
def userPage(request):
	return render(request, 'UserPage.html', {})

def news_list(request):
    news = Article.objects.all()
    articles = []
    for new in news:
        reviews = new.review_set.all()
        if reviews:
            number_of_reviews = len(reviews)
        else:
            number_of_reviews = 0
        articles.append({"new": new,"number_of_reviews": number_of_reviews})

    context = {
        "news_list": articles
    }
    return render(request, "news.html", context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password is incorrect')
			return render(request, 'auth/login.html', {})


	context = {}
	return render(request, 'auth/login.html', context)	

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		your_schedule = request.POST['your-schedule']


		appointment = "Name: " + message_name + " Email: " + message_email + " Message: " + message + "Time: " + your_schedule

		if message is not None:
			send_mail(
				('abeuov.o0705@gmail.com'),
				appointment,
				settings.EMAIL_HOST_USER,
				 #To email
				 ['abeuov.o0705@gmail.com'],
				 fail_silently=False,
				),
		
			return render(request, 'appointment.html', {
				'message_name' : message_name,
				'message_email' : message_email,
				'message' : message,
				'your_schedule' : your_schedule 
				})
		else:
			messages.error(request, 'You need add something to make booking')
			return render(request, 'contact.html', {})

	else:
		return render(request, 'contact.html', {})



def about(request):
	return render(request, 'about.html', {})
def pricing(request):
    services= Servise.objects.all()
    servises = []
    for service in services:
        servises.append({"service": service})
    stuffs= Stuff.objects.all()
    doctors = []
    for stuff in stuffs:
        doctors.append({"stuff": stuff})
    return render(request, "pricing.html", {"servise_list": servises,"doctors": doctors })

def service(request):
    services= Offer.objects.all()
    servises = []
    for service in services:
        servises.append({"service": service})
    return render(request, "service.html", {"offer_list": servises})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']
		return render(request, 'appointment.html', {'your_schedule'})
	else:
		return render(request, 'appointment.html', {})


def book_media(request, pk):
    book = get_object_or_404(Offer, pk=pk)

    if request.method == "POST":
        form = OfferMediaForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book = form.save(False)
            cover = form.cleaned_data.get("cover")
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            if cover:
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)
            book.name=name
            book.description = description
            book.save()
            messages.success(request, "Book \"{}\" was successfully updated.".format(book))
            return redirect("service")
    else:
        form = OfferMediaForm(instance=book)

    return render(request, "instance-form.html",
                  {"instance": book, "form": form, "model_type": "Book", "is_file_upload": True})

@login_required
def review_edit(request, offer_pk, review_pk=None):
    offer = get_object_or_404(Offer, pk=offer_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=offer_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            updated_review = form.save(False)
            updated_review.offer = offer
            if review is None:
                messages.success(request, "Comment for \"{}\" created.".format(offer))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Comment for \"{}\" updated.".format(offer))

            updated_review.save()

            return redirect("news")
    else:
        form = ReviewForm(instance=review)

    return render(request, "instance-form.html",
                  {"form": form,
                   "instance": review,
                   "model_type": "Review",
                   "related_instance": offer,
                   "related_model_type": "Offer"
                   })

def create_service(request):
    submitted = False
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(False)
            cover = form.cleaned_data.get("cover")
            if cover:
                image = Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                service.cover.save(cover.name, image_file)
            service.save()
            return redirect('service')
    
    form = ServiceForm()
    return render(request, "instance-form.html",
                  {"form": form,
                   "model_type": "Offer",
                   })
def logoutUser(request):
    logout(request)
    return redirect('home')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    reviews = article.review_set.all()
    if reviews:
        article_rating = average_rating([review.rating for review in reviews])
        context = {
            "article": article,
            "article_rating": article_rating,
            "reviews": reviews
        }
    else:
        context = {
            "article": article,
            "article_rating": None,
            "reviews": None
        }
    if request.user.is_authenticated:
        max_viewed_article_length = 10
        viewed_articles = request.session.get('viewed_articles', [])
        viewed_article = [article.id, article.name]
        if viewed_article in viewed_articles:
            viewed_articles.pop(viewed_articles.index(viewed_article))
        viewed_articles.insert(0, viewed_article)
        viewed_articles = viewed_articles[:max_viewed_article_length]
        request.session['viewed_articles'] = viewed_articles
    return render(request, "article.html", context)

def service_added(request,pk):
    service = get_object_or_404(Servise, pk=pk)
    if request.user.is_authenticated:
        max_added_services_length = 10
        added_services = request.session.get('added_services', [])
        added_service = [service.name, service.quantity, service.price,]
        if added_service in added_services:
            added_services.pop(added_services.index(added_service))
        added_services.insert(0, added_service)
        added_services = added_services[:max_added_services_length]
        request.session['added_services'] = added_services
    messages.success(request, "Service \"{}\" was added.".format(service))
    return redirect("pricing")