/**
 * This function add a datestamp to the date added column everytime a new email is added in CONTACT and will delete when the email is removed
 * 
 * @param {context} e This is the default onEdit function parameter.
 */
function onEdit(e) {
  const activeSheet = e.source.getActiveSheet();
  const range = e.range;
  if (activeSheet.getName() === "CONTACTS") {
    const currentColumn = range.getColumn();
    if (currentColumn === 2) {                                                                      // Only trigger when a new email is added in CONTACTS
    const currentRow = range.getRow();
    const numberOfRows = range.getNumRows();
      if (activeSheet.getRange(currentRow, currentColumn, numberOfRows).isBlank() == true){         // Check if the current cell is empty or not
        activeSheet.getRange(currentRow, 1, numberOfRows).setValue('');
      }
      else {
        const date = Utilities.formatDate(new Date(), "GMT+1", "dd/MM/yyyy");
        const currentRow = range.getRow();
        activeSheet.getRange(currentRow, 1, numberOfRows).setValue(date);
      }
    };
  }
};
