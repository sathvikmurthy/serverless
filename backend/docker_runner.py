import subprocess
import tempfile

def execute_function(func):
    if func['language'] == 'python':
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False) as f:
            f.write(func['code'])
            f.flush()
            cmd = ["docker", "run", "--rm", "-v", f.name+":/app/script.py", "python:3.9", "python", "/app/script.py"]
            try:
                output = subprocess.check_output(cmd, timeout=func['timeout'], stderr=subprocess.STDOUT)
                return output.decode()
            except subprocess.TimeoutExpired:
                return "Execution timed out"
            except subprocess.CalledProcessError as e:
                return e.output.decode()
    elif func['language'] == 'javascript':
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.js', delete=False) as f:
            f.write(func['code'])
            f.flush()
            cmd = ["docker", "run", "--rm", "-v", f.name+":/app/script.js", "node:20", "node", "/app/script.js"]
            try:
                output = subprocess.check_output(cmd, timeout=func['timeout'], stderr=subprocess.STDOUT)
                return output.decode()
            except subprocess.TimeoutExpired:
                return "Execution timed out"
            except subprocess.CalledProcessError as e:
                return e.output.decode()