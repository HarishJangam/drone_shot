import os
import json
from flask import Flask,request, Response
import json

app = Flask(__name__)
DB = "DB"
schema = {}

def req_body_validation(table: str, schema: dict, req_body : dict, check_required: bool=False) -> str:
    req_body_requirement = schema.get(table)
    err_msg = []
    
    if not req_body_requirement:
        return f"{table} schema is not available"
    #  Checking allowed attributes
    allowed_attr = req_body_requirement.keys() # ["fullname", "age", "username", "password"]
    for key, val in req_body.items():
        if key not in allowed_attr:
            err_msg.append(f"{key} is unkown")
    
    # Checking required attributes
    if check_required:
        required_attrs = [key for key, val in req_body_requirement.items() if val.get("required")]
        for key, val in req_body_requirement.items():
            if val.get("required") and key not in req_body:
                err_msg.append(f"{key} is required")
    
    for key, val in req_body.items():
        if key not in req_body_requirement:
            continue
        
        requred_type = req_body_requirement.get(key, {}).get("type")
        actual_type = type(val).__name__
        if requred_type != actual_type:
            err_msg.append(f"{key} type should be {requred_type}")
    

    return ", ".join(err_msg)

def read_file(table: str, record_id: str) -> dict:
    data = {}
    with open(f"{DB}/{table}/{record_id}.json", "r") as f:
        data = json.load(f)
        
    return data

def update_file(table, record_id, req_body) -> dict:
    data = read_file(table, record_id)
    data = {**data, **req_body}
    
    with open(f"{DB}/{table}/{record_id}.json", "w") as f:
        json.dump(data, f)
    
    return data

def create_file(table, record_id, req_body) -> dict:
    with open(f"{DB}/{table}/{record_id}.json", "w") as f:
        json.dump(req_body, f)
    
    return req_body

def delete_file(table, record_id) -> None:
    # update_file(table, record_id, {"delete": True})
    if os.path.exists(f"{DB}/{table}/{record_id}.json"):
        os.remove(f"{DB}/{table}/{record_id}.json")

def get_no_of_files(table: str) -> int:
    files = os.listdir(f"{DB}/{table}")
    return len(files)

def read_all_files(table: str) -> list:
    files = os.listdir(f"{DB}/{table}")
    files = [f[:-5] for f in files if f.endswith(".json")]
    data = []
    for file in files:
        data.append(read_file(table, file))
    return data
def file_not_exists(table, record_id):
    if os.path.exists(f"{DB}/{table}/{record_id}.json"):
        return False
    
    return True

def table_not_exists(table):
    if os.path.exists(f"{DB}/{table}"):
        return False
    
    return True

tags = {
    "customer": "CUST",
    "drone_shot": "DRST",
    "location": "LOC",
    "booking": "BKNG"
}
#  rountes
@app.route("/api/<table>",methods = ["GET"])
def get_records(table):
    records = []
    status = 200
    err_msg = ""
    if table_not_exists(table):
        err_msg = f"{table} not found"
        status = 404
    else:
        records = read_all_files(table)
    
    resp =  json.dumps({
        "error": err_msg,
        "data": records
    })
    return Response(response=resp.encode(), content_type="application/json", status=status)


@app.route("/api/<table>/<record_id>",methods = ["GET"])
def get_single_record(table, record_id):
    err_msg = ""
    status = 200
    record = {}
    if file_not_exists(table, record_id):
        err_msg = f"{table}/{record_id} not found"
        status = 404
    else:
        record = read_file(table, record_id)
    
    resp =  json.dumps({
        "error": err_msg,
        "data": record
    })
    return Response(response=resp.encode(),content_type="application/json", status=status)

@app.route("/api/<table>",methods = ["POST"])
def create_record(table):
    req_body=request.json
    status = 200
    record = {}
    err_msg = req_body_validation(table, schema, req_body, check_required=True)
    if err_msg:
        status = 400
    else:
        tag = tags.get(table, "RD")
        count = str(get_no_of_files(table) + 1)
        record_id = tag + count.rjust(8, "0")
        req_body[f"{table}_id"] = record_id
        record = create_file(table, record_id, req_body)
    
    resp =  json.dumps({
        "error": err_msg,
        "data": record
    })
    return Response(response=resp.encode(),content_type="application/json", status=status)


@app.route("/api/<table>/<record_id>",methods = ["PATCH"])
def update_record(table, record_id):
    req_body=request.json
    status = 200
    record = {}
    if file_not_exists(table, record_id):
        err_msg = f"{table}/{record_id} not found"
        status = 404
    
    else:
        err_msg = req_body_validation(table, schema, req_body)
        if err_msg:
            status = 400
        else:
            record = update_file(table, record_id, req_body)
    
    resp =  json.dumps({
        "error": err_msg,
        "data": record
    })
    return Response(response=resp.encode(),content_type="application/json", status=status)

@app.route("/api/<table>/<record_id>",methods = ["DELETE"])
def delete_record(table, record_id):
    status = 200
    err_msg=""
    if file_not_exists(table, record_id):
        err_msg = f"{table}/{record_id} not found"
        status = 404
    else:
        delete_file(table, record_id)
    
    resp =  json.dumps({
        "error": err_msg,
        "data": {}
    })
    return Response(response=resp.encode(),content_type="application/json", status=status)

if __name__ == "__main__":
    with open("required.json","r") as f:
        schema=json.load(f)
    
    app.run(debug=True) 
    
"""
response format:
response = {
    "error": "",
    "data": ""
}
"""
