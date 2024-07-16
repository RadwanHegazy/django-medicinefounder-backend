from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError
from users.models import User

class UserTokens :

    @property
    def tokens (self) : 
        user_token = RefreshToken.for_user(self.user)
        data = {
            'refresh_token' : str(user_token),
            'access_token' : str(user_token.access_token),
        }
        return data
    

class RegisterSerializer (serializers.ModelSerializer, UserTokens):
    class Meta:
        model = User
        fields = ('full_name','email','password','pharmcy_name','whats_app_number',)

    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        self.user.save()
        return self.user
    
class LoginSerializer(serializers.Serializer, UserTokens):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try :
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid email"
            })
        
        if not self.user.check_password(password): 
            raise ValidationError({
                'message' : "invalid password"
            })
            
        return attrs
    
    