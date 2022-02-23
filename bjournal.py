from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
	name: str
	date: date
	status: str

def main():
	print("Welcome to bjournal, a programmer's bullet journal.")
	print("Today's date is", date.today().isoformat())

	task = Task("My first task", date(2022, 2, 21), "Completed")
	print(task)

if __name__ == "__main__":
	main()