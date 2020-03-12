from model import services, support


def support_recommendation(pid):
    most_useful_support = support.Support().most_useful_support(pid)
    if most_useful_support[1] < 1:
        default_recommended_service = services.Service().get_service()
        return default_recommended_service[0]
    else:
        return most_useful_support[0]
