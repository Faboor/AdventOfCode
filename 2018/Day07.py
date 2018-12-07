# Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.
# Visually, these requirements look like this:
#
#
#   -->A--->B--
#  /    \      \
# C      -->D----->E
#  \           /
#   ---->F-----
# Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:
#
# Only C is available, and so it is done first.
# Next, both A and F are available. A is first alphabetically, so it is done next.
# Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
# After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
# F is the only choice, so it is done next.
# Finally, E is completed.
# So, in this example, the correct order is CABDFE.
#
# In what order should the steps in your instructions be completed?

from collections import defaultdict
import heapq
import re
import utils

PATTERN = re.compile(r'Step (?P<pred>.) must be finished before step (?P<succ>.) can begin.')


def part_1():
  requirements_for, required_by, available = process_input()

  work_order = []
  while available:
    pred = heapq.heappop(available)
    work_order.append(pred)
    for succ in required_by[pred]:
      requirements_for[succ].remove(pred)
      if not requirements_for[succ]:
        heapq.heappush(available, succ)

  return ''.join(work_order)


def process_input():
  requirements_for = defaultdict(set)
  required_by = defaultdict(set)
  available = set()
  for pred, succ in (re.match(PATTERN, line).groups() for line in utils.get_input_lines(7)):
    if pred not in requirements_for:
      available.add(pred)
    available.difference_update([succ])
    requirements_for[succ].add(pred)
    required_by[pred].add(succ)
  available = list(available)
  heapq.heapify(available)

  return requirements_for, required_by, available


print(part_1())

# --- Part Two ---
#
# As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.
#
# Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.
#
# To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:
#
# Second   Worker 1   Worker 2   Done
#    0        C          .
#    1        C          .
#    2        C          .
#    3        A          F       C
#    4        B          F       CA
#    5        B          F       CA
#    6        D          F       CAB
#    7        D          F       CAB
#    8        D          F       CAB
#    9        D          .       CABF
#   10        E          .       CABFD
#   11        E          .       CABFD
#   12        E          .       CABFD
#   13        E          .       CABFD
#   14        E          .       CABFD
#   15        .          .       CABFDE
# Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.
#
# Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.
#
# In this example, it would take 15 seconds for two workers to complete these steps.
#
# With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?


def part_2():
  requirements_for, required_by, available = process_input()

  idle_workers = 5
  working = []
  current_time = 0
  while working or available:
    while available and idle_workers:
      to_do = heapq.heappop(available)
      heapq.heappush(working, (current_time + work_duration(to_do), to_do))
      idle_workers -= 1
    if working:
      current_time, done = heapq.heappop(working)
      idle_workers += 1
      for succ in required_by[done]:
        requirements_for[succ].remove(done)
        if not requirements_for[succ]:
          heapq.heappush(available, succ)
  return current_time


def work_duration(a):
  return ord(a) - 4


print(part_2())
