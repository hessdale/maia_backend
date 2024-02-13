import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.post("/api/client-login")
def post_login():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        token=uuid4().hex
        results = dbhelper.run_procedure("call post_client_session(?,?,?)",[token,request.json.get("username"),request.json.get("password")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.delete("/api/client-login")
def delete_login():
    try:
        error = dbhelper.check_endpoint_info(request.headers,["token"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure("call delete_client_session(?)",[request.headers.get("token")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.get("/api/design-images")
def get_design_images():
    try:
        results = dbhelper.run_procedure("call get_design_images()",[])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.get("/api/misc-images")
def get_misc_images():
    try:
        results = dbhelper.run_procedure("call get_misc_images()",[])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

@app.get("/api/portrait-images")
def get_portrait_images():
    try:
        results = dbhelper.run_procedure("call get_portrait_images()",[])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("sorry something went wrong",500)
    # some except blocks with possible errors
    except TypeError:
        print("invalid input type, try again.")
    except UnboundLocalError:
        print("coding error")
    except ValueError:
        print("value error, try again") 

if(dbcreds.production_mode == True):
    print("Running Production Mode")
    import bjoern #type: ignore
    bjoern.run(app,"0.0.0.0",5000)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)
