from django.http import HttpResponse
import utils.cache.lru_cache as lru_cache


def index(request):
    return HttpResponse(f"You're at the cat index.")


def create_user(request):
    return HttpResponse(f"You're at the create_user.")


def update_user(request, user_id):
    return HttpResponse(f"You're at the update_user {user_id}.")


def read_user(request, user_id):
    return HttpResponse(f"You're at the read_user {user_id}.")


def delete_user(request, user_id):
    return HttpResponse(f"You're at the delete_user {user_id}.")


def create_cat(request):
    return HttpResponse(f"You're at the create_cat.")


def update_cat(request, cat_id):
    return HttpResponse(f"You're at the update_cat {cat_id}.")


def read_cat(request, cat_id):
    return HttpResponse(f"You're at the read_cat {cat_id}.")


def delete_cat(request, cat_id):
    return HttpResponse(f"You're at the delete_cat {cat_id}.")


def create_review(request):
    return HttpResponse(f"You're at the create_review.")


def update_review(request, review_id):
    return HttpResponse(f"You're at the update_review {review_id}.")


def read_review(request, review_id):
    return HttpResponse(f"You're at the read_review {review_id}.")


def delete_review(request, review_id):
    return HttpResponse(f"You're at the delete_review {review_id}.")
