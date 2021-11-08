from django.conf import settings
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import utils.cache.lru_cache as lru_cache

from django.views.decorators.http import require_http_methods

from cat.models import Cat, Review


class CatView(View):
    def get(self, request):
        if 'id' in self.request.GET:
            id = self.request.GET.get('id')
            try:
                obj = Cat.objects.get(id=int(id))
            except Cat.DoesNotExist:
                raise Http404(f'Cat #{id} not found!')

            return JsonResponse({
                "id": obj.id,
                "name": obj.name,
                "birth_year": obj.birth_year,
                "description": obj.description
            })
        else:
            return JsonResponse({"cats": [{
                "id": obj.id,
                "name": obj.name,
                "birth_year": obj.birth_year,
                "description": obj.description
            } for obj in Cat.objects.all()]})

    @csrf_exempt
    def post(self, request):
        return JsonResponse({'result': ""})

    def put(self, request):
        return JsonResponse({'result': ""})

    def delete(self, request):
        return JsonResponse({'result': ""})


class ReviewView(View):
    def get(self, request):
        if 'id' in self.request.GET:
            id = self.request.GET.get('id')
            try:
                obj = Review.objects.get(id=int(id))
            except Review.DoesNotExist:
                raise Http404(f'Review #{id} not found!')

            return JsonResponse({
                "id": obj.id,
                "review_title": obj.review_title,
                "review_text": obj.review_text,
                "general_rating": obj.general_rating,
                "attractiveness": obj.attractiveness,
                "sociability": obj.sociability,
                "playfulness": obj.playfulness,
                "user_id": obj.user.id,
                "cat_id": obj.cat.id,
            })
        else:
            return JsonResponse({"reviews": [{
                "id": obj.id,
                "review_title": obj.review_title,
                "review_text": obj.review_text,
                "general_rating": obj.general_rating,
                "attractiveness": obj.attractiveness,
                "sociability": obj.sociability,
                "playfulness": obj.playfulness,
                "user_id": obj.user.id,
                "cat_id": obj.cat.id,
            } for obj in Review.objects.all()]})

    def post(self, request):
        return JsonResponse({'result': ""})

    def put(self, request):
        return JsonResponse({'result': ""})

    def delete(self, request):
        return JsonResponse({'result': ""})


class UserView(View):
    def get(self, request):
        if 'id' in self.request.GET:
            id = self.request.GET.get('id')
            try:
                obj = User.objects.get(id=int(id))
            except User.DoesNotExist:
                raise Http404(f'User #{id} not found!')

            return JsonResponse({
                "id": obj.id,
                "username": obj.username
            })
        else:
            return JsonResponse({"users": [{
                "id": obj.id,
                "username": obj.username
            } for obj in User.objects.all()]})
