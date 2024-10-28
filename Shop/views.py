import product
# Create your views here.
def home(request):
          all_Product = product.objects.all()
               return render(request, 'Shop/home.html' ,{'all_Product': all_Product})

               def product_detail(req