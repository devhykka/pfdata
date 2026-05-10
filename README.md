# PFData

Multiple sources of data for the Project Flight flight simulator on Roblox. 


Excluding the `callsigns.json` and the `waypoints.json` file, all files **NOT IN** the `.data` folder (and sub-folders) should NOT be edited. All pull requests targeting these files will be invalidated.

## Format
The appropriate format for files can be found below.

`.data/sectors/{fir}/{sector}.json` - These are enroute sectors. No aerodrome sectors are to be added.
```json
{
  "name": "Developer Control", <-- This is the name of the sector.
  "topdown": ["EGKK", "EGLC", "EGFF", "PAFA", "MDPC", "MDST", "MTCA", "MDAB", "MDCR", "LCLK", "LCPH", "LCRA", "LPMA"], <-- These are the airports the sector covers top-down.
  "default": ["EGTT", "LCCC", "LPPC", "EURO", "KZAK", "EKDK", "EHAA", "EGPX", "EGGX"] <-- These are the sectors the position covers.*
}
```

* - To view all sectors, please refer to `sectors.svg` in the root directory.

---

`.data/stations/fir/{identifier}` - These are all stations available to connect as.
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

These formats are bound to change, please always refer to this file to confirm the formats before contributing to the project.