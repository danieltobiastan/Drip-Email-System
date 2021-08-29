function getSheetNames(){
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheets = ss.getSheets();

  const sheetNames = sheets.map(sheet=> {
    return sheet.getSheetName();
  })

  Logger.log(sheetNames[0]);
  readData(sheetNames[0]);                                              //read contact sheet
}

function readData(sheetName) {
  var out = new Array()
  var sheet = SpreadsheetApp.getActive().getSheetByName(sheetName);
  var data = sheet.getDataRange().getValues();
  for(var col = 0; col < data.length; col++) {
     for (var row = 0; row < data[col].length; row++) {
         Logger.log(data[col][row]);                                    //read each cell left to right and top to bottom
    }
  }
}


function sendEmail() {

  //Infinite while loop to check the drip system
  while (True) {

  }
}

