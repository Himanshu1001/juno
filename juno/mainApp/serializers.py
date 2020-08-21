from rest_framework import serializers
from mainApp.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name','password','username',)
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		username = validated_data.pop('username')
		password = validated_data.pop('password')
		if not User.objects.filter(username = username).exists():
			if PhoneOTP.objects.filter(phone_number = username,is_verified=True).exists():
				user, created = User.objects.get_or_create(username = username,**validated_data)
				user.set_password(password)
				user.save()
				return user
			raise serializers.ValidationError("Phone number not verified")		
		raise serializers.ValidationError("User already exist")

class Custom_UserSerializer(serializers.ModelSerializer):
	user = UserSerializer(required = True)
	# verified = VerifySerializer(read_only = True)
	class Meta:
		model = Custom_User
		fields = '__all__'
		depth = 1

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = UserSerializer.create(UserSerializer(), validated_data=user_data)
		# verified = Verify().save()
		custom_user, created = Custom_User.objects.update_or_create(user=user,**validated_data)
		return custom_user
		
	def update(self,instance, validated_data):
		user_data = validated_data.pop('user')
		user = instance.user
		user.first_name = user_data.get('first_name',user.first_name)
		user.last_name = user_data.get('last_name',user.last_name)
		user.email = user_data.get('email',user.email)
		user.save()
		return instance

class UserTasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserTasks
		fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Content
		fields = '__all__'

class ChallangesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Challanges
		fields = '__all__'

class UserChallangesSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserChallanges
		fields = '__all__'