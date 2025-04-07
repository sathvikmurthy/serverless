const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { v4: uuidv4 } = require('uuid');

function runFunction({ code, language, timeout = 5 }) {
  return new Promise((resolve, reject) => {
    const id = uuidv4();
    const tempDir = path.join(__dirname, 'tmp', id);
    fs.mkdirSync(tempDir, { recursive: true });

    let filename, dockerImage, runCommand;

    if (language === 'python') {
      filename = 'handler.py';
      dockerImage = 'func-runner-python';
    } else if (language === 'javascript') {
      filename = 'handler.js';
      dockerImage = 'func-runner-js';
    } else {
      return reject(new Error('Unsupported language'));
    }

    // Write user code
    fs.writeFileSync(path.join(tempDir, filename), code);

    // Run container with timeout
    const dockerCmd = `docker run --rm -v ${tempDir}:/app ${dockerImage}`;

    const child = exec(dockerCmd, { timeout: timeout * 1000 }, (err, stdout, stderr) => {
      if (err) {
        if (err.killed) return reject(new Error("Execution timed out"));
        return reject(stderr || err.message);
      }
      resolve(stdout.trim());
    });
  });
}

module.exports = runFunction;
