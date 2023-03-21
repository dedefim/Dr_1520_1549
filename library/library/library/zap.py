import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Users, TODO
class TodoType(DjangoObjectType):

    class Meta:
        model = TODO
        fields = '__all__'
class Query(graphene.ObjectType):
    all_books = graphene.List(TodoType)
    def resolve_all_books(root, info):
        return TODO.objects.all()
schema = graphene.Schema(query=Query)


class Query(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, ferst_name=graphene.Int(required=True))
    Todo_by_id = graphene.Field(TodoType, Project=graphene.Int(required=True))
    def resolve_users_by_id(self, info, ferst_name, Project):
        try:
            return Users.objects.get(ferst_name=ferst_name), TODO.objects.get(Project=Project)
        except Users.DoesNotExist:
            return None