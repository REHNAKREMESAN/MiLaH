from django.shortcuts import render, redirect, get_object_or_404

def card(request):


    return render(request, "Payment/CardPayment.html", {})
