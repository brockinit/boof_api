const Mailchimp = require('mailchimp-api-v3');

module.exports.handler = (event, context, callback) => {
  const API_KEY = process.env.API_KEY;
  const mailchimp = new Mailchimp(API_KEY);
  mailchimp
    .request({
      method: 'post',
      path: '/lists/96d472b10a/members',
      body: {
        email_address: event.emailAddress,
        status: 'subscribed',
        merge_fields: {
          FNAME: event.firstName,
          LNAME: event.lastName,
          NOTE: event.contactUsNote
        }
      },
    })
    .then(function(results) {
      callback(null, {
        statusCode: 200,
        body: JSON.stringify({ test: 'object' }),
      });
    })
    .catch(function(err) {
      callback(err, {
        statusCode: 500,
      });
    });
};
