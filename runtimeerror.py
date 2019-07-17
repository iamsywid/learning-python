presents = iter(["phone", "camera", "laptop"])

def get_present_for(name):
    print(name + " got " + next(presents, "nothing"))


get_present_for("anna")
get_present_for("jane")
get_present_for("claire")
get_present_for("christine")


