#!/usr/env python3

"""
Author: Elf41
Inspired by: https://github.com/crackedskull/Stabilize-ReverseShell/blob/main/stabilize_rev_shell.py
https://github.com/RoqueNight/Reverse-Shell-TTY-Cheat-Sheet
"""

import pyautogui as pya
import time

def withShift(str):
    with pya.hold("shift"):
        pya.press(str)

def withCtrl(str):
    with pya.hold("ctrl"):
        pya.press(str)

def write_bin():
    withShift('/')
    pya.write("bin")

def write_sh():
    write_bin()
    withShift('/')
    pya.write("sh")

def write_bash():
    write_bin()
    withShift('/')
    pya.write("bash")

def write_dash():
    write_bin()
    withShift('/')
    pya.write("dash")

def write_zsh():
    write_bin()
    withShift('/')
    pya.write("zsh")

def write_ksh():
    write_bin()
    withShift('/')
    pya.write("ksh")

def not_supported():
    perror("Not Supported")

def write_vi_or_vim(v_num="1"):
    match int(str(v_num)[0]):
        case 1:
            pya.write("vi")
        case 2:
            pya.write("vim")
        case _:
            pya.write("vi")

def choose_shell_path(shell_number_str="2"):
    match int(str(shell_number_str)[0]):
        case 1:
            write_sh()
        case 2:
            write_bash()
        case 3:
            write_dash()
        case 4:
            write_zsh()
        case 5:
            write_ksh()
        case _:
            write_bash()

def choose_shell_write_name(shell_number_str="2"):
    match int(str(shell_number_str)[0]):
        case 1:
            pya.write("sh")
        case 2:
            pya.write("bash")
        case 3:
            pya.write("dash")
        case 4:
            pya.write("zsh")
        case 5:
            pya.write("ksh")
        case _:
            pya.write("bash")

def use_python_to_stabilize(shell_num="2", version=""):
    # python -c 'import pty; pty.spawn("/bin/bash")'
    
    pya.write("python")
    pya.write(version)
    pya.write(" -c")
    pya.press(' ')
    withShift("'")

    pya.write("import pty")
    withShift(';')
    pya.press(' ')

    pya.write("pty.spawn")
    withShift('(')
    withShift('"')

    choose_shell_path(shell_num)

    withShift('"')
    withShift(')')
    withShift("'")

def use_script_to_stabilize(shell_num="2"):
    # /usr/bin/script -qc /bin/bash /dev/null
    withShift('/')
    pya.write("usr")
    write_bin()
    withShift('/')
    pya.write("script")

    pya.press(' ')

    pya.write("-qc")

    pya.press(' ')

    choose_shell_path(shell_num)

    pya.press(' ')

    withShift('/')
    pya.write("dev")
    withShift('/')
    pya.write("null")

def use_ruby_to_stabilize(shell_num="2"):
    # ruby -e "exec '/bin/bash'"
    pya.write("ruby -e")
    pya.press(' ')
    
    withShift('"')
    pya.write("exec")
    pya.press(' ')

    withShift("'")
    choose_shell_path(shell_num)
    withShift("'")
    withShift('"')

def use_perl_to_stabilize(shell_num="2"):
    # perl -e "exec '/bin/bash';"
    pya.write("perl -e")
    pya.press(' ')

    withShift('"')
    pya.write("exec")
    pya.press(' ')

    withShift("'")
    choose_shell_path(shell_num)
    withShift("'")
    withShift(';')
    withShift('"')

def use_lua_inline_to_stabilize(shell_num="2"):
    # lua -e "os.execute('/bin/bash')"
    pya.write("lua -e")
    pya.press(' ')

    withShift('"')
    pya.write("os.execute")
    pya.press('(')
    withShift("'")
    choose_shell_path(shell_num)
    withShift("'")
    withShift(')')
    withShift('"')

