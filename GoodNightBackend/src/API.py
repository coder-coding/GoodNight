from flask import request
import json
from . import db

old_msg_list_id = {}
currentMsg = {}


def Api(app):
    @app.route('/')
    def hello():
        return 'Hello, I\'m LZM!'

    @app.route('/get/<project>')
    def getProjectMsg(project):
        # global old_msg_list_id
        print(request.args)
        start_time = request.args["start"]
        end_time = request.args["end"]
        res = db.query_db(
            'select * from (select rowid,* from message where project = ? and time >= ? and time <= ?  limit 20) order by rowid DESC',
            [project, start_time, end_time])
        # if project not in old_msg_list_id.keys():
        #     old_msg_list_id[project] = []
        resList = []
        for r in res:
            # print(dict(r))
            # old_msg_list_id[project].append(r['rowid'])
            resList.append(dict(r))
        # print(resList)
        return {'project': project, 'data': resList}

    @app.route('/update/<project>')
    def updateProjectMsg(project):
        global old_msg_list_id, currentMsg
        res = db.query_db(
            'SELECT rowid,* FROM [message] WHERE project = ? ORDER BY rowid DESC LIMIT 20',
            [project])
        if project not in old_msg_list_id.keys():
            old_msg_list_id[project] = []
        if project not in currentMsg.keys():
            currentMsg[project] = []
        resList = []
        for r in res:
            # print(r['rowid'])
            if r['rowid'] not in old_msg_list_id[project]:
                old_msg_list_id[project].append(r['rowid'])
                resList.append(dict(r))
            # resList.append(dict(r))
        old_msg_list_id[project] = old_msg_list_id[project][-100:]
        if len(resList) > 0:
            currentMsg[project] = resList[:]
        # print(currentMsg[project])
        return {'project': project, 'data': currentMsg[project]}

    @app.route('/post/<project>', methods=['POST'])
    def postProjectMsg(project):
        data = json.loads(request.data)
        data_str = ''
        for k in ['project', 'type', 'level', 'context']:
            # print(data[k])
            if type(data[k]) == int:
                data_str += str(data[k]) + ','
            else:
                data_str += '\'' + data[k] + '\' ,'
        data_str = '(' + data_str[:-1] + ')'
        res = db.write_db(
            'insert into message (project,type,level,context) values ' +
            data_str)
        # print(data.keys(),type(data['context']))
        return data

    @app.route('/projects')
    def projects():
        res = db.query_db(
            'SELECT [project] FROM [message] GROUP  BY [project]')
        resList = []
        for r in res:
            # print(list(r))
            resList.append({'name': r['project']})
        return {'data': resList}

    return app