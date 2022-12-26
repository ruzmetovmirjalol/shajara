from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer


# class AmakiView(APIView):
#     """
#     Amakilarni topish (1-variant)
#     """
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user = request.user
#
#         amakilar = User.objects.none()
#
#         father = user.father
#
#         if father is None:
#             amakilar = User.objects.none()
#         else:
#             grand_father = father.father
#
#             if grand_father is None:
#                 amakilar = User.objects.none()
#             else:
#                 amakilar = User.objects.filter(father=grand_father, toifa='erkak').exclude(id=father.id)
#
#         serializer = UserSerializer(amakilar, many=True)
#
#         return Response(serializer.data)


class AmakiView(APIView):
    """
    Amakilarni topish (2-variant)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = father.father

            if grand_father is None:
                amakilar = User.objects.none()
            else:
                amakilar = User.objects.filter(father=grand_father, toifa='erkak').exclude(id=father.id)
        except:
            amakilar = User.objects.none()

        serializer = UserSerializer(amakilar, many=True)

        return Response(serializer.data)


class AmmaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = user.father.father

            if grand_father is None:
                ammalar = User.objects.none()
            else:
                ammalar = User.objects.filter(father=grand_father, toifa='ayol')

        except:
            ammalar = User.objects.none()

        serializer = UserSerializer(ammalar, many=True)

        return Response(serializer.data)


class TogaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = user.mother.father

            if grand_father is None:
                togalar = User.objects.none()
            else:
                togalar = User.objects.filter(father=grand_father, toifa='erkak')

        except:
            togalar = User.objects.none()

        serializer = UserSerializer(togalar, many=True)

        return Response(serializer.data)


class XolaView(APIView):
    def get(self, request):
        user = request.user

        try:
            mother = user.mother

            grand_father = user.mother.father

            if grand_father is None:
                xolalar = User.objects.none()
            else:
                xolalar = User.objects.filter(father=grand_father, toifa='ayol').exclude(id=mother.id)

        except:
            xolalar = User.objects.none()

        serializer = UserSerializer(xolalar, many=True)

        return Response(serializer.data)


class AmakivachchaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = user.father.father

            if grand_father is None:
                amakivachchalar = User.objects.none()
            else:
                amakivachchalar = User.objects.filter(father__father=grand_father).exclude(father=father)

        except:
            amakivachchalar = User.objects.none()

        serializer = UserSerializer(amakivachchalar, many=True)

        return Response(serializer.data)


class AmmavachchaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = user.father.father

            if grand_father is None:
                ammavachchalar = User.objects.none()
            else:
                ammavachchalar = User.objects.filter(mother__father=grand_father)

        except:
            ammavachchalar = User.objects.none()

        serializer = UserSerializer(ammavachchalar, many=True)

        return Response(serializer.data)


class TogavachchaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            grand_father = user.mother.father

            if grand_father is None:
                togavachchalar = User.objects.none()
            else:
                togavachchalar = User.objects.filter(father__father=grand_father)

        except:
            togavachchalar = User.objects.none()

        serializer = UserSerializer(togavachchalar, many=True)

        return Response(serializer.data)


class XolavachchaView(APIView):
    def get(self, request):
        user = request.user

        try:
            mother = user.mother

            grand_father = user.mother.father

            if grand_father is None:
                xolavachchalar = User.objects.none()
            else:
                xolavachchalar = User.objects.filter(mother__father=grand_father).exclude(mother=mother)

        except:
            xolavachchalar = User.objects.none()

        serializer = UserSerializer(xolavachchalar, many=True)

        return Response(serializer.data)


class JiyanView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            father = user.father

            mother = user.mother

            grand_father = user.father.father

            grand_father_m = user.mother.father

            if grand_father is None:
                jiyanlar = User.objects.none()
            else:
                jiyanlar = User.objects.filter(
                    Q(father__father=grand_father) | Q(mother__father=grand_father) | Q(father__father=grand_father_m) |
                    Q(mother__father=grand_father_m)).exclude(mother=mother)

        except:
            jiyanlar = User.objects.none()

        serializer = UserSerializer(jiyanlar, many=True)

        return Response(serializer.data)


class PochchaView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            mother = user.mother

            grand_father = user.father.father

            grand_father_m = user.mother.father

            if grand_father is None:
                pochchalar = User.objects.none()
            else:
                pochchalar = User.objects.filter(Q(pair__father=grand_father, toifa='erkak') |
                                                 Q(pair__father=grand_father_m, toifa='erkak')).exclude(id=father.id)

        except:
            pochchalar = User.objects.none()

        serializer = UserSerializer(pochchalar, many=True)

        return Response(serializer.data)


class KenayiView(APIView):
    def get(self, request):
        user = request.user

        try:
            father = user.father

            mother = user.mother

            grand_father = user.father.father

            grand_father_m = user.mother.father

            if grand_father is None:
                kenayilar = User.objects.none()
            else:
                kenayilar = User.objects.filter(Q(pair__father=grand_father, toifa='ayol') |
                                                Q(pair__father=grand_father_m, toifa='ayol')).exclude(id=mother.id)

        except:
            kenayilar = User.objects.none()

        serializer = UserSerializer(kenayilar, many=True)

        return Response(serializer.data)

# class AmakiView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         grand_father = user.father.father
#
#         amakilar = User.objects.filter(father=grand_father, toifa='erkak').exclude(id=father.id)
#
#         serializer = UserSerializer(amakilar, many=True)
#
#         return Response(serializer.data)
#
#
# class AmmaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.father.father
#
#         ammalar = User.objects.filter(father=grand_father, toifa='ayol')
#
#         serializer = UserSerializer(ammalar, many=True)
#
#         return Response(serializer.data)
#
#
# class TogaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.mother.father
#
#         togalar = User.objects.filter(father=grand_father, toifa='erkak')
#
#         serializer = UserSerializer(togalar, many=True)
#
#         return Response(serializer.data)
#
#
# class XolaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         mother = user.mother
#
#         grand_father = user.mother.father
#
#         xolalar = User.objects.filter(father=grand_father, toifa='ayol').exclude(id=mother.id)
#
#         serializer = UserSerializer(xolalar, many=True)
#
#         return Response(serializer.data)
#
#
# class AmakivachchaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         grand_father = user.father.father
#
#         amakivachchalar = User.objects.filter(father__father=grand_father).exclude(father=father)
#
#         serializer = UserSerializer(amakivachchalar, many=True)
#
#         return Response(serializer.data)
#
#
# class AmmavachchaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.father.father
#
#         ammavachchalar = User.objects.filter(mother__father=grand_father)
#
#         serializer = UserSerializer(ammavachchalar, many=True)
#
#         return Response(serializer.data)
#
#
# class TogavachchaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.mother.father
#
#         togavachchalar = User.objects.filter(father__father=grand_father)
#
#         serializer = UserSerializer(togavachchalar, many=True)
#
#         return Response(serializer.data)
#
#
# class XolavachchaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         mother = user.mother
#
#         grand_father = user.mother.father
#
#         xolavachchalar = User.objects.filter(mother__father=grand_father).exclude(mother=mother)
#
#         serializer = UserSerializer(xolavachchalar, many=True)
#
#         return Response(serializer.data)
#
#
# class JiyanView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         jiyanlar = User.objects.filter(
#             Q(father__father=grand_father) | Q(mother__father=grand_father) | Q(father__father=grand_father_m) | Q(
#                 mother__father=grand_father_m)).exclude(mother=mother)
#
#         serializer = UserSerializer(jiyanlar, many=True)
#
#         return Response(serializer.data)
#
#
# class PochchaView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         pochchalar = User.objects.filter(Q(pair__father=grand_father, toifa='erkak') |
#                                          Q(pair__father=grand_father_m, toifa='erkak')).exclude(id=father.id)
#
#         serializer = UserSerializer(pochchalar, many=True)
#
#         return Response(serializer.data)
#
#
# class KenayiView(APIView):
#     def get(self, request):
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         kenayilar = User.objects.filter(Q(pair__father=grand_father, toifa='ayol') |
#                                         Q(pair__father=grand_father_m, toifa='ayol')).exclude(id=mother.id)
#
#         serializer = UserSerializer(kenayilar, many=True)
#
#         return Response(serializer.data)


#################################################################################################


# from http.client import HTTPResponse
# from django.db.models import Q
# from django.http import HttpResponse
# from django.shortcuts import render
#
# from user.models import User
#
#
# def amaki_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         grand_father = user.father.father
#
#         amakilar = User.objects.filter(father=grand_father, toifa='erkak').exclude(id=father.id).values_list('username',
#                                                                                                              flat=True)
#
#         return HttpResponse(amakilar)
#
#
# def amma_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.father.father
#
#         ammalar = User.objects.filter(father=grand_father, toifa='ayol').values_list('username', flat=True)
#
#         return HttpResponse(ammalar)
#
#
# def toga_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.mother.father
#
#         togalar = User.objects.filter(father=grand_father, toifa='erkak').values_list('username', flat=True)
#
#         return HttpResponse(togalar)
#
#
# def xola_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         mother = user.mother
#
#         grand_father = user.mother.father
#
#         xolalar = User.objects.filter(father=grand_father, toifa='ayol').exclude(id=mother.id).values_list('username',
#                                                                                                            flat=True)
#
#         return HttpResponse(xolalar)
#
#
# def amakivachcha_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         grand_father = user.father.father
#
#         amakivachchalar = User.objects.filter(father__father=grand_father).exclude(father=father).values_list(
#             'username', flat=True)
#
#         return HttpResponse(amakivachchalar)
#
#
# def ammavachcha_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.father.father
#
#         ammavachchalar = User.objects.filter(mother__father=grand_father).values_list('username', flat=True)
#
#         return HttpResponse(ammavachchalar)
#
#
# def togavachcha_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         grand_father = user.mother.father
#
#         togavachchalar = User.objects.filter(father__father=grand_father).values_list('username', flat=True)
#
#         return HttpResponse(togavachchalar)
#
#
# def xolavachcha_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         mother = user.mother
#
#         grand_father = user.mother.father
#
#         xolavachchalar = User.objects.filter(mother__father=grand_father).exclude(mother=mother).values_list(
#             'username', flat=True)
#
#         return HttpResponse(xolavachchalar)
#
#
# def jiyan_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         jiyanlar = User.objects.filter(
#             Q(father__father=grand_father) | Q(mother__father=grand_father) | Q(father__father=grand_father_m) | Q(
#                 mother__father=grand_father_m)).exclude(mother=mother).values_list(
#             'username', flat=True)
#
#         return HttpResponse(jiyanlar)
#
#
# def pochcha_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         pochchalar = User.objects.filter(Q(pair__father=grand_father, toifa='erkak') |
#                                          Q(pair__father=grand_father_m, toifa='erkak')). \
#             exclude(id=father.id).values_list('username', flat=True)
#
#         return HttpResponse(pochchalar)
#
#
# def kenayi_view(request):
#     if request.method == 'GET':
#         # user = request.user
#         user = User.objects.filter(username='mirjalol').first()
#
#         father = user.father
#
#         mother = user.mother
#
#         grand_father = user.father.father
#
#         grand_father_m = user.mother.father
#
#         kenayilar = User.objects.filter(Q(pair__father=grand_father, toifa='ayol') |
#                                         Q(pair__father=grand_father_m, toifa='ayol')). \
#             exclude(id=mother.id).values_list('username', flat=True)
#
#         return HttpResponse(kenayilar)