def use_lua_to_stabilize(shell_num="2"):
    # lua [enter] os.execute('/bin/bash')
    pya.write("lua")
    pya.press('enter')

    pya.write("os.execute")
    pya.press('(')
    withShift("'")
    choose_shell_path(shell_num)
    withShift("'")
    withShift(')')

def use_vi_or_vim_to_stabilize(shell_num="2", v_num="1"):
    # vi [enter] :!bash
    write_vi_or_vim(v_num)
    pya.press("enter")
    pya.press("esc")
    withShift(":")
    withShift("!")
    choose_shell_write_name(shell_num)
    pya.press("enter")


def main():
    which_one = input("[!]\tAfter you answered the last questions you will have 3 seconds\n\tto take your cursor to the terminal in which the nc session is running\n\n[?]\tHow should the shell get stabilized?\n--------------------------------------------\n0:\tFast (python no further questions)\n1:\tpython (default)\n2:\tpython + version\n3:\tscript\n4:\truby\n5:\tperl\n6:\tlua\n7:\tvi or vim\n")
    if (which_one == "0"):
        assert(1==1)
    else:
        if (which_one == "2"):
            which_py_version = input("[?]\tWhich python version would you like?\n--------------------------------------------\n1:\tpython3 (default)\n2:\tpython2\n")
            if (which_py_version == "" or which_py_version == "1"):
                which_py_version = "3"
        elif (which_one == "6"):
            which_lua_expr = input("[?]\tWhich lua expr would you like to Invoke?\n------------------------------------------------\n1:\tinline (default)\n2:\teditor\n")
            if (which_lua_expr == ""):
                which_lua_expr = "1"
        elif (which_one == "7"):
            v_number = input("[?]\tvi or vim?\n------------------\n1:\tvi (default)\n2:\tvim\n")
            if (v_number == ""):
                v_number = "1"
        which_shell = input("[?]\tWhich shell?\n--------------------\n1:\tsh\n2:\tbash (dafault)\n3:\tdash\n4:\tzsh\n5:\tksh\n")
        if (which_shell == ""):
            which_shell = "2"
        with_color = input("[?]\tShould we try to export xterm-256color? (Y/n)\n-----------------------------------------------------\n")
        if (with_color == ""):
            with_color = "n"

        

    if (which_one == ""):
        which_one = "0"

    print("[!]\tTake your cursor to the terminal in which the nc session is running")

    time.sleep(3)

    print("[*]\tInitializing Script...")

    match int(str(which_one)[0]):
        case 0:
            use_python_to_stabilize(which_shell, "")
        case 1:
            use_python_to_stabilize(which_shell, "")
        case 2:
            use_python_to_stabilize(which_shell, which_py_version)
        case 3:
            use_script_to_stabilize(which_shell)
        case 4:
            use_ruby_to_stabilize(which_shell)
        case 5:
            use_perl_to_stabilize(which_shell)
        case 6:
            if (which_lua_expr == "1"):
                use_lua_inline_to_stabilize(which_shell)
            elif (which_lua_expr == "2"):
                use_lua_to_stabilize(which_shell)
            else:
                use_lua_inline_to_stabilize(which_shell)
        case 7:
            use_vi_or_vim_to_stabilize(which_shell, v_number)
        case 8:
            not_supported()
        case _:
            use_python_to_stabilize(which_shell, "")

    pya.press("enter")
    time.sleep(1)

    with pya.hold("ctrl"):
        pya.press("z")

    pya.write("stty raw -echo")
    pya.press("enter")
    time.sleep(1)

    pya.write("fg")
    pya.press("enter")
    pya.press("enter")
    time.sleep(1)

    pya.write("export TERM")
    withShift('=')
    if with_color == "N" or with_color == "n":
        pya.write("xterm")
    elif with_color == "Y" or with_color == "y":
        pya.write("xterm-256color")
    else:
        pya.write("xterm")
    pya.press("enter")
    time.sleep(1)

    print("[+]\tShell Stabilized!")
    exit()

main()
