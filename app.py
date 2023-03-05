from flask import Flask

app = Flask(__name__)


"""
goal: TODO app

GET: get all tasks
PUT: add task for today


"""

tasks = ["task1", "task2", "task2"]

@app.route('/')
def get_all_tasks():
    return tasks

@app.route('/add', methods=['POST'])
def add_task():
    new_tasks = json.loads(request.data)
    if new_tasks:
        tasks.append(new_tasks)
    # if error: return False

    # for r in records:
    #     if r['name'] == record['name']:
    #         r['email'] = record['email']
    #     new_records.append(r)
    # with open('/tmp/data.txt', 'w') as f:
    #     f.write(json.dumps(new_records, indent=2))
    return True
    





