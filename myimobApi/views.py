from rest_framework import decorators,  response, views

@decorators.api_view(["GET",])
def apiOverview(request):
    """
        Ajouter la gestion des authorisations.
    """
    api_urls = {
        "List all houses": "/api/house_list/",
        "Create house": "/api/create_house/",
        "House details": "api/<str:pk>/details/",
        "Delete house": "api/<str:pk>/delete/",
        "Update house": "api/<str:pk>/update/",
        "Get house by Catergory":"api/house_by_category/<str:pk>/",
    }

    return response.Response(data=api_urls)

@decorators.api_view(["GET"])
def get_all(request):
    ctx = {"message":"First API View."}
    return response.Response(data=ctx)