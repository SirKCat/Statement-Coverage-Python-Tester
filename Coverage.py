import os


def coverage(name):
    if os.path.isfile(name + '_Cov_test.py'):
        os.remove(name + '_Cov_test.py')
    counter = 0
    with open(name + "_Cov_test.py", "a") as out:
        with open(name + ".py", "r") as code:
            out.write("global _TheTestingCounter_\n")
            out.write("_TheTestingCounter_ = 0 \n")
            for i in code:
                if i[0] == '\n':
                    out.write(i)
                elif i[0] != ' ':
                    if i[:3] == "def":
                        out.write('_TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        counter += 1
                        out.write(i)
                        out.write("    global _TheTestingCounter_\n")
                    else:
                        counter += 1
                        out.write('_TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        out.write(i)



                else:
                    x = i.split("    ")
                    space = ""
                    lecounter = -1
                    indentation = "    "
                    for space in x:
                        lecounter = lecounter + 1
                    indentation = indentation * lecounter

                    if x[lecounter][:4] == "elif" or x[lecounter][:4] == "else":
                        out.write(indentation + '    _TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        counter += 1
                        out.write(i)

                    else:
                        out.write(indentation + '_TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        counter += 1
                        out.write(i)

            out.close()
        code.close()
    return counter


def decision(name):
    if os.path.isfile(name + '_Dec_test.py'):
        os.remove(name + '_Dec_test.py')
    counter = 0
    with open(name + "_Dec_test.py", "a") as out:
        with open(name + ".py", "r") as code:
            out.write("_TheTestingCounter_ = 0 \n")
            for i in code:
                if i[0] == '\n':
                    out.write(i)
                elif i[0] == ' ':
                    x = i.split("    ")
                    space = ""
                    lecounter = -1
                    indentation = "    "
                    for space in x:
                        lecounter = lecounter + 1
                    indentation = indentation * lecounter
                    if x[lecounter][:4] == "elif" or x[lecounter][:4] == "else":
                        out.write(indentation + '    _TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        counter += 2
                        out.write(i)
                    elif x[lecounter][:2] == "if":
                        out.write(indentation + '_TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                        counter += 2
                        out.write(i)

                    else:
                        out.write(i)
                        if i[:2] == 'if':
                            out.write('_TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                            out.write(i)
                            counter = counter + 2
                        elif i[:4] == 'elif':
                            out.write('    _TheTestingCounter_ = _TheTestingCounter_ + 1 \n')
                            out.write(i)
                            counter = counter + 2

                else:
                    out.write(i)

            out.close()
        code.close()
    return counter
