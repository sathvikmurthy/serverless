import subprocess
import tempfile

def execute_function(func):
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