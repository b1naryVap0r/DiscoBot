# https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot

import discord
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
#discord channel and bot specifics for api comms
def main():
    TOKEN = 
    client = discord.Client()
    channel = 

    # the actual ctf site for deets
    site= 'https://ctftime.org/event/list/upcoming'
    page = requests.get(site)

    @client.event
    async def on_message(message):

        # stops loops - bots shouldnt talk to themself
        if message.author == client.user:
            return

        #the talky bits - commands and replies
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')
        elif message.content.startswith('!commands'):
            await message.channel.send('Event BOI RESPONDS TO ALL THESE THINGS !!! --- :: !hello, !commands, !ctf, !pancakes')
        elif message.content.startswith('!pancakes'):
            await message.channel.send('!waffles are better')
        elif message.content.startswith('!waffles'):
            await message.channel.send('www.waffles.com')
        elif message.content.startswith('!ctf'):

            #stops 403's, websites don't like bots
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")

            #parse the table for upcoming ctf events
            table1= page_soup.find('table', {'class': 'table table-striped'})
            Names = table1.findAll('td')
            eventNames = []
            for Name in Names:
                eventNames.append(Name)
                eventNames = eventNames[:150] #2k char limit, 150 until formatting scrubbed

                #scrubber?
                

                #talky bit
                msg = 'Hello {0.author.mention}'.format(message)
                await message.channel.send(eventNames)
            
    @client.event #login deets to confirm established connection
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print(',-,-,-,-,-,-.')

#required to work- auth
    client.run(TOKEN)

#bc python
if __name__ == "__main__":
    main()