


class ModelAdminBase(object):
    list_display = ()
    list_per_page = 20
    choice_fields = ()
    fk_fields = ()
    filter_horizontal = ()
    model = None
    onclick_fields = {}

    readable_table = False

    readonly_fields = []

def register(admin_dic,model,admin_class):
    '''注册admin'''
    if model._meta.db_table not in admin_dic:
        admin_dic[model._meta.db_table] = admin_class
    else:
        raise Exception

