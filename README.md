# PFData

Multiple sources of data for the Project Flight flight simulator on Roblox. 


Excluding the `callsigns.json` and the `waypoints.json` file, all files **NOT IN** the `.data` folder (and sub-folders) should NOT be edited. All pull requests targeting these files will be invalidated.

## Data Files Information
`.data/sectors/*` | Enroute Sectors only, format:
```json
{
  "name": "Developer Control", <-- This is the name of the sector.
  "topdown": ["EGKK", "EGLC", "EGFF", "PAFA", "MDPC", "MDST", "MTCA", "MDAB", "MDCR", "LCLK", "LCPH", "LCRA", "LPMA"], <-- These are the airports the sector covers top-down.
  "default": ["EGTT", "LCCC", "LPPC", "EURO", "KZAK", "EKDK", "EHAA", "EGPX", "EGGX"] <-- These are the sectors the position covers.*
}
```

*This data is used for the extend logic, please do not add aerodromes to this folder.*

`.data/stations/*` | All positions, format:
```json
[
  {
    "name": "Cardiff Radar",
    "callsign": "EGFF_APP",
    "frequency": 119.155,
    "facility": "Approach",
    "line1": "Cardiff Radar",
    "line2": "Pilot briefings at wiki.pfatc.net/pilots/briefings",
    "line3": "Submit feedback at feedback.pfatc.net",
    "line4": ""
  },
  {
    "name": "Cardiff Tower",
    "callsign": "EGFF_TWR",
    "frequency": 133.105,
    "facility": "Tower",
    "line1": "Cardiff Tower",
    "line2": "Pilot briefings at wiki.pfatc.net/pilots/briefings",
    "line3": "Submit feedback at feedback.pfatc.net",
    "line4": ""
  }
]
```

```json
[
  {
    "name": "London Control",
    "callsign": "EGTT_CTR",
    "frequency": 127.830,
    "facility": "Enroute",
    "line1": "London Control | CPDLC [INOP]",
    "line2": "Submit feedback at feedback.pfatc.net",
    "line3": "",
    "line4": ""
  },
  {
    "name": "London Control (West)",
    "callsign": "EGTT_W_CTR",
    "frequency": 126.080,
    "facility": "Enroute",
    "line1": "London Control | CPDLC [INOP]",
    "line2": "Submit feedback at feedback.pfatc.net",
    "line3": "",
    "line4": ""
  }
]
```
