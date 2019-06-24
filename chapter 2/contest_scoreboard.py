from functools import total_ordering

@total_ordering
class Student:

  def __init__(self, sid):
    self.sid = sid
    self.problems = {}

  def add_problem(self, pid, time, L):
    if pid not in self.problems.keys():
      self.problems[pid] = {'C':[0], 'I':[0], 'R':[0], 'U':[0], 'E':[0]}

    if self.problems[pid][L][0] == 0:
      self.problems[pid][L][0] = time
    else:
      self.problems[pid][L] += [time]

  def get_num_problems(self):
    num_problems = 0
    for problem in self.problems.keys():
      if self.problems[problem]['C'][0] > 0:
        num_problems += 1
    return num_problems

  def calculate_penalty(self):
    penalty = 0
    for problem in self.problems.keys():
      sol_time = sorted(self.problems[problem]['C'])[0]
      penalty += sol_time
      for time in self.problems[problem]['I']:
        if time != 0 and time < sol_time:
          penalty += 20
    return penalty

  def __lt__(self, other):
    snumprob = self.get_num_problems()
    onumprob = other.get_num_problems()
    if snumprob < onumprob:
      return True
    elif snumprob == onumprob:
      spenalty = self.calculate_penalty()
      openalty = other.calculate_penalty()
      if spenalty > openalty:
        return True
      elif spenalty == openalty:
        return self.sid > other.sid
      else:
        return False
    else:
      return False

  def __str__(self):
    return "{} {} {}".format(self.sid, self.get_num_problems(), self.calculate_penalty())



def read_input():
  num_cases = int(input().strip())

  input()
  for i in range(num_cases):
    student_dict = {}
    try:
      while (True):
        line = input().strip()
        if not line: break
        tmp = line.split()
        tmp = [int(tmp[0]), int(tmp[1]), int(tmp[2]), tmp[3]]
        if tmp[0] not in student_dict.keys():
          student_dict[tmp[0]] = Student(tmp[0])
        student_dict[tmp[0]].add_problem(tmp[1], tmp[2], tmp[3])
    except EOFError: pass

    sorted_students = sorted(student_dict.values(), reverse=True)
    for student in sorted_students:
      print (student)

    if i<num_cases-1: print()



read_input()