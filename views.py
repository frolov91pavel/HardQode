from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Group


@login_required
def product_detail(request, product_id):
    print("Старт")
    product = get_object_or_404(Product, pk=product_id)
    if request.user == product.creator:
        groups = Group.objects.filter(product=product)

        if product.start_date > timezone.now():

            for group in groups:

                num_users_in_group = group.users.count()
                print(num_users_in_group)
                print(group.min_users)
                if num_users_in_group < group.min_users:
                    group.users.add(request.user)
                    print(request.user)
                    break
        else:

            min_group_size = min(group.min_users for group in groups)
            max_group_size = max(group.max_users for group in groups)
            total_users = sum(group.users.count() for group in groups)
            avg_users_per_group = total_users // len(groups)

            for group in groups:
                num_users_in_group = group.users.count()
                if num_users_in_group < max_group_size and num_users_in_group < avg_users_per_group:
                    group.users.add(request.user)
                    break

        return render(request, 'product_detail.html', {'product': product})
    else:
        return HttpResponse("У вас нет доступа к этому продукту.")
