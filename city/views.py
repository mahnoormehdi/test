from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def get(request):
    # Path to your JSON file
    json_file_path = 'city/data.json'  # Update with the correct path

    try:
        # Read JSON data from the file
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Return JSON data in the response
        return JsonResponse({'data': json_data}, status=200)

    except FileNotFoundError:
        return JsonResponse({'error': 'JSON file not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format in the file'}, status=500)