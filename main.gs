
/**
* This function returns all the available google sheets.
*
* @returns {sheets} all sheets in the document.
*/
function getSheetNames(){
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheets = ss.getSheets();
  const sheetNames = sheets.map(sheet=> {
    return sheet.getSheetName();
  })
  return sheetNames;
}

/**
 * This function return the data from the sheet as strings.
 * 
 * @param {string} sheetName The name of the sheet to read.
 * @param {number} firstRow The first row to start reading from.
 * @param {number} column The column to read.
 * @returns {Array} out The cells in an array.
 */
function readData(sheetName, firstRow, column) {
  const out = new Array();
  const sheet = SpreadsheetApp.getActive().getSheetByName(sheetName);
  const data = sheet.getDataRange().getValues();
    var lengthOfRows = sheet.getLastRow();
     for (var row = firstRow; row < lengthOfRows; row++) {
         out.push(data[row][column]);
    }
  return out;
}

function dripStatus() {

}

function checkStatus() {

  //Infinite while loop to check the drip system
  while (True) {

  }
}
