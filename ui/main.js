const { app, BrowserWindow, ipcMain } = require("electron");
const { spawn } = require("child_process");
const path = require("path");

let pyProc;

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 400,
    webPreferences: {
      preload: path.join(__dirname, "src", "index.js"),
    },
  });

  win.loadFile(path.join(__dirname, "src", "index.html"));
}

app.whenReady().then(() => {
  // Spawn Python core
  pyProc = spawn("python3", [path.join(__dirname, "../core/main.py")]);
  console.log("start");

  // Event: data dari Python
  pyProc.stdout.on("data", (data) => {
    try {
      const message = JSON.parse(data.toString());
      mainWindow.webContents.send("fromPython", message);
    } catch (err) {
      console.error("Failed to parse:", data.toString());
    }
  });

  // Error log
  pyProc.stderr.on("data", (data) => {
    console.error(`Python error: ${data}`);
  });

  createWindow();
});

app.on("will-quit", () => {
  if (pyProc) pyProc.kill();
});
