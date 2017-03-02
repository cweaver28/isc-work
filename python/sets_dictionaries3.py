d = {"maggie": "UK", "ronnie": "usa"}
dir(d)
d.items()
d.keys()
print d.values()
d.get("maggie", "nowhere")
res = d.setdefault("mikhail", "ussr")
print res, d["mikhail"]

