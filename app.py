# from data.single_pred_tasks.tasks import _TASKS
import task_datasets as data

from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/overview')
def overview():
    return render_template('overview/index.html')

@app.route('/single_pred_tasks/overview')
def single_pred_tasks():
    vars = {
        "items": data.single_pred_tasks.tasks,
        "data": [(endpt, label, data.single_pred_tasks.datasets[endpt]) for endpt, label, _ in data.single_pred_tasks.tasks[1:]] # skip adme 
    }
    return render_template('single_pred_tasks/index.html', **vars)

@app.route("/single_pred_tasks/<task>")
def single_pred_tasks_data(task):
    task = task.lower()
    if task == "adme":
        return render_template("single_pred_tasks/adme.html")
    elif task in data.single_pred_tasks.datasets:
        datasets = []
        for var in data.single_pred_tasks.datasets[task]:
            if var in data.single_pred_tasks.meta:
                if len(data.single_pred_tasks.meta[var]) != 10:
                    raise Exception(var, len(data.single_pred_tasks.meta[var])) 
                datasets.append([var] + data.single_pred_tasks.meta[var])
        args = {
            "datasets": datasets,
            "task": task,
        }
        return render_template("single_pred_tasks/task.html", **args)
    return redirect("/single_pred_tasks/overview")


if __name__ == '__main__':
    app.run(debug=True)  # debug=True for development mode