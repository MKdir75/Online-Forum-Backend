from fastapi import APIRouter

router = APIRouter()

@router.post("/ban")
def ban_user(user_id: int):
    return {"msg": f"User {user_id} banned"}

@router.post("/report")
def report_post(post_id: int):
    return {"msg": f"Post {post_id} reported"}
