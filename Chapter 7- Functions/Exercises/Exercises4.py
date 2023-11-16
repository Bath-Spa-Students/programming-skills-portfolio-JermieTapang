def make_shirt(size='large', message='I want to GO!'):
    """Show what is going to be imprinted on the shirt."""
    print("\nI'm going to commision a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'LETS stay HERE!')