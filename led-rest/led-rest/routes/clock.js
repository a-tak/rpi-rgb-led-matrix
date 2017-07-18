var express = require('express');
var path = require('path');
var router = express.Router();
var configFile = require('config');
//config配下のファイルを読みに行く
var settingsFilePath = configFile.config.modeFilePath
var modeFilePath =  path.join(settingsFilePath, 'mode');

// GET
router.get('/brightness', function(req, res, next) {
  
  res.json(userList);
});

// POST
router.post('/', function (req, res) {
  res.json('POST '  + req.body.id + ' OK');
});

// PUT
router.put('/mode', function (req, res) {
  value = req.body.value;
  var fs = require('fs');
  fs.writeFile(modeFilePath, value, function (err) {
    console.log(err);
  })
  res.json('PUT clock mode Change ' + req.body.value);
});

// DELETE
router.delete('/:id', function (req, res) {
  res.json('DELETE '  + req.params.id + ' OK');
});

module.exports = router;
