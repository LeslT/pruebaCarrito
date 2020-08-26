from django.http import HttpResponse

#View products
def getProducts(request):
    return HttpResponse("Holi")

#View shopping cart products
def getShoppingCartProducts(request):
    return HttpResponse("Holi2")

def addProduct(request, reference, description, value):
    return HttpResponse("")

def addProductsTo(request):
    return HttpResponse("")

def deleteProducts(request):
    return HttpResponse("")

def deleteProduct(request):
    return HttpResponse("")

def confirm(request):
    return HttpResponse("")

def register(request):
    return HttpResponse("")

def login(request):
    return HttpResponse("")