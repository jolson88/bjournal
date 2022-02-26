from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
	name: str
	date: date
	status: str

@dataclass
class CommandContext:
	originalInput: str
	command: str
	argumentString: str

def newTaskCommand(ctx: CommandContext):
	tasks.append(Task(ctx.argumentString, date.today(), "NotStarted"))

def quitCommand(_ctx: CommandContext):
	print("Thanks for using bjournal!")
	exit(0)

def parseInput(userInput: str) -> CommandContext:
	userInput = userInput + " " # Somewhat of a "hack" to make it easier to parse out command and arguments
	userCommand = userInput[userInput.find(" "):]
	return CommandContext(
		originalInput = userInput.strip(),
		command = userInput[:userInput.find(" ")],
		argumentString = userInput[userInput.find(" "):].strip()
	)

commands = {
	"n": newTaskCommand,
	"q": quitCommand,
	"quit": quitCommand,
}
tasks = []

def main():
	print("Welcome to bjournal, a programmer's bullet journal.")
	print("Today's date is", date.today().isoformat())
	
	while True:
		userInput = input("? ")
		if userInput.strip() == "":
			print("Please enter a command")
			continue

		commandContext = parseInput(userInput);
		command = commands.get(commandContext.command)
		if (command is not None):
			command(commandContext)
		else:
			print(f'Command "{commandContext.command}" is not recognized!')

if __name__ == "__main__":
	main()