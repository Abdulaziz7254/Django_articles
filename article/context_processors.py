from .form import LoginForm, RegistrationForm, SuggestionForm, CommentForm, EditProfileForm

def global_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegistrationForm(),
        'suggestion_form': SuggestionForm(),
        'comment_form': CommentForm(),
        'edit_profile_form': EditProfileForm()



    }
