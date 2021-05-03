import json
from flask import Flask, request, jsonify
app = Flask(__name__)

tasks = {
    0:{
        'id':0,
        'description':'todo-1',
        'done':False
    },
    1:{
        'id':1,
        'description':'todo-2',
        'done':False
    }
}
#定義清單的計數器
task_id_counter = 2

@app.route('/')
@app.route('/tasks/')
def get_tasks():
    res = {
        'success':True,
        'data':list(tasks.values())
    }
    return jsonify(res)

@app.route('/tasks/', methods=['POST'])
def creat_task():
    #讓計數器可以被全域存取
    global task_id_counter
    #將取得的資料以json載入
    body = json.loads(request.data)
    #指定拿取description,若無則顯示no description
    description = body.get("description", "no description")
    #開始建立新的清單內容
    task = {
        "id":task_id_counter,
        "description": description,
        "done":False
    }
    #將清單內容增加回task清單中
    tasks[task_id_counter] = task
    task_id_counter += 1
    return json.dumps({
        "success":True,
        "data":task
    }), 201

@app.route('/tasks/<int:task_id>/')
def get_task(task_id):
        task = tasks.get(task_id)
        if not task:
            return json.dumps({
                "success":False,
                "error":"Task not found"
            }), 404
            return json.dumps({
                "success":True,
                "data":task
            }), 200

@app.route('/tasks/<int:task_id>/', methods=['POST'])
def update_task(task_id):
        task = tasks.get(task_id)
        if not task:
            return json.dumps({
                "success":False,
                "error":"Task not found"
            }), 404
        body = json.loads(request.data)
        description = body.get("description")
        if description:
            task['description'] = description
        task['done'] = body.get("done", False)
        return json.dumps({
            "success":True,
            "data":task
        }), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return json.dumps({
            "success":False,
            "error":"Task not found"
        }), 404
    del tasks[task_id]
    return json.dumps({
        "success":True,
        "data":task
    }), 200
    
    