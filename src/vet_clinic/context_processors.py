menu = [
    {'title': "About", 'url_name': 'vet_clinic:about'},
    {'title': "Services", 'url_name': 'vet_clinic:services'},
    {'title': "Faq", 'url_name': 'vet_clinic:faq'},
    {'title': "Happy Clients", 'url_name': 'vet_clinic:responses'},
    {'title': "Contacts", 'url_name': 'vet_clinic:contacts'},
]


def get_mainmenu(request):
    return {'mainmenu': menu}
