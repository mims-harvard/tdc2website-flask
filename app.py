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
    # task = task.lower()
    if task == "adme":
        return render_template("single_pred_tasks/adme.html")
    elif task in data.single_pred_tasks.datasets:
        datasets = []
        for var in data.single_pred_tasks.datasets[task]:
            if var in data.single_pred_tasks.meta:
                if len(data.single_pred_tasks.meta[var]) != 10:
                    raise Exception(var, len(data.single_pred_tasks.meta[var])) 
                datasets.append([var] + data.single_pred_tasks.meta[var])
        desc = data.single_pred_tasks.desc[task]
        args = {
            "datasets": datasets,
            "task": task,
            "desc_id": desc[0],
            "desc_title": desc[1],
            "desc_desc": desc[2],
            "desc_impact": desc[3],
            "desc_gen": desc[4],
            "desc_product": desc[5],
            "desc_pipeline": desc[6],
        }
        return render_template("single_pred_tasks/task.html", **args)
    return redirect("/single_pred_tasks/overview")

@app.route("/multi_pred_tasks/overview")
def multi_pred_tasks():
    vars = {
        "items": data.multi_pred_tasks.tasks,
        "data": [(endpt, label, data.multi_pred_tasks.datasets[endpt]) for endpt, label, _ in data.multi_pred_tasks.tasks]
    }
    return render_template("multi_pred_tasks/index.html", **vars)

@app.route("/multi_pred_tasks/<task>")
def multi_pred_task_data(task):
    if task == "catalyst":
        return render_template("multi_pred_tasks/catalyst.html")
    elif task == "ddi":
        return render_template("multi_pred_tasks/ddi.html")
    elif task == "drugres":
        return render_template("multi_pred_tasks/drugres.html")
    elif task == "dti":
        return render_template("multi_pred_tasks/dti.html")
    elif task == "mti":
        return render_template("multi_pred_tasks/mti.html")
    elif task == "ppi":
        return render_template("multi_pred_tasks/ppi.html")
    elif task == "proteinpeptide":
        return render_template("multi_pred_tasks/proteinpeptide.html")
    elif task == "tcrepitope":
        return render_template("multi_pred_tasks/tcrepitope.html")
    elif task == "antibodyaff":
        return render_template("multi_pred_tasks/antibodyaff.html")
    elif task == "trialoutcome":
        return render_template("multi_pred_tasks/trialoutcome.html")
    elif task == "scdti":
        return render_template("multi_pred_tasks/scdti.html")
    elif task == "counterfactual":
        return render_template("multi_pred_tasks/counterfactual.html")
    elif task in data.multi_pred_tasks.datasets:
        datasets = []
        for var in data.multi_pred_tasks.datasets[task]:
            if var in data.multi_pred_tasks.meta:
                if len(data.multi_pred_tasks.meta[var]) != 10:
                    raise Exception(var, len(data.multi_pred_tasks.meta[var])) 
                datasets.append([var] + data.multi_pred_tasks.meta[var])
        desc = data.multi_pred_tasks.desc[task]
        args = {
            "datasets": datasets,
            "task": task,
            "desc_id": desc[0],
            "desc_title": desc[1],
            "desc_desc": desc[2],
            "desc_impact": desc[3],
            "desc_gen": desc[4],
            "desc_product": desc[5],
            "desc_pipeline": desc[6],
        }
        return render_template("multi_pred_tasks/task.html", **args)
    else:
        return redirect("/multi_pred_tasks/overview")
        


if __name__ == '__main__':
    app.run(debug=True)  # debug=True for development mode