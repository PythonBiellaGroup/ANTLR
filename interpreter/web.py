import json

from flask import Flask, render_template, redirect, url_for, request

from interpreter.controller import Controller
from interpreter.entities_ast import Module, Entity
from interpreter.interpreter import Interpreter


def load_module() -> Module:
    m = Module()

    client = m.add_entity("Client")
    client.add_str_feature("name")
    client.add_str_feature("address")

    project = m.add_entity("Project")

    return m


def load_interpreter(module: Module) -> Interpreter:
    c = Controller()
    i = Interpreter(module, c)
    return i


def create_app():
    # create and configure the app
    app = Flask("SimpleTable", template_folder='templates', static_folder='static')
    module = load_module()
    interpreter = load_interpreter(module)

    @app.route('/entity/<string:entity_name>/add')
    def add_entity(entity_name):
        # call interpreter
        interpreter.instantiate_entity(module.get_entity_by_name(entity_name))
        # redirect
        return redirect("/entity/%s" % entity_name)

    @app.route('/run', methods = ['POST'])
    def run_script():
        print("request %s" % str(request.json))
        answer = {}
        answer['ok'] = True
        answer['issues'] = ['Foo']
        return json.dumps(answer)


    @app.route('/entity/<string:entity_name>/show/<int:instance_id>')
    def instance_page(entity_name, instance_id):
        return render_template('instance.html',
                               entities=module.entities,
                               entity=module.get_entity_by_name(entity_name),
                               instance=interpreter.instances_by_id(entity_name, instance_id), logs=interpreter.logs)

    @app.route('/entity/<string:entity_name>/')
    def entity_page(entity_name):
        return render_template('entities.html',
                               entities=module.entities,
                               entity=module.get_entity_by_name(entity_name),
                               instances=interpreter.instances_by_entity_name(entity_name), logs=interpreter.logs)

    @app.route('/')
    def index_page():
        nb_of_entities = {}
        for e in module.entities:
            if e not in interpreter.instances_by_entity:
                nb_of_entities[e.name] = 0
            else:
                nb_of_entities[e.name] = len(interpreter.instances_by_entity[e])
        return render_template('index.html', entities=module.entities, nb_of_entities=nb_of_entities, logs=interpreter.logs)

    return app
