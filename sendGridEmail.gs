//Global variables
const SENDGRID_KEY = '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';

/**
 *  This function sets up the emails being sent.
 * 
 * @param {string} recipient email address.
 * @returns {Array} array including header and header
 */
function setUpEmails(recipient) {
  var header = {
    "Authorization" : "Bearer "+SENDGRID_KEY, 
    "Content-Type": "application/json" 
  }
  var body = {
    "personalizations": [{
      "to": [{
          "email": recipient
        }],
      "subject": "Hello, World!"
    }],
    "from": {
      "email": "theoridho6@gmail.com"
    },
    "content": [{
        type: "text/html",
        value: "<html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>"
    }]
  }
  return [header, body];
}

/**
 * This function sends email sequentially with the given setUpEmails values.
 * 
 * @param {string} recipients of the email
 */
function sendEmail(recipients) {
  email = setUpEmails(recipients);
  headers = email[0];
  body = email[1];
  const options = {
    'method':'post',
    'headers':headers,
    'payload':JSON.stringify(body)
  }

  const response = UrlFetchApp.fetch("https://api.sendgrid.com/v3/mail/send",options);                    //sends the fetch request to the api
}

/**
 * This function works by sending all the given emails as batches
 */
function sendBacth() {
  var contact = getSheetNames()[0];
  var emails = readData(contact, 1, 0);
  for (var i = 0; i < emails.length; i++) {
    sendEmail(emails[i]);
    Logger.log('email '+ '   ' +  i.toString() + '  ' + 'sent to' + '  ' +  emails[i])
  }
  Logger.log("Complete");
}
