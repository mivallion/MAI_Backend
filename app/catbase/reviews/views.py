from django.contrib.auth.models import User
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.views import APIView

from cat.models import Cat
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from utils.permissions import IsGetOrIsAuthenticated


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewView(APIView):

    permission_classes = [IsGetOrIsAuthenticated]

    def get(self, request):
        if 'id' in self.request.GET:
            id = self.request.GET.get('id')
            try:
                obj = Review.objects.get(id=int(id))
            except Review.DoesNotExist:
                return JsonResponse(status=204)

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

        data = request.data.dict()

        if 'sociability' not in data or \
                'attractiveness' not in data or \
                'playfulness' not in data or \
                'review_title' not in data or \
                'cat_id' not in data:
            return HttpResponseBadRequest()

        if not Cat.objects.filter(id=data['cat_id']).exists():
            return JsonResponse(data={'error': f"cat with id={data['cat_id']} doesn't exists"}, status=204)

        data['general_rating'] = round((int(data['sociability']) +
                                        int(data['attractiveness']) +
                                        int(data['playfulness'])) / 3)
        data['review_text'] = None if 'review_text' not in data else data['review_text']
        data['user_id'] = request.user.id
        Review.objects.create(
            review_title=data['review_title'],
            review_text=data['review_text'],
            general_rating=data['general_rating'],
            attractiveness=data['attractiveness'],
            sociability=data['sociability'],
            playfulness=data['playfulness'],
            cat_id=data['cat_id'],
            user_id=data['user_id']
        )
        return JsonResponse(data, status=201)

    def put(self, request):

        data = request.data.dict()

        if 'id' not in data:
            return HttpResponseBadRequest()

        if not Review.objects.filter(id=data['id']).exists():
            return JsonResponse(data={'error': f"review with id={data['id']} doesn't exists"}, status=204)

        obj = Review.objects.get(id=data['id'])

        if 'sociability' in data:
            obj.sociability = int(data['sociability'])
        if 'attractiveness' in data:
            obj.attractiveness = int(data['attractiveness'])
        if 'playfulness' in data:
            obj.playfulness = int(data['playfulness'])
        if 'review_title' in data:
            obj.review_title = data['review_title']
        if 'review_text' in data:
            obj.review_text = data['review_text']
        obj.general_rating = round((obj.sociability + obj.attractiveness + obj.playfulness) / 3)
        obj.save()

        return JsonResponse(obj.dict(), status=201)

    def delete(self, request):

        data = request.data.dict()

        if 'id' not in data:
            return HttpResponseBadRequest()

        Review.objects.filter(id=data['id']).delete()

        return JsonResponse({}, status=201)
