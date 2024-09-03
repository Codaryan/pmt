from rest_framework import serializers
from .models import Client,Project,ProjectUser

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    users = ProjectUserSerializer(many=True)   
    
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        request_data = dict(self.context["request"].data)
        req_users = request_data["users"]
        creator = self.context["request"].user
        # print(req_users)
        users = validated_data.pop('users')
        validated_data["created_by"] = creator        
        user_instance = Project.objects.create(**validated_data)           
        # for user in users:           
        #     ProjectUser.objects.create(project_users=user_instance,**user)

        for user in req_users: 
            if "id" in user.keys():
                if ProjectUser.objects.filter(id=user['id']).exists():
                    existing_user_instance = Project.objects.get(id=user['id'])
                    print(user)
                    print(existing_user_instance)
                    ProjectUser.objects.update(project_users=user_instance,**user)
                else:
                    user["created_by"] = creator
                    ProjectUser.objects.create(project_users=user_instance,**user)
        return user_instance

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user = self.context["request"].user
        # print(f"User is: {user}")        
        
        projects = validated_data.pop('projects')
        # print(dict(validated_data))
        validated_data["created_by"] = user        
        client_instance = Client.objects.create(**validated_data)
        for project in projects:
            print(client_instance)
            print(project)
            Project.objects.create(client_project=client_instance,**project)
        return client_instance