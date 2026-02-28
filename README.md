## CometBot
CometBot pulls current comet data from [COBS](https://cobs.si/) and sends a report to discord via webhooks. I made this to make sure I am always up to date on current comet situation, so that I can take pictures of those comets, that are bright enough.

### How does it work?
CometBot requests data of all comets that have current magnitude at least 15 (variable MAG1). It than discards all comets, that have peak magnitude date older than two week ago and comets with peak magnitude larger than 10 (variable MAG2). Then it sorts them by peak magnitute date and constructs a table inside of a code block to represent the data in a nice way. This table will wrap if the screen is too small (like on mobile) and it will become completly unreadable, so it also sends the same data in form of a discord embed (one embed per comet). That is it.

### How to use?
- Put your webhook url into a .env file (contents of .env: `'WEBHOOK'='your webhook url'`).
- Set up a cron job to periodically run main.py