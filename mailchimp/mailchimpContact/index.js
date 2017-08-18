const Mailchimp = require('mailchimp-api-v3');

module.exports.handler = (event, context, callback) => {
  const { CONTACT_LIST_ID, API_KEY } = process.env;
  const mailchimp = new Mailchimp(API_KEY);
  mailchimp
    .request({
      method: 'post',
      path: `/lists/${CONTACT_LIST_ID}/members`,
      body: {
        email_address: event.emailAddress,
        status: 'subscribed',
        merge_fields: {
          FNAME: event.firstName,
          LNAME: event.lastName,
          NOTE: event.contactUsNote,
        },
      },
    })
    .then(function(results) {
      callback(null, {
        statusCode: 200,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ success: true }),
      });
    })
    .catch(function(err) {
      callback(err, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        statusCode: 500,
      });
    });
};
