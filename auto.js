const puppeteer = require('puppeteer');
const urlBase = 'https://web.whatsapp.com/send?phone=918698800448&text=This+is+testing.+Please+ignore&source&data&app_absent=true';

contact = [919049481501,918698800448,918526262648];
msg= "testing";

async function main(contact,msg) {
      const browser = await puppeteer.launch({ // 1
        headless: false,
        userDataDir: './pavan',
      });

      let pages = await browser.pages();

      const page = pages[0]; // 2 
      
      contact.forEach(no => {
        const urlBase = 'https://web.whatsapp.com/send?phone='+ no +'&text='+msg+'&source&data&app_absent=true';
        page.goto(urlBase, { waitUntil: 'networkidle0' }); // wait until page load
  
        page.mainFrame()
          .waitForSelector('._35EW6')
          .then(() => {
              page.evaluate(() => {
                  document.querySelector('._35EW6').click();
               })
          });
      });
      
}

main(contact,msg);