from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model( )
        fields = UserCreationForm.Meta.fields + ('email',)  
        # 존재하는 것만 email처럼 추가할 수 있음. migration의 user의 field에서 추가할 수 있는 것을 확인할 수 있음.


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
        # userchangeform전부를 가져오면 관리자로 바꿀 수 있게 해버리는등 보여지면 안되는 것까지 보여지게 됨. 때문에 여기서는 필드를 지정해줌.
        # 비밀번호 변경 폼은 따로 있어서 여기선 보여지지 않음.
        