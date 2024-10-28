const { exec } = require("child_process");

setInterval(() => {
  exec(`git add . && git commit -m "Auto commit" && git push origin main`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error}`);
      return;
    }
    console.log(`Output: ${stdout}`);
  });
}, 5000); // 5000ms = 5 seconds
