from app import app, db
from flask import jsonify, request, abort
from .models import HistoryCPU
from datetime import datetime
from sqlalchemy.sql import func


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file("index.html")


@app.route('/api/v1/data', methods=['GET'])
def get_data():
    page = request.args.get("page", type=int)
    page_size = request.args.get("page_size", type=int)
    sort = request.args.get("sort[]")
    sort_desc = request.args.get("sort_desc[]")
    if sort is not None:
        col = getattr(HistoryCPU, sort)
        if "true" in sort_desc:
            col = col.desc()
    else:
        col = HistoryCPU.id
    model = HistoryCPU.query.order_by(col).paginate(page, page_size, False)
    count = HistoryCPU.query.count()
    aggr_all = db.session.query(func.max(HistoryCPU.utilize).label("max"),
                            func.min(HistoryCPU.utilize).label("min"),
                            func.avg(HistoryCPU.utilize).label("avg")).one()
    sub_query = db.session.query(HistoryCPU.utilize.label("utilize")).order_by(HistoryCPU.id.desc()).limit(100).cte()
    aggr_100 = db.session.query(func.max(sub_query.c.utilize).label("max"),
                               func.min(sub_query.c.utilize).label("min"),
                               func.avg(sub_query.c.utilize).label("avg")).one()
    aggr = {
        "max": aggr_all.max,
        "min": aggr_all.min,
        "avg": round(aggr_all.avg, 2),
        "max100": aggr_100.max,
        "min100": aggr_100.min,
        "avg100": round(aggr_100.avg, 2),
    }
    result = list()
    for row in model.items:
        result.append({"id": row.id, "date": row.date, "utilize": row.utilize})
    response = jsonify({"total": count, "items": result, "aggr": aggr})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/api/v1/data', methods=['POST'])
def post_data():
    r = request
    if not request.form or not "utilize" in request.form:
        abort(400)
    history = HistoryCPU(utilize=request.form["utilize"], date=datetime.now())
    db.session.add(history)
    db.session.commit()
    return jsonify({"utilize": request.form["utilize"]})
