def default():
    package_json = load_template("css", {"file_name": arguments[0]})
    create_file(package_json, "public/css/" + arguments[0] + ".css")

def undo():
    delete_file("public/css/" + arguments[0] + ".css")
