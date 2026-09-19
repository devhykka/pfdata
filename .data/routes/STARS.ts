type TStars = {
	[airportCode: string]: {
		[runway: string]: {
			[starName: string]: string[]
		}
	}
}

export const STARS: TStars = {
	"EGKK": {
		"08L": {
			"KUNAV1G": [
				"KUNAV", "AMDUT", "KKE64", "TIMBA"
			],
			"VASUX1G": [
				"VASUX", "DISVO", "TELTU", "HOLLY"
			]
		},
		"08R": {
			"KUNAV1G": [
				"KUNAV", "AMDUT", "KKE64", "TIMBA"
			],
			"VASUX1G": [
				"VASUX", "DISVO", "TELTU", "HOLLY"
			]
		},
		"26L": {
			"KUNAV1G": [
				"KUNAV", "AMDUT", "KKE64", "TIMBA"
			],
			"VASUX1G": [
				"VASUX", "DISVO", "TELTU", "HOLLY"
			]
		},
		"26R": {
			"KUNAV1G": [
				"KUNAV", "AMDUT", "KKE64", "TIMBA"
			],
			"VASUX1G": [
				"VASUX", "DISVO", "TELTU", "HOLLY"
			]
		}
	},
	
	"PAFA": {
		"2L": {
			"LIBER5": [
				"CAWIN", "STARC", "GLOWS"
			],
			"HRDNG4": [
				"RDFLG", "HRDNG", "RNDRR", "KRIIS"
			]
		},
		"20R": {
			"LIBER5": [
				"CAWIN", "STARC", "MINRR"
			],
			"HRDNG4": [
				"RDFLG", "HRDNG", "RNDRR", "ROAAD"
			]
		
		}
	},

	"MDPC": {
		"08": {
			"POKEG1W": [
				"POKEG", "BEREL", "AGNAL"
			],
			"BETIR1W": [
				"BETIR", "AGNAL"
			],
			"KATOK1W": [
				"KATOK", "AGNAL"
			],
			"ANTEX1W": [
				"ANTEX", "PC101", "AGNAL"
			]
		},
		"09": {
			"POKEG2B": [
				"POKEG", "BEREL", "AGNAL"
			],
			"BETIR2B": [
				"BETIR", "AGNAL"
			],
			"KATOK2B": [
				"KATOK", "AGNAL"
			],
			"ANTEX2B": [
				"ANTEX", "PC101", "AGNAL"
			]
		},
		"26": {
			"POKEG1C": [
				"POKEG", "BEREL", "AGNAL", "PC101"
			],
			"BETIR1C": [
				"BETIR", "PC101"
			],
			"KATOK1C": [
				"KATOK", "PC101"
			],
			"ANTEX1C": [
				"ANTEX", "PC101"
			]
		},
		"27": {
			"POKEG2C": [
				"POKEG", "BEREL", "AGNAL", "PC101", "MAROG"
			],
			"BETIR2C": [
				"BETIR", "PC101", "MAROG"
			],
			"KATOK2C": [
				"KATOK", "MAROG"
			],
			"ANTEX2C": [
				"ANTEX", "MESPA", "PC103", "MAROG"
			]
		}
	},

	"MDST": {
		"11": {
			"Vectors": []
		},
		"29": {
			"Vectors": []
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
      "Vectors": []
    },
    "27": {
      "Vectors": []
    }
  },

  	"EGFF": {
		"12": {
			"BAJJA1C": [
				"BAJJA", "BCN", "CDF"
     		],
			"DAWLY1C": [
				"DAWLY", "IZLAW", "EXMOR", "CDF"
			],
			"ELREW1C": [
				"ELREW", "BCN", "CDF"
			],
			"TOJAQ2C": [
				"TOJAQ", "FARJO", "IZLAW", "EXMOR", "CDF"
			]
    },
		"30": {
			"BAJJA1C": [
				"BAJJA", "BCN", "CDF"
     		],
			"DAWLY1C": [
				"DAWLY", "IZLAW", "EXMOR", "CDF"
			],
			"ELREW1C": [
				"ELREW", "BCN", "CDF"
			],
			"TOJAQ2C": [
				"TOJAQ", "FARJO", "IZLAW", "EXMOR", "CDF"
			]
		}
	},

	"LCLK": {
		"04": {
			"LUBES1R": [
				"LUBES", "RIMEX"
			],
			"PHA1R": [
				"PHA", "KURSA", "GIPRO", "RIMEX"
			],
			"LUBES1A": [
				"LUBES", "LCA"
			],
			"PHA1C": [
				"PHA", "LCA"
			]
		},
		"22": {
			"BONEK1R": [
				"BONEK", "DAROS", "ADLAS", "OTESA", "LCA"
			],
			"LUBES1A": [
				"LUBES", "LCA"
			],
			"PHA1C": [
				"PHA", "LCA"
			]
		}
	},

	"LCPH": {
		"11": {
			"NORDI1T": [
                "NORDI", "PHA"
            ],
			"TOBAL1T": [
                "TOBAL", "PH940", "PHA"
            ],
			"GIPRO1A": [
                "GIPRO", "KURSA", "PHA"
            ]
            },
        "29": {
           "NORDI1T": [
                "NORDI", "PHA"
            ],
			"TOBAL1T": [
                "TOBAL", "PH940", "PHA"
            ],
			"GIPRO1A": [
                "GIPRO", "KURSA", "PHA"
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
			"RAKUN1P": [
				"RAKUN", "PILIM"
			],
			"EKNOT1P": [
				"EKNOT", "MA533", "PILIM"
			],
			"NIDUL1P": [
				"NIDUL", "MA542", "MA538", "PILIM"
			],
			"IBBAN1P": [
				"IBBAN", "MA538", "PILIM"
			],
			"KICAS1P": [
				"KICAS", "PILIM"
			]
		},
		"23": {
			"RAKUN1P": [
				"RAKUN", "PILIM"
			],
			"EKNOT1P": [
				"EKNOT", "MA533", "PILIM"
			],
			"NIDUL1P": [
				"NIDUL", "MA542", "MA538", "PILIM"
			],
			"IBBAN1P": [
				"IBBAN", "MA538", "PILIM"
			],
			"KICAS1P": [
				"KICAS", "PILIM"
			]
		},
	}
}

const uniqueStarNames = new Set<string>();

for (const airportCode in STARS) {
	if (Object.prototype.hasOwnProperty.call(STARS, airportCode)) {
		const airportStars = STARS[airportCode];

		for (const runway in airportStars) {
			if (Object.prototype.hasOwnProperty.call(airportStars, runway)) {
				const runwayStars = airportStars[runway];

				for (const starName in runwayStars) {
					if (Object.prototype.hasOwnProperty.call(runwayStars, starName)) {
						uniqueStarNames.add(starName);
					}
				}
			}
		}
	}
}

export const STARNAMES: string[] = Array.from(uniqueStarNames);
