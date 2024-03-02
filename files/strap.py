for pv[get_pid()]["f"] in ["wget.lja", "wget.py"]:
    shutil.copy(i, path.join(root, "bin", i))

be.api.setvar("return", "0")
