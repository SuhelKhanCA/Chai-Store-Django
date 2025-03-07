from django.shortcuts import render, redirect
from chai.models import Review, ChaiVariety
from django.contrib import messages

def index(request):
    chais = ChaiVariety.objects.all()
    reviews = Review.objects.all().order_by('-id')[:6]
    context = {
        'reviews': reviews,
        'chais': chais
    }
    return render(request, 'website/index.html', context)

def about(request):
    return render(request, 'website/our_story.html')

def menu(request):
    return render(request, 'website/menu.html')

def locations(request):
    return render(request, 'website/locations.html')

def review(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            review_text = request.POST.get('review')
            rating = int(request.POST.get('rating'))
            
            Review.objects.create(
                author=name,
                review_text=review_text,
                rating=rating
            )
            
            messages.success(request, 'Thank you for your review!')
            # return redirect('index')
            
        except Exception as e:
            messages.error(request, 'Something went wrong. Please try again.')
            
    return render(request, 'website/review.html')