menu = [
    {'title': "About", 'url_name': 'vet_clinic:about'},
    {'title': "Services", 'url_name': 'vet_clinic:services'},
    {'title': "Blog", 'url_name': 'vet_clinic:blog'},
    {'title': "Happy Clients", 'url_name': 'vet_clinic:responses'},
    {'title': "Contacts", 'url_name': 'vet_clinic:contacts'},
]


def get_mainmenu(request):
    return {'mainmenu': menu}


footer_nav = [
    {'title': "Testimonials", 'url_name': 'vet_clinic:responses'},
    {'title': "Blog", 'url_name': 'vet_clinic:blog'},
]


def get_footer_nav(request):
    return {'footer_nav': footer_nav}


footer_quick_links = [
    {'title': "Services", 'url_name': 'vet_clinic:services'},
    {'title': "About us", 'url_name': 'vet_clinic:about'},
]


def get_footer_quick_links(request):
    return {'footer_links': footer_quick_links}


footer_support = [
    {'title': "FAQ", 'url_name': 'vet_clinic:faq'},
    {'title': "Contacts", 'url_name': 'vet_clinic:contacts'},
]


def get_support(request):
    return {'footer_support': footer_support}

