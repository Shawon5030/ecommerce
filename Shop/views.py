import product
# Create your views here.
def home(request):
          all_Product = product.objects.all()
               return render(request, 'Shop/home.html' ,{'a'})