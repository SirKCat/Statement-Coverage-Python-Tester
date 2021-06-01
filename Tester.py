import os
from Coverage import decision, coverage
from time import sleep

print(" =^..^= Welcome to the Statement - Decision Coverage tool v0.01 =^..^= ")
print("""\033[2;37;40m                              Made by (Khaled Redhwan) AKA 
                     ^___^          ╔═╗┬┬─┐ ╔═╗┌─┐┌┬┐          ^___^ 
                    ( o.o )         ╚═╗│├┬┘ ║  ├─┤ │          ( o.o )
                     > ^ <          ╚═╝┴┴└─o╚═╝┴ ┴ ┴           > ^ <  
\033[0;37;0m""")

name = input("To begin, What's the name of the file you want to test? ")


if os.path.isfile(name + '_Cov_test.py'):
    os.remove(name + '_Cov_test.py')
if os.path.isfile(name + '_Cov_engine.py'):
    os.remove(name + '_Cov_engine.py')
if os.path.isfile(name + '_Dec_test.py'):
    os.remove(name + '_Dec_test.py')
if os.path.isfile(name + '_Dec_engine.py'):
    os.remove(name + '_Dec_engine.py')



def engineCov():
    with open(name + "_Cov_engine.py", "a") as out:
        out.write("import Coverage\n")
        out.write(f"import {name}_Cov_test\n")
        out.write(f"_coverage = {name}_Cov_test._TheTestingCounter_/Coverage.coverage('{name}')\n\n\n")
        out.write("print('-------------------------------------------------------------------')\n")
        out.write("print('The statement coverage percentage is ',round(_coverage*100),'%')\n")
        out.write("print('-------------------------------------------------------------------')\n")


def enginDec():
    with open(name + "_Dec_engine.py", 'a') as out:
        out.write("import Coverage\n")
        out.write(f"import {name}_Dec_test\n")
        out.write(f"_coverage = {name}_Dec_test._TheTestingCounter_/Coverage.decision('{name}')\n\n\n")
        out.write("print('-------------------------------------------------------------------')\n")
        out.write("print('The decision coverage percentage is ',round(_coverage*100),'%')\n")
        out.write("print('-------------------------------------------------------------------')\n")

coverage(name)
decision(name)
enginDec()
engineCov()

print("\033[1;36;40m Please enter the input for the statement coverage Now!\033[0m")
os.system(f"cmd /c py {name + '_Cov_engine.py'}")
os.remove(name + '_Cov_test.py')
os.remove(name + '_Cov_engine.py')
print("\n\n\n\n\n\033[1;31;40m Please enter the input for the decision coverage Now!\033[0m")
os.system(f"cmd /c py {name + '_Dec_engine.py'}")
os.remove(name + '_Dec_test.py')
os.remove(name + '_Dec_engine.py')
print("Done!")
sleep(3)


