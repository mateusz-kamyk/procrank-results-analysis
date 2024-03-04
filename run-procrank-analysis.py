#!/usr/bin/env python3

#Requirements
#============
# -- Python 3.x
# -- matplotlib 3.7.1
#
#Installation
#============
# 1. sudo apt install python3
# 2. pip install matplotlib
# 
#Running the script
#==================
# ./run-procrank-analysis.py example-data.txt
#

import sys
import matplotlib.pyplot as plt

def main():
  procrank_no = 0
  pss_values = []
  uss_values = []

  print("No Pss Uss")

  with open(sys.argv[1], 'r') as f:
    for line in f:
      if "  PID" in line:
        procrank_no += 1

        pss_sum = 0
        uss_sum = 0

        for next_line in f:
          if "RAM:" in next_line:
            break
          if "WPE" in next_line:
            process_pss = int(next_line.split()[3].strip("K"))
            process_uss = int(next_line.split()[4].strip("K"))
            pss_sum += process_pss
            uss_sum += process_uss

        pss_values.append(pss_sum/1024.0)
        uss_values.append(uss_sum/1024.0)

        print(f"{procrank_no} {pss_sum/1024.0:.2f}M {uss_sum/1024.0:.2f}M")

  plt.plot(pss_values, label='Pss')
  plt.plot(uss_values, label='Uss')
  plt.xlabel('No')
  plt.ylabel('memory usage [MB]')
  plt.title('Procrank Pss and Uss of WPE processes')
  plt.legend()
  plt.ylim(ymin=0, ymax=500)
  plt.xlim(xmin=0)
  y_ticks = range(0, 500, 50)
  plt.yticks(y_ticks)
  x_ticks = range(0, procrank_no, 5)
  plt.xticks(x_ticks)
  plt.show()

if __name__ == "__main__":
  main()
