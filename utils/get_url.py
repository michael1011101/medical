__author__ = 'linweihua'

from bots import setup_django_env
setup_django_env()

from stalk.models.helpers import DiseaseHelper, SymptomHelper

def get_urls_from_ids(from_id, to_id, type):
    urls = {}
    if type == 'disease':
        disease_list = DiseaseHelper.objects.filter(id__gte=int(from_id), id__lte=int(to_id))
        for ele in disease_list:
            urls[ele.id] = ele.link
        return urls
    elif type == 'symptom':
        symptom_list = SymptomHelper.objects.filter(id__gte=int(from_id), id__lte=int(to_id))
        for ele in symptom_list:
            urls[ele.id] = ele.link
        return urls
