def default():
    output = load_template("html", {"file_name": arguments[0]})
    create_file(output, "public/html/" + arguments[0] + ".html")

def undo():
    delete_file("public/html/" + arguments[0] + ".html")
