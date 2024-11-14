import multiprocessing
import time

processes = []

def simulate_life(person):
  print(f"{person['name']} was born.")
  years_old = 0
  while years_old < person["will_die_at"]:
    time.sleep(1)
    years_old += 1
    print(f"{person['name']} is {years_old} years old.")
    if person.get("children", []) == []:
      continue
    if years_old in [son["will_born_at"] for son in person.get("children", [])]:
      print(f"{person['name']} had a son.")
      children = person.get("children", [])
      for son in children:
        if son["will_born_at"] == years_old:
          son_to_born = son
          processes.append(multiprocessing.Process(target=simulate_life, args=(son_to_born,)))
          processes[-1].start()

  print(f"{person['name']} died.")


def main():
  print("Start simulation.")
  grandson_1 = {"name": "Grandson 1", "will_die_at": 12, "will_born_at": 12}
  grandson_2 = {"name": "Grandson 2", "will_die_at": 18, "will_born_at": 14}
  son_1 = {"name": "Son 1", "will_die_at": 30, "will_born_at": 14, "children": [grandson_1]}
  son_2 = {"name": "Son 2", "will_die_at": 30, "will_born_at": 16, "children": [grandson_2]}
  father = {"name": "Father", "will_die_at": 60, "children": [son_1, son_2]}

  processes.append(multiprocessing.Process(target=simulate_life, args=(father,)))
  processes[-1].start()

  for process in processes:
    process.join()


if __name__ == "__main__":
  main()