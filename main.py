
def count_batteries_by_usage(cycles):
  low=0
  high=0
  mid=0
  for i in range (0,len(cycles)):
    if cycles[i]<410:
      low+=1
    elif cycles[i]>=410 and cycles[i]<=949:
      mid+=1
    else:
      high+=1
  return {
    "lowCount": low,
    "mediumCount": mid,
    "highCount": high
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
