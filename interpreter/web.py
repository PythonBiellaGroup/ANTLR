import json
import os
import sys
import traceback

from flask import Flask, render_template, redirect, request

from interpreter.entities_parser.entities_ast import Module
from interpreter.entities_parser.entities_pylasu_parser import EntitiesPylasuParser
from interpreter.interpreter import Interpreter
from interpreter.script_parser.script_pylasu_parser import ScriptPylasuParser


def load_module() -> Module:
    if os.path.isfile('web.entities'):
        with open('web.entities', "r") as file:
            code = file.read()
            result = EntitiesPylasuParser().parse(code)
            if len(result.issues) == 0:
                print("No issues parsing the entities configuration")
            else:
                print("Issues parsing the entities configuration: %s" % str(result.issues))
            return result.root

    else:
        raise Exception("No entities defined")


def load_interpreter(module: Module) -> Interpreter:
    return Interpreter(module)


def create_app():
    # create and configure the app
    app = Flask("EntitiesAndScript", template_folder='templates', static_folder='static')

    module = load_module()
    interpreter = load_interpreter(module)

    @app.route('/entity/<string:entity_name>/add')
    def add_entity(entity_name):
        # call interpreter
        interpreter.instantiate_entity(module.get_entity_by_name(entity_name))
        # redirect
        return redirect("/entity/%s" % entity_name)

    @app.route('/clearLogs', methods = ['POST'])
    def clear_logs():
        print('clear logs')
        interpreter.clear_logs()
        answer = {}
        answer['ok'] = True
        return json.dumps(answer)

    @app.route('/run', methods = ['POST'])
    def run_script():
        print("request %s" % str(request.json))
        script_code = request.json['code']
        result = ScriptPylasuParser().parse(script_code)
        issues = result.issues
        try:
            issues = result.issues + interpreter.run_script(result.root)
            answer = {}
            answer['ok'] = len(issues) == 0
            answer['issues'] = [str(i) for i in issues]
        except BaseException as ex:
            # Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)

            # Format stacktrace
            stack_trace = list()

            for trace in trace_back:
                stack_trace.append(
                    "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" % ex_value)
            for e in stack_trace:
                print(e)
            answer = {}
            answer['ok'] = False
            answer['error'] = str(ex_value)
            answer['issues'] = [str(i) for i in issues]
        return json.dumps(answer)


    @app.route('/entity/<string:entity_name>/show/<int:instance_id>')
    def instance_page(entity_name, instance_id):
        return render_template('instance.html',
                               module_name=module.name,
                               entities=module.entities,
                               entity=module.get_entity_by_name(entity_name),
                               instance=interpreter.instances_by_id(entity_name, instance_id), logs=interpreter.output)

    @app.route('/entity/<string:entity_name>/')
    def entity_page(entity_name):
        return render_template('entities.html',
                               module_name=module.name,
                               entities=module.entities,
                               entity=module.get_entity_by_name(entity_name),
                               instances=interpreter.instances_by_entity_name(entity_name), logs=interpreter.output)

    @app.route('/')
    def index_page():
        nb_of_entities = {}
        for e in module.entities:
            if e not in interpreter.instances_by_entity:
                nb_of_entities[e.name] = 0
            else:
                nb_of_entities[e.name] = len(interpreter.instances_by_entity[e])
        return render_template('index.html',
                               module_name=module.name,
                               entities=module.entities, nb_of_entities=nb_of_entities, logs=interpreter.output)

    return app
