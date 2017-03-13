from channels import Group

def callAPI(instance):
    Group('main').send({'text': 'Speech To Text Complete'})
    return 'Hello'
