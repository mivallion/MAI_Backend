from django.http import JsonResponse
import utils.cache.lru_cache as lru_cache


def read_user(request, user_id):
    return JsonResponse({"id": user_id})


def create_cat(request):
    return JsonResponse({"id": 1})


def update_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


def read_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


def delete_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


def create_review(request):
    return JsonResponse({"id": 1})


def update_review(request, review_id):
    return JsonResponse({"id": review_id})


def read_review(request, review_id):
    return JsonResponse({"id": review_id})


def delete_review(request, review_id):
    return JsonResponse({"id": review_id})
