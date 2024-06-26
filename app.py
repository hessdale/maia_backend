import dbcreds
import dbhelper
import smtplib
from uuid import uuid4
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.post("/api/client")
def post_client():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        if(error != None):
            return make_response(jsonify(error),400)
        salt=uuid4().hex
        results = dbhelper.run_procedure("call post_client(?,?,?)",[request.json.get("username"),request.json.get("password"),salt])
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

@app.get("/api/design-photos")
def get_design_images():
    try:
        results = dbhelper.run_procedure("call get_design_photos()",[])
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

@app.post("/api/design-images")
def post_design_image():
    try:
        error = dbhelper.check_endpoint_info(request.headers,["token"])
        if(error != None):
            return make_response(jsonify(error),400)
        is_valid = dbhelper.check_endpoint_info(request.files, ['uploaded_image'])
        if(is_valid != None):
            return make_response(jsonify(is_valid), 400)
        # Save the image using the helper found in apihelpers
        file_name = dbhelper.save_file(request.files['uploaded_image'])
        # If the filename is None something has gone wrong
        error = dbhelper.check_endpoint_info(request.form,["image_description"])
        if(error != None):
            return make_response(jsonify(error),400)
        if(file_name == None):
            return make_response(jsonify("Sorry, something has gone wrong"), 500)
        results = dbhelper.run_procedure("call post_design_photo(?,?,?)",[request.headers.get("token"),file_name,request.form["image_description"]])
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

@app.get("/api/misc-photos")
def get_misc_images():
    try:
        results = dbhelper.run_procedure("call get_misc_photos()",[])
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

@app.post("/api/misc-images")
def post_misc_image():
    try:
        error = dbhelper.check_endpoint_info(request.headers,["token"])
        if(error != None):
            return make_response(jsonify(error),400)
        is_valid = dbhelper.check_endpoint_info(request.files, ['uploaded_image'])
        if(is_valid != None):
            return make_response(jsonify(is_valid), 400)
        # Save the image using the helper found in apihelpers
        file_name = dbhelper.save_file(request.files['uploaded_image'])
        # If the filename is None something has gone wrong
        error = dbhelper.check_endpoint_info(request.form,["image_description"])
        if(error != None):
            return make_response(jsonify(error),400)
        if(file_name == None):
            return make_response(jsonify("Sorry, something has gone wrong"), 500)
        results = dbhelper.run_procedure("call post_misc_photo(?,?,?)",[request.headers.get("token"),file_name,request.form["image_description"]])
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

@app.get("/api/portrait-photos")
def get_portrait_images():
    try:
        results = dbhelper.run_procedure("call get_portrait_photos()",[])
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

@app.post("/api/portrait-images")
def post_portrait_image():
    try:
        error = dbhelper.check_endpoint_info(request.headers,["token"])
        if(error != None):
            return make_response(jsonify(error),400)
        is_valid = dbhelper.check_endpoint_info(request.files, ['uploaded_image'])
        if(is_valid != None):
            return make_response(jsonify(is_valid), 400)
        # Save the image using the helper found in apihelpers
        file_name = dbhelper.save_file(request.files['uploaded_image'])
        # If the filename is None something has gone wrong
        error = dbhelper.check_endpoint_info(request.form,["image_description"])
        if(error != None):
            return make_response(jsonify(error),400)
        if(file_name == None):
            return make_response(jsonify("Sorry, something has gone wrong"), 500)
        results = dbhelper.run_procedure("call post_portrait_photo(?,?,?)",[request.headers.get("token"),file_name,request.form["image_description"]])
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

@app.post("/api/contact-form")
def post_contact_form():
    try:
        error = dbhelper.check_endpoint_info(request.json,['FirstName','LastName','Email','Note'])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure("call post_contact_form(?,?,?,?)",[request.json['FirstName'],request.json['LastName'],request.json['Email'],request.json['Note']])
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
    bjoern.run(app,"0.0.0.0",6785)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)
