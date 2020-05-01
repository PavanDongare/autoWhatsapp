const puppeteer = require('puppeteer');
const urlBase = 'https://web.whatsapp.com/send?phone=918698800448&text=I%27m+interested+in+your+car+for+sale&source&data&app_absent=true';

async function main() {
      const browser = await puppeteer.launch({ // 1
        headless: false,
        userDataDir: './pavan',
      });

      let pages = await browser.pages();

      const page = pages[0]; // 2 
      await page.goto(urlBase, { waitUntil: 'networkidle0' }); // wait until page load

      const [response] = await Promise.all([
        page.waitForNavigation(), // The promise resolves after navigation has finished
      ]);

      await page.mainFrame()
        .waitForSelector('._35EW6')
        .then(() => {
            page.evaluate(() => {
                document.querySelector('._35EW6').click();
             })
        });
}

main();
