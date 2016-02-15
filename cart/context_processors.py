from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
    # we make the info available through RequestContext
    # as a dictionary named cart.
