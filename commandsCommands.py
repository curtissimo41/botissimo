import os
import json

cmdFile = f'{os.path.dirname(os.path.realpath(__file__))}/commandsBasic.txt'

def addcomm(cmd_JSON, alias, msg):
    """Add a new bot command."""
    if not alias or not msg:
        return 'Correct usage: !addcomm <name> <message>'
    else:
        try:
            if cmd_JSON[alias]:
                return f'Command "{alias}" already exists.'
        except:
            pass

        newComm_dict = {'cooldown': 60, 'return': ' '.join(msg)}
        cmd_JSON[str(alias).lower()] = newComm_dict

        with open(cmdFile, 'w+', encoding = 'utf-8') as f:
            f.write(json.dumps(cmd_JSON, indent=4, sort_keys=True))
            
        return f'Added command "{str(alias).lower()}" FeelsOkayMan 👍'


def delcomm(cmd_JSON, alias):
    """Delete a bot command by name."""
    if not alias:
        return 'Correct usage: !delcomm <name>'
    else:
        try:
            if cmd_JSON[alias]:
                cmd_JSON.pop(alias, None)
        except:
            return f'Command "{alias}" does not exist.'

        with open(cmdFile, 'w+', encoding = 'utf-8') as f:
            f.write(json.dumps(cmd_JSON, indent=4, sort_keys=True))
            
        return f'Deleted command "{alias}" madnakS 👎'


def editcomm(cmd_JSON, alias, new_msg):
    """Edit a bot command."""
    if not alias or not new_msg:
        return 'Correct usage: !editcomm <name> <new message>'
    else:
        try:
            if cmd_JSON[alias]:
                cmd_JSON[alias] = {'cooldown': 60, 'return': ' '.join(new_msg)}
        except:
            return f'Command "{alias}" does not exist.'

        with open(cmdFile, 'w+', encoding = 'utf-8') as f:
            f.write(json.dumps(cmd_JSON, indent=4, sort_keys=True))

        return f'Edited command "{alias}" FeelsOkayMan 👍'
