from django.shortcuts import render

__all__ = [
    "profile",
]

def profile(request, username):
    context = {
        'username': username,
    }

    return render(request, 'member/profile.html', context)
