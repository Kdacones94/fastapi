from neomodel import StructuredNode, StringProperty, RelationshipTo

class User(StructuredNode):
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    friends = RelationshipTo('User', 'FRIEND')

# Example of creating a user node
def create_user(username: str, email: str):
    user = User(username=username, email=email)
    user.save()
    return user

# Example of querying a user node
def get_user_by_username(username: str):
    return User.nodes.get(username=username)