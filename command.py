def command(commands):
    return commands.replace('()','o').replace('(al)','al')

print(command("G()(al)"))