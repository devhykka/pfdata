type TSids = {
	[airportCode: string]: {
		[runway: string]: {
			[sidNamw: string]: string[]
		}
	}
}

export const SIDS: TSids = {
	"MDPC": {
		"09": {
			"KATOK2T": [
				"MAROG", "KATOK"
			],
			"CHUMA2T": [
				"MAROG", "PC101","CHUMA"
			],
			"PIXAR2T": [
				"MAROG", "PC101", "PIXAR"
			],
			"ETBOD2T": [
				"MAROG", "PC103", "PC106", "MIBNI", "ETBOD"
			]
		},
		"27": {
			"KATOK3T": [
				"PC198", "PC202", "KATOK"
			],
			"CHUMA3T": [
				"PC198", "PC202", "CHUMA"
			],
			"PIXAR3T": [
				"PC198", "PC202", "PIXAR"
			],
			"ETBOD3T": [
				"PC198", "MIBNI", "ETBOD"
			]
		},
		"08": {
			"KATOK2T": [
				"TEXOS", "KATOK"
			],
			"CHUMA2T": [
				"TEXOS", "PC101", "CHUMA"
			],
			"PIXAR2T": [
				"TEXOS", "PC101", "PIXAR"
			],
			"ETBOD2T": [
				"TEXOS", "PC103", "PC106", "MIBNI", "ETBOD"
			]
		},
		"26": {
			"KATOK3T": [
				"PC200", "PC202", "KATOK"
			],
			"CHUMA3T": [
				"PC200", "PC202", "CHUMA"
			],
			"PIXAR3T": [
				"PC200", "PC202", "PIXAR"
			],
			"ETBOD3T": [
				"PC200", "MIBNI", "ETBOD"
			]
		}
	},

	"MDST": {
		"11": {
			"KODIX2U": [
                "ST530", "KODIX"
            ],
            "LERED2U": [
                "ST530", "ST551", "LERED"
            ],
             "MALVN2U":[
                "ST530", "ST551", "MALVN"
            ]
            
		    },
		"29": {
			"LERED2V": [
                "ST548", "LERED"
            
            ],
            "MALVN2V": [
                "ST548", "ST571", "MALVN"
            ]
		}
	},

	"MDAB": {
		"11": {
			"Vectors": []
		},
		"29": {
			"Vectors": []
		}
	},

	"MTCA": {
		"08": {
			"Vectors": []
		},
		"26": {
			"Vectors": []
		}
	},

	"MDCR": {
		"12": {
			"Vectors": []
		},
		"30": {
			"Vectors": []
		}
	},

	"EGKK": {
		"08R": {
            "IMVUR1Z": [ 
                 "KKN09", "KKW19" , "IMVUR" 
            ],
            "ODVIK2Z": [ 
                 "KKE04", "ODVIK"
            ],
			"SFD4Z": [
				"KKE05", "SFD"
			],
			"LAM1Z": [
				"KKE05", "KKN09", "LAM"
			]
		},
		"26L": {
			"BOGNA1X": [
				"KKW08", "KKS25", "BOGNA"
			],
			"NOVMA1X": [
				"KKW09", "MID", "NOVMA"
			],
			"WIZAD1X": [
				"KKW08", "KKS13", "KKS14", "MAY", "WIZAD"
			],
			"SFD1X": [
				"KKW08", "KKS13", "SFD"
			],
			"LAM6M": [
				"LAM"
			]
		}
	},

	"EGHI": {
		"02": {
			"Vectors": []
		},
		"20": {
			"Vectors": []
		}
  },

  "EGLC": {
		"09": {
			"BPK1H": [
				"LCE01", "LCN03", "BPK"
      ],
			"ODUKU1H": [
				"LCE01", "LCE02", "ODUKU"
			]
    },
		"27": {
			"BPK1A": [
				"LCW01", "LCN02", "BPK"
      ],
      "ODUKU1A": [
				"LCW01", "LCN03", "LCE04", "ODUKU"
			]
		}
	},

	"EGFF": {
		"12": {
			"LEKC1B": [
				"LEKCI"
      ],
			"BCN1B": [
				"BCN"
			],
			"EXMO1B": [
				"EXMOR"
			]
    },
		"30": {
			"BCN1A": [
				"BCN"
			],
			"EXMO1A": [
				"EXMOR"
			]
		}
	},

	"LCLK": {
		"04": {
			"BONEK2W": [
				"LK400", "OTESA", "ADLAS", "DAROS", "BONEK"
			],
			"NORDI1W": [
				"LK400", "OTESA", "ADLAS", "NORDI"
			],
			"RUDER1W": [
				"LK400", "SOBOS", "RUDER"
			],
			"EMEDA1W": [
				"LK400", "REXAL", "EMEDA"
			]
		},
		"22": {
			"LUBES1W": [
				"LK601", "RIMEX", "LUBES"
			],
			"KURSA1W": [
				"LK601", "RIMEX", "GIPRO", "KURSA"
			],
			"RUDER1D": [
				"LK601", "BOSIS", "KOBER", "RUDER"
			],
			"EMEDA1D": [
				"LK601", "BOSIS", "EMEDA"
			]
		}
	},

	"LCPH": {
		"11": {
			"ESERI1R": [
                "PH901", "ESERI"
            ],
            "GENOS1R": [
                "PH901", "NIMSI", "GENOS"
            ],
            "RIMEX1R": [
                "PH901", "PH950", "GIPRO", "RIMEX"
            ]

            },
        "29": {
           "ESERI1W":  [
                "PH965", "ESERI"
            ],
            "GENOS1W": [
                "PH965", "NIMSI", "GENOS"
            ],
             "NORDI1W":[
                "PH965", "NORDI"
            ],
            "RIMEX1W": [
                "PH965", "PH950", "GIPRO", "RIMEX"
            ]
		}
	},

	"LCRA": {
		"10": {
			"Vectors": []
		},
		"28": {
			"Vectors": []
		}
	},

	"LPMA": {
		"05": {
			"LAPPA1E": [
				"MA647", "PS702", "LAPPA"
			],
			"DEGUN1E": [
				"MA647", "DEGUN"
			],
			"GOSGA1E": [
				"GOSGA"
			],
			"GALOZ1E": [
				"MA401", "MA402", "MA403", "GALOZ"
			],
			"NIDUL1E": [
				"MA401", "MA402", "NIDUL"
			]
		},
		"23": {
			"LAPPA1W": [
				"MA647", "PS702", "LAPPA"
			],
			"DEGUN1W": [
				"MA647", "DEGUN"
			],
			"GOSGA1W": [
				"GOSGA"
			],
			"GALOZ1W": [
				"MA401", "MA402", "MA403", "GALOZ"
			],
			"NIDUL1W": [
				"MA401", "MA402", "NIDUL"
			]
		},
	},

	"PAFA": {
		"02L": {
			"GLEEN8": [
				"FAI", "ENN", "GAL"
			],
			"MKNLY4": [
				"FAI", "PUYVO", "TKA"
			],
			"PUYVO5": [
				"PUYVO"
			],
			"RDFLG5": [
				"SHMMR", "RDFLG"
			]
		},
		"02R": {
			"GLEEN8": [
				"FAI", "ENN", "GAL"
			],
			"MKNLY4": [
				"FAI", "PUYVO", "TKA"
			]
		},
		"20R": {
			"GLEEN8": [
				"ENN", "GAL"
			],
			"MKNLY4": [
				"PUYVO", "TKA"
			],
			"PUYVO5": [
				"PUYVO"
			],
			"RDFLG5": [
				"SHMMR", "RDFLG"
			]
		},
		"20L": {
			"GLEEN8": [
				"ENN", "GAL"
			],
			"MKNLY4": [
				"PUYVO", "TKA"
			]
		}
	}
};

const uniqueSidNames = new Set<string>();

for (const airportCode in SIDS) {
	if (Object.prototype.hasOwnProperty.call(SIDS, airportCode)) {
		const airportSids = SIDS[airportCode];

		for (const runway in airportSids) {
			if (Object.prototype.hasOwnProperty.call(airportSids, runway)) {
				const runwaySids = airportSids[runway];

				for (const sidName in runwaySids) {
					if (Object.prototype.hasOwnProperty.call(runwaySids, sidName)) {
						uniqueSidNames.add(sidName);
					}
				}
			}
		}
	}
}

export const SIDNAMES: string[] = Array.from(uniqueSidNames);
