from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import InletPoint

@csrf_exempt
def ingest_inlets(request):

    if request.method != "POST":
        return JsonResponse({"error": "Post only"}, status=405)

    try:
        data = json.loads(request.body)

        points = data.get("points", [])

        saved = []

        for p in points:
            obj = InletPoint.objects.create(
                pointid=p.get("pointid"),
                name=p.get("name", ""),
                status=p.get("status", ""),
                longitude=p.get("lon"),
                latitude=p.get("lat")
            )

            saved.append(obj.id)

        return JsonResponse({
            "status": "success",
            "inserted": len(saved),
            "ids": saved
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
