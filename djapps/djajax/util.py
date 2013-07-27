import os
import subprocess

ENV_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..%s" % (os.sep)))

def _run_script(script_name, path, *args):

    current_dir = os.getcwd()
    script = "./%s %s" % (script_name, ' '.join(args))
    path = os.path.join(ENV_ROOT, 'djajax')
    os.chdir(path)
    
    process = subprocess.Popen(script, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, executable="/bin/bash")
    out, err = process.communicate()
    os.chdir(current_dir)
        
    if err:
        print "err:%s" % err
        
    return out 

def run_script(param1):
    path = ''
    script_response = _run_script('script.sh', path, param1)
    return str(script_response)

