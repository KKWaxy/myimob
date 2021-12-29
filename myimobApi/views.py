from rest_framework import decorators,  response, views

# def apiOverview(request):
#     api_urls = {
        
#     }

@decorators.api_view(["GET"])
def get_all(request):
    ctx = {"message":"First API View."}
    return response.Response(data=ctx)