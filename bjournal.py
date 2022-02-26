from dataclasses import dataclass
from datetime import date
from typing import Callable

@dataclass
class Task:
	name: str
	date: date
	status: str

tasks: list[Task] = []

@dataclass
class CommandContext:
	original_input: str
	command: str
	argument_string: str

def list_tasks_cmd(_ctx: CommandContext) -> None:
	for task in tasks:
		print(f"- {task.name}")

def new_task_cmd(ctx: CommandContext) -> None:
	tasks.append(Task(ctx.argument_string, date.today(), "NotStarted"))

def quit_cmd(_ctx: CommandContext) -> None:
	print("\nThanks for using bjournal!")
	exit(0)

def parse_input(user_input: str) -> CommandContext:
	user_input = user_input + " " # Somewhat of a "hack" to make it consistent to parse out command and arguments
	user_command = user_input[user_input.find(" "):]
	return CommandContext(
		original_input = user_input.strip(),
		command = user_input[:user_input.find(" ")],
		argument_string = user_input[user_input.find(" "):].strip()
	)

commands: dict[str, Callable[[CommandContext], None]] = {
	"l": list_tasks_cmd,
	"n": new_task_cmd,
	"q": quit_cmd,
	"quit": quit_cmd,
}

def main():
	print("Welcome to bjournal, a programmer's bullet journal.")
	print("Today's date is", date.today().isoformat())
	
	while True:
		user_input = input("? ")
		if user_input.strip() == "":
			print("Please enter a command")
			continue

		command_ctx = parse_input(user_input);
		command = commands.get(command_ctx.command)
		if (command is not None):
			command(command_ctx)
		else:
			print(f'Command "{command_ctx.command}" is not recognized!')

if __name__ == "__main__":
	main()