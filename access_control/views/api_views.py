from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        response = {"token": False, "status": False, "error": False}
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
<<<<<<< Updated upstream
        # try:
        if user:
=======

        if user:
            login(request, user)
>>>>>>> Stashed changes
            try:
                response["token"] = user.auth_token.key
                response["status"] = status.HTTP_200_OK
                return JsonResponse(response)
            except Exception as e:
                response["error"] = str(e)
                return JsonResponse(response)
        else:
            response["error"] = 'Geen juist wachtwoord of gebruikersnaam opgegeven' \
                if not username or not password else 'Verkeerde inloggegevens'
            response["status"] = status.HTTP_400_BAD_REQUEST
            return JsonResponse(response)
