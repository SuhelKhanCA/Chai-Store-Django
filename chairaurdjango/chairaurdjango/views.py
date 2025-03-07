from django.shortcuts import render, redirect
from chai.models import Review, ChaiVariety
from django.contrib import messages

def home(request):
    chais = ChaiVariety.objects.all()
    reviews = Review.objects.all()[:6]
    print(chais)
    print(reviews)
    context = {
        'reviews': reviews,
        'chais': chais
    }
    return render(request, 'website/index.html', context=context)

def about(request):
    return render(request, 'website/our_story.html')

def locations(request):
    
    return render(request, 'website/locations.html')

def reviews(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            review_text = request.POST.get('review')
            rating = int(request.POST.get('rating'))
            
            # Create new review
            review = Review.objects.create(
                author=name,
                review_text=review_text,
                rating=rating
            )
            
            messages.success(request, 'Thank you for your review!')
            return redirect('home')
            
        except Exception as e:
            messages.error(request, 'Something went wrong. Please try again.')
            
    return render(request, 'website/review.html')

