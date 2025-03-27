from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest

# 🔴 404 - Page Not Found
def handler404(request, exception):
    return render(request, "404.html", status=404)

# 🔴 500 - Server Error
def handler500(request):
    return render(request, "500.html", status=500)

# 🔴 403 - Forbidden
def handler403(request, exception):
    # استخدام Response مباشرة لعرض الرسالة في JSON
    return Response({"detail": "You do not have permission to access this resource."}, status=status.HTTP_403_FORBIDDEN)

# 🔴 400 - Bad Request
def handler400(request, exception):
    return render(request, "400.html", status=400)
