class CarInfoRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'NoSQL':
            return 'carinfo'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'NoSQL':
            return 'carinfo'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'NoSQL' and obj2._meta.app_label == 'NoSQL':
            return True
        # Allow if neither is chinook app
        elif 'carinfo' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'carinfo' or model._meta.app_label == "NoSQL":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'NoSQL':
            return True
        else:
            return False
