from django.http import JsonResponse
import utils.cache.lru_cache as lru_cache

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def read_user(request, user_id):
    return JsonResponse({"id": user_id})


@require_http_methods(["POST"])
def create_cat(request):
    return JsonResponse({"id": 1})


@require_http_methods(["POST"])
def update_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


@require_http_methods(["GET"])
def read_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


@require_http_methods(["POST"])
def delete_cat(request, cat_id):
    return JsonResponse({"id": cat_id})


@require_http_methods(["POST"])
def create_review(request):
    return JsonResponse({"id": 1})


@require_http_methods(["POST"])
def update_review(request, review_id):
    return JsonResponse({"id": review_id})


@require_http_methods(["GET"])
def read_review(request, review_id):
    return JsonResponse({"id": review_id})


@require_http_methods(["POST"])
def delete_review(request, review_id):
    return JsonResponse({"id": review_id})
