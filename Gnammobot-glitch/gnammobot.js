//gnammobot - glitch

const { Telegraf } = require('telegraf');
const fs = require('fs');

// Create a new instance of the Telegraf bot using your bot token
const bot = new Telegraf('TELEGRAM_BOT_TOKEN');

// Get today's date
const today = new Date();
const formattedDate = `${today.getFullYear()}-${(today.getMonth() + 1).toString().padStart(2, '0')}-${today.getDate().toString().padStart(2, '0')}`;

// URL for the catering menu
const url = `https://www.mazzotti.org/bassaromagnacatering/calendar.php?comune=7&grado=2&giorno=${formattedDate}`;

// Send a GET request to the URL
const response = await axios.get(url, { httpsAgent: agent });

// Create a BeautifulSoup object to parse the HTML content
const soup = BeautifulSoup(response.data, "html.parser");

// Find the div element with the class "fc-day-number" containing today's day number
const dayElement = soup.find("div", { class: "fc-day-number", text: formattedDate });

// Find the parent div element with class "fc-div-content"
const divContentElement = dayElement.parent;

// Find the nested div element with class "menu-calendar"
const menuElement = divContentElement.find("div", { class: "menu-calendar" });

// Check if menu is available for today
if (menuElement) {
  // Extract the menu text
  let menuText = menuElement.text.trim();
  menuText = menuText.replace(/\n/g, '  \n');  // Replace line breaks with two spaces and a line break

  // Create the Markdown content
  const markdownContent = `Oggi si mangia:\n\n${menuText}`;

  // Save the Markdown content to output.md file
  fs.writeFileSync('output.md', markdownContent);
} else {
  fs.writeFileSync('output.md', 'No menu available for today.');
}

// Start command handler
bot.start((ctx) => ctx.reply('Ciao, sono gnammobot! Ti posso aiutare a scoprire qual è il menù di oggi nelle mense scolastiche servite da Bassa Romagna Catering'));

// Help command handler
bot.help((ctx) => ctx.reply('Ti aiuto io!'));

// Menu command handler
bot.command('menu', async (ctx) => {
  const content = fs.readFileSync('output.md', 'utf-8');
  ctx.replyWithMarkdown(content);
});

// Launch the bot
bot.launch();