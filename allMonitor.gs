/**
 * This is an automated function that will cache new emails as they are added.
 * 
 * @param {context} e This is the default onEdit function parameter.
 */
function onEdit(e) {
  const cache = CacheService.getScriptCache();
  const activeSheet = e.source.getActiveSheet();
  const range = e.range;
  if (activeSheet.getName() === "All") {                           //set trigger to 'CONTACT' sheet only
    const currentColumn = range.getColumn();
    if (currentColumn === 1) {                                          //only trigger when a new email is added
      const data = activeSheet.getDataRange().getValues();
      const lengthOfRows = activeSheet.getLastRow();
      for (var row = 1; row < lengthOfRows; row++) {                    //for each row get the emails
        cache.put(row, data[row][0]);
      }
    };
  }
};

function test() {                                                       //default cache expiration time is 10mins/600secs
  var cache = CacheService.getScriptCache();
  Logger.log(cache.get([1]));
  Logger.log(cache.get([2]));
  Logger.log(cache.get([3]));
  Logger.log(cache.get([4]));
}