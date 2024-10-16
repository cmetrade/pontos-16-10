const { defineConfig } = require("cypress");

module.exports = defineConfig({

  defaultCommandTimeout: 100000,
  viewportWidth: 1000,
  viewportHeight: 600,
  pageLoadTimeout: 100000,

  component: {
    viewportWidth: 500,
    viewportHeight: 500,
  },
  
  e2e: {
    setupNodeEvents(on, config) {
        //defaultCommandTimeout: 100000
        pageLoadTimeout: 100000 
    },
  chromeWebSecurity: false
  },
});
