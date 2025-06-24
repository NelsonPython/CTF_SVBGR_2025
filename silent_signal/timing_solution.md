### Open SilentSignal.pcap in Wireshark

Notice the only thing that changes is the time stamp.  Extract the ICMP packets:

```
Wireshark -> File -> Extract Packet Dissections -> As CSV
```

See [silentsignal.csv](silentsignal.csv)

### Decode the flag
See [compute_time_delta.py](compute_time_delta.py).  Compute the difference between the timestamps to get a list of numbers:

86
66
82
71
123
116
105
109
51
95
116
114
52
118
51
108
95
118
49
97
95
112
49
110
103
125

Each of those numbers corresponds to a character in the ASCII table.  Decode and prepend an "S" to reveal the flag:
SVBRG{tim3_tr4v3l_v1a_p1ng}



