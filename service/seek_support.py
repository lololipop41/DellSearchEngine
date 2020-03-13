from model import support


def seeking_for_support(pid, sid):
    single_support = support.Support().get_support(pid, sid)
    supid = 0
    usage = 0
    for item in single_support:
        supid = item[0]
        usage = item[3]
    new_usage = usage + 1
    update_usage = support.Support().update_usage(supid, new_usage)
    if update_usage:
        return True, "Usage Updated Successfully!"
    else:
        return False, "Unable to Update Usage!"
