def default():
    package_json = load_template("js", {"file_name": arguments[0]})
    create_file(package_json, "public/js/" + arguments[0] + ".js")

def undo():
    delete_file("public/js/" + arguments[0] + ".js")
