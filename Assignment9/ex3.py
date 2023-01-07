import subprocess


# ca min 20 in lecture

program = input("Enter program or press ENTER to exit: ")

if program is not None:
    args = list()
    arg = input("Enter argument or press ENTER to skip: ")
    while arg != "":
        args.append(arg)
        arg = input("Enter argument or press ENTER to skip: ")

    encoding = input("Enter encoding or press ENTER to skip: ")

    if len(args) == 0 and encoding == "":
        print(f"Running program '{program}' without any arguments and no encoding")

    if len(args) == 0 and encoding != "":
        print(f"Running program '{program}' without any arguments and encoding '{encoding}'")

    if len(args) > 0 and encoding == "":
        print(f"Running program '{program}' with arguments {args} and no encoding")

    if len(args) > 0 and encoding != "":
        print(f"Running program '{program}' with arguments {args}  and encoding '{encoding}'")

    try:
        p = subprocess.Popen([program, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=encoding)
        outs, errs = p.communicate()
        print(f"The program finished with exit code {p.returncode}")
        if outs != "" and outs != b'':
            print(f"The program produced the following standard output:\n{outs}")
        if errs != "" and errs != b'':
            print(f"The program produced the following error output:\n{errs}")
    except LookupError:
        print(f"The specified encoding '{encoding}' could not be found\n",)
    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")
