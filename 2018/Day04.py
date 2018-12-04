# For example, consider the following records, which have already been organized into chronological order:
#
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up
# Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.
#
# Visually, these records show that the guards are asleep at these times:
#
# Date   ID   Minute
#             000000000011111111112222222222333333333344444444445555555555
#             012345678901234567890123456789012345678901234567890123456789
# 11-01  #10  .....####################.....#########################.....
# 11-02  #99  ........................................##########..........
# 11-03  #10  ........................#####...............................
# 11-04  #99  ....................................##########..............
# 11-05  #99  .............................................##########.....
# The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.
#
# Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.
#
# If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.
#
# Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
#
# In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).
#
# While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.
#
# What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

import utils
import re
from collections import defaultdict
from bisect import insort

PATTERN = re.compile(r'\[(?P<year>\d{4})-(?P<month>\d\d)-(?P<day>\d\d) (?P<hour>\d\d):(?P<minute>\d\d)] (Guard #(?P<id>\d+).+$|(?P<sleep>f).+$|(?P<wakeup>w).+$)')


def part_1():
  guard_intervals = process_input()

  max_total = 0
  max_guard = 0
  for guard, intervals in guard_intervals.items():
    total = sum(wake - sleep for sleep, wake in intervals)
    if total > max_total:
      max_total = total
      max_guard = guard

  chosen_minute, _ = find_minute_with_most_overlap(guard_intervals[max_guard])
  return max_guard * chosen_minute


def process_input():
  log = sorted(utils.get_input_lines(4))
  guard_intervals = defaultdict(list)

  current_guard = 0
  last_asleep = 0
  for entry in (re.match(PATTERN, e).groupdict() for e in log):
    if entry['id']:
      current_guard = int(entry['id'])
    elif entry['sleep']:
      last_asleep = int(entry['minute'])
    elif entry['wakeup']:
      guard_intervals[current_guard].append((last_asleep, int(entry['minute'])))

  return guard_intervals


def find_minute_with_most_overlap(intervals):
  def peek(x):
    return x[0] if x else 61

  open_interval_ends = []
  max_open = 0
  chosen_minute = 0
  for start, end in sorted(intervals):
    while start > peek(open_interval_ends):
      open_interval_ends.pop(0)
    insort(open_interval_ends, end)
    if len(open_interval_ends) > max_open:
      max_open = len(open_interval_ends)
      chosen_minute = start

  return chosen_minute, max_open


# --- Part Two ---
#
# Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?
#
# In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)
#
# What is the ID of the guard you chose multiplied by the minute you chose?

def part_2():
  guard_intervals = process_input()

  max_overlaps = 0
  chosen_guard = 0
  chosen_minute = 0
  for guard, intervals in guard_intervals.items():
    best_minute, n_overlaps = find_minute_with_most_overlap(intervals)
    if n_overlaps > max_overlaps:
      max_overlaps = n_overlaps
      chosen_guard = guard
      chosen_minute = best_minute

  return chosen_guard * chosen_minute
