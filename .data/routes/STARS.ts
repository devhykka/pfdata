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

	"MDPC": {
		"08": {
			"POKEG1W": [
				"POKEG", "VOGEP", "BEREL", "AGNAL"
			],
			"BETIR1W": [
				"BETIR", "ILOBI", "PIXES", "BEREL", "AGNAL"
			],
			"KATOK1W": [
				"KATOK", "LETAD", "BEREL", "AGNAL"
			],
			"ANTEX1W": [
				"ANTEX", "LETAD", "BEREL", "AGNAL"
			]
		},
		"09": {
			"POKEG1W": [
				"POKEG", "VOGEP", "BEREL", "AGNAL"
			],
			"BETIR1W": [
				"BETIR", "ILOBI", "PIXES", "BEREL", "AGNAL"
			],
			"KATOK1W": [
				"KATOK", "LETAD", "BEREL", "AGNAL"
			],
			"ANTEX1W": [
				"ANTEX", "LETAD", "BEREL", "AGNAL"
			]
		},
		"26": {
			"POKEG1C": [
				"POKEG", "VOGEP", "BEREL", "DASVO", "PC203", "LETAD", "VIRTO"
			],
			"BETIR1C": [
				"BETIR", "ILOBI", "PIXES", "BEREL", "DASVO", "PC203", "LETAD", "VIRTO"
			],
			"KATOK1C": [
				"KATOK", "LETAD", "VIRTO"
			],
			"ANTEX1C": [
				"ANTEX", "VIRTO"
			]
		},
		"27": {
			"POKEG1C": [
				"POKEG", "VOGEP", "BEREL", "DASVO", "PC203", "LETAD", "MESPA"
			],
			"BETIR1C": [
				"BETIR", "ILOBI", "PIXES", "BEREL", "DASVO", "PC203", "LETAD", "MESPA"
			],
			"KATOK1C": [
				"KATOK", "LETAD", "MESPA"
			],
			"ANTEX1C": [
				"ANTEX", "MESPA"
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
				"LUBES", "NORDI", "PEEKO"
			],
			"KURSA1R": [
				"KURSA", "GIPRO", "RIMEX"
			]
		},
		"22": {
			"BONEK1R": [
				"BONEK", "ADLAS", "AMAKO", "SOBOS", "ROKIK"
			],
			"NIMSI1R": [
				"NIMSI", "ESERI", "BETID", "BOSIS", "AMAKO", "SOBOS", "ROKIK"
			],
			"KRASI1V": [
				"KRASI", "MURAT", "ROKIK"
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
	},

	"PAFA": {
		"02L": {
			"Vectors": []
		},
		"02R": {
			"Vectors": []
		},
		"20R": {
			"Vectors": []
		},
		"20L": {
			"Vectors": []
		}
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
