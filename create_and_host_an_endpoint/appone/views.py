from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from datetime import datetime
import pytz

def my_endpoint(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if slack_name and track:
        current_utc_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        current_day = datetime.now(pytz.UTC).strftime("%A")
        
        github_file_url = "https://github.com/emmystrings309/Zuri/blob/main/create_and_host_an_endpoint/appone/views.py"
        github_repo_url = "https://github.com/emmystrings309/Zuri.git"
        
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return JsonResponse(response_data)

    return JsonResponse({"error": "Invalid parameters"}, status=400)
