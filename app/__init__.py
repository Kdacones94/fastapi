from fastapi import FastAPI

# Commented out model imports as they are not relevant to the current project
# from .user import User
# from .post import Post
# from .comment import Comment

# Commented out __all__ definition as it is not relevant to the current project
# __all__ = ["User", "Post", "Comment"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}