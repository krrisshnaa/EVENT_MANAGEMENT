from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event, Participant

# 🔷 Homepage: List of events
def events_list(request):
    events = Event.objects.filter(date__gte=now().date()).order_by('date')
    return render(request, 'events/events_list.html', {'events': events})

# 🔷 Event detail + registration
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        participant = Participant.objects.create(
            name=name,
            email=email,
            event=event
        )

        # send confirmation email
        send_mail(
            subject='Event Registration Confirmation',
            message=f'Thank you {name} for registering for {event.name}!',
            from_email='your_email@example.com',  # replace with your email
            recipient_list=[email],
            fail_silently=False,
        )

        return render(request, 'events/success.html', {
            'participant': participant,
            'event': event
        })

    return render(request, 'events/event_detail.html', {'event': event})

# 🔷 Success page
def success(request):
    return render(request, 'events/success.html')

# 🔷 User Registration page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})