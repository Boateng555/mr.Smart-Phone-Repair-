
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key') 
        if cart is None:
            cart = {}
        self.session['session_key'] = cart 
        self.cart = cart