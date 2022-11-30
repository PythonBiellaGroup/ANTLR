instances_by_entity = {}


def add_entity(entity_type, **kwargs):
    if entity_type not in instances_by_entity:
        instances_by_entity[entity_type] = []
    instance = entity_type()
    instances_by_entity[entity_type].append(instance)
    for k in kwargs:
        setattr(instance, k, kwargs[k])
    return instance
