def list_benefits():
    a = """"More organized code", 
    "More readable code", 
    "Easier code reuse", 
    "Allowing programmers to share and connect code together"""
    return a.split(",")         

def build_sentence(benefit):
    return benefit+" is the benefit of the functions! "

def name_the_benefits_of_functions():

    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print build_sentence(benefit)

name_the_benefits_of_functions()