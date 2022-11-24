instances_by_entity = {}


def add_entity(type, instance):
    if type not in instances_by_entity:
        instances_by_entity[type] = []
    instances_by_entity[type].append(instance)
    return instance
