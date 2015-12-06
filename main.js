const electron = require('electron');
const app = electron.app;  // Module to control application life.
const BrowserWindow = electron.BrowserWindow;  // Module to create native browser window.
const ipc = require("electron").ipcMain;
const fs = require('fs');

// Report crashes to our server.
electron.crashReporter.start();

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
var mainWindow = null;

// Quit when all windows are closed.
app.on('window-all-closed', function() {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform != 'darwin') {
    app.quit();
  }
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
app.on('ready', function() {
  // Create the browser window.
  mainWindow = new BrowserWindow({width: 1920, height: 1024});

  console.log("teafashdöfoaiwhegöoaiwh");

  // fs.readdir('F:\\projects\\swymtest', function(err, files) {
  //   console.log("show files server"+files[0]);
  //   mainWindow.webContents.send('show-files', files);
  // });
  //mainWindow.send('show-files', 'nice message');

  // and load the index.html of the app.
  mainWindow.loadURL('file://' + __dirname + '/index.html');

  mainWindow.webContents.on('did-finish-load', function() {
   //mainWindow.webContents.send('show-files', 'whoooooooh!');
   fs.readdir('F:\\projects\\swymtest', function(err, files) {
     console.log("show files server"+files[0]);
     mainWindow.webContents.send('show-files', files);
   });
  });

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function() {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
});
