const { createClient } = require('contentful');
const { SPACE_ID, ACCESS_TOKEN, CONTENT_TYPE } = process.env;

module.exports.get = (e, ctx, cb) => {
  const client = createClient({
    space: SPACE_ID,
    accessToken: ACCESS_TOKEN,
  });
  const getArticles = ({ items }) => {
    const content = items.find(({ name }) => name === CONTENT_TYPE);
    return client
      .getEntries({ content_type: content.sys.id })
      .then(response => response.items)
      .catch(error => cb(error));
  };
  client
    .getContentTypes()
    .then(getArticles)
    .then(items => {
      cb(null, items);
    })
    .catch(error => cb(error));
};
