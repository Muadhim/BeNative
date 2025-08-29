const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("beNative", {
  sendMessage: (msg) => {
    console.log("setnd message");
    // kirim ke Python via stdin
    process.stdin.write(JSON.stringify(msg) + "\n");
  },
  onMessage: (callback) =>
    ipcRenderer.on("fromPython", (_, data) => callback(data)),
});
