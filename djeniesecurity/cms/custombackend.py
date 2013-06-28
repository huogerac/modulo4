from django.contrib.auth.models import User


class SMSBackend:
    def authenticate(self, username=None, password=None):
        
        try:
            # Try to find a user matching your username
            user = User.objects.get(username=username)

            #  Check the password is the reverse of the username
            if password == username[::-1]:
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None
        
        

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None                
        
