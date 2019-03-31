#!/usr/bin/env python3

import discord
import json
import sys

import diceFormulaParser as dice

# DISCORD CLIENT
client = discord.Client()

# HELPER FUNCTIONS
async def send_response(message, channel, user=None):
	if user:
		message = '{} {}'.format(user.mention, message)
	await client.send_message(channel, message)

def read_config(path):
	with open(path) as f:
	    data = json.load(f)
	return data

def format_roll(result, requester):
	individual = ', '.join(result['individual'])
	return 'Result: {}, Individual Rolls: {}'.format(result['total'], individual)

# COMMAND HANDLERS
async def on_roll(command_body, channel, requester):
	result = dice.get_dice_formula_result(command_body)
	message = format_roll(result, requester)
	await send_response(message, channel, requester)

# GLOBALS
config = read_config(sys.argv[1] if len(sys.argv) > 1 else 'config.json')
<<<<<<< HEAD
valid_commands = {'/roll' : on_roll}
=======
valid_commands = {'/roll' : on_roll, '/' : on_roll} # MAKE SURE THE SHORTCUT / COMMAND IS THE LAST ONE!
>>>>>>> 58f6b55... Added comment to not shoot myself in the foot

# DISCORD EVENT HANDLING
@client.event
async def on_ready():
	print('DiceBot is ready to roll!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return # We do not want to process our own messages

	for command, handler in valid_commands.items():
		if message.content.startswith(command):
			command_body = message.content[len(command):]
			await handler(command_body, message.channel, message.author)

client.run(config['bot_token'])
