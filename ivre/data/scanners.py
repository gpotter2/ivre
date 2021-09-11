#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of IVRE.
# Copyright 2011 - 2020 Pierre LALET <pierre@droids-corp.org>
#
# IVRE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IVRE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IVRE. If not, see <http://www.gnu.org/licenses/>.

"""This sub-module contains data used to identify network scanners.

"""

# pylint: disable=line-too-long


JA3_CLIENT_VALUES = {
    # Masscan has three values because it will send its static client
    # hello message three times if it does not get an answer (which is
    # weird).
    "18e9afaf91db6f8a2470e7435c2a1d6b": ("Masscan", None),
    "2351bc927776c12aff03dcf9f1c12270": ("Masscan", None),
    "5f8552974406f5edd94290c87c3f9f24": ("Masscan", None),
    "8951236eca85955755e4946572ef32bb": ("Censys", "DTLS"),
}


USER_AGENT_VALUES = {
    "Mozilla/5.0 (compatible; Nmap Scripting Engine; "
    "https://nmap.org/book/nse.html)": ("Nmap", None),
    "Mozilla/5.0 zgrab/0.x": ("Zgrab", None),
    "masscan/1.0 (https://github.com/robertdavidgraham/masscan)": ("Masscan", None),
    "HTTP Banner Detection (https://security.ipip.net)": ("ipip.net", None),
    "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/": (
        "Censys",
        None,
    ),
}


UDP_PAYLOAD_PROBES = {
    b"\x16\xfe\xfd\x00\x00\x00\x00\x00\x00\x00\x00\x00~\x01\x00\x00r\x00\x00\x00\x00\x00\x00\x00r\xfe\xfd_\x06\x07BnS\xder\xd8\xef3~_\xeeY\x10\x19I\x8b-N\x7f\xde>\x09\xf4\xa8?\x03\xf9W\x06\x00\x00\x00\x0c\xc0\xac\xc0\xae\xc0+\xc0/\xc0\x0a\xc0\x14\x01\x00\x00<\x00\x0d\x00\x10\x00\x0e\x04\x03\x05\x03\x06\x03\x04\x01\x05\x01\x06\x01\x08\x07\x00\x0a\x00\x08\x00\x06\x00\x1d\x00\x17\x00\x18\x00\x0b\x00\x02\x01\x00\x00\x17\x00\x00\x00\x00\x00\x0e\x00\x0c\x00\x00\x09127.0.0.1": (  # noqa: E501
        "Censys",
        "DTLS",
    ),
    b"\x93\xd5\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03213\x011\x03168\x03192\x07in-addr\x04arpa\x00\x00\x0c\x00\x01": (
        "Censys",
        "DNS",
    ),  # DNS query IN PTR 213.1.168.192.in-addr.arpa.  # noqa: E501
    # https://nmap.org/book/osdetect-methods.html
    b"CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC": (
        "Nmap",
        "Fingerprint-U1"
    )
}


TCP_PAYLOAD_PROBES = {
    b"\x16\x03\x02\x01o\x01\x00\x01k\x03\x02RH\xc5\x1a#\xf7:N\xdf\xe2\xb4\x82/\xff\tT\x9f\xa7\xc4y\xb0h\xc6\x13\x8c\xa4\x1c=\"\xe1\x1a\x98 \x84\xb4,\x85\xafn\xe3Y\xbbbhl\xff(=':\xa9\x82\xd9o\xc8\xa2\xd7\x93\x98\xb4\xef\x80\xe5\xb9\x90\x00(\xc0\n\xc0\x14\x009\x00k\x005\x00=\xc0\x07\xc0\t\xc0#\xc0\x11\xc0\x13\xc0'\x003\x00g\x002\x00\x05\x00\x04\x00/\x00<\x00\n\x01\x00\x00\xfa\xef\x00\x00\x1a\x00\x18\x00\x00\x15syndication.twimg.com\xff\x01\x00\x01\x00\x00\n\x00\x08\x00\x06\x00\x17\x00\x18\x00\x19\x00\x0b\x00\x02\x01\x00\x00#\x00\xb0\x81\x01\x19g`\x1e\x04B\x9a\xf3\xe2<\x86XO\x87iD\xb0\x1d\x8e\x01\xfa\xa5\x87=]\xdc\x16L\xb4 \xda\xd3B\xb0\x88\xec\n\x13\xc3\xc6LDt}\xf5\x83\x93\xeb\x16`~G\x07\x15\xaeh?2\xfc(q\xdd\x8d*\xe0\x9e\x03\xad(\xd9\x89/\x0f\x07\xaf\xc1'\x8e\xf1W\xfb\xc6\xc4\xd4V:\xf6\xedYaJ\x17\x14\x0b\xd7|\xae\xfeU\xd9z\xa6\xf6\xc6W\xb5<\xedx\x9d\xee9\xd8g\x02\t\x92\xcb\xa5f\xa3H=\x06\xed\xa5\x02.\x9b\x16\xf6+\xe7?ye\x1a\xcbl\\\xbdk\xad\x11\xde\xbe\xdf5\xdb\x0b\xff,\x90\x942\xb5\x94W=^%\xd2\x1b\xd2D\x85\x961(i\xd7J\x13\n3t\x00\x00uO\x00\x00\x00\x05\x00\x05\x01\x00\x00\x00\x00": (  # noqa: E501
        "Masscan",
        "TLS",
    ),
    b"fox a 1 -1 fox hello\n{\nfox.version=s:1.0\nid=i:2\n};;\n": (
        "Nmap-modified",
        "niagara-fox-modified",
    ),
}

TCP_FLAGS_PROBES = {
    # Some scanners use extremely specific TCP flags/options on SYN.
    # https://docs.zeek.org/en/v4.0.0/scripts/base/init-bare.zeek.html#type-SYN_packet
    # https://nmap.org/book/osdetect-methods.html

    # Format: (DF, win_size, win_scale, MSS, SACK_OK, TSval, TSecr): ("Scanner name", "Probe name")
    (0, 4, 5, 640, 0, 0xFFFFFFFF, 0): ("Nmap", "Fingerprint-P3"),
    (1, 31337, 10, 265, 1, 0xFFFFFFFF, 0): ("Nmap", "Fingerprint-T5")
}

# ports that scanners scan by default
DEFAULT_SCANNED_PORTS = {
    "tcp": [
        (
            set((1, 3, 4, 6, 7, 9, 13, 17, 19, 20, 21, 22, 23, 24, 25, 26, 30, 32, 33, 37, 42, 43, 49, 53, 70, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 99, 100, 106, 109, 110, 111, 113, 119, 125, 135, 139, 143, 144, 146, 161, 163, 179, 199, 211, 212, 222, 254, 255, 256, 259, 264, 280, 301, 306, 311, 340, 366, 389, 406, 407, 416, 417, 425, 427, 443, 444, 445, 458, 464, 465, 481, 497, 500, 512, 513, 514, 515, 524, 541, 543, 544, 545, 548, 554, 555, 563, 587, 593, 616, 617, 625, 631, 636, 646, 648, 666, 667, 668, 683, 687, 691, 700, 705, 711, 714, 720, 722, 726, 749, 765, 777, 783, 787, 800, 801, 808, 843, 873, 880, 888, 898, 900, 901, 902, 903, 911, 912, 981, 987, 990, 992, 993, 995, 999, 1000, 1001, 1002, 1007, 1009, 1010, 1011, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1102, 1104, 1105, 1106, 1107, 1108, 1110, 1111, 1112, 1113, 1114, 1117, 1119, 1121, 1122, 1123, 1124, 1126, 1130, 1131, 1132, 1137, 1138, 1141, 1145, 1147, 1148, 1149, 1151, 1152, 1154, 1163, 1164, 1165, 1166, 1169, 1174, 1175, 1183, 1185, 1186, 1187, 1192, 1198, 1199, 1201, 1213, 1216, 1217, 1218, 1233, 1234, 1236, 1244, 1247, 1248, 1259, 1271, 1272, 1277, 1287, 1296, 1300, 1301, 1309, 1310, 1311, 1322, 1328, 1334, 1352, 1417, 1433, 1434, 1443, 1455, 1461, 1494, 1500, 1501, 1503, 1521, 1524, 1533, 1556, 1580, 1583, 1594, 1600, 1641, 1658, 1666, 1687, 1688, 1700, 1717, 1718, 1719, 1720, 1721, 1723, 1755, 1761, 1782, 1783, 1801, 1805, 1812, 1839, 1840, 1862, 1863, 1864, 1875, 1900, 1914, 1935, 1947, 1971, 1972, 1974, 1984, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2013, 2020, 2021, 2022, 2030, 2033, 2034, 2035, 2038, 2040, 2041, 2042, 2043, 2045, 2046, 2047, 2048, 2049, 2065, 2068, 2099, 2100, 2103, 2105, 2106, 2107, 2111, 2119, 2121, 2126, 2135, 2144, 2160, 2161, 2170, 2179, 2190, 2191, 2196, 2200, 2222, 2251, 2260, 2288, 2301, 2323, 2366, 2381, 2382, 2383, 2393, 2394, 2399, 2401, 2492, 2500, 2522, 2525, 2557, 2601, 2602, 2604, 2605, 2607, 2608, 2638, 2701, 2702, 2710, 2717, 2718, 2725, 2800, 2809, 2811, 2869, 2875, 2909, 2910, 2920, 2967, 2968, 2998, 3000, 3001, 3003, 3005, 3006, 3007, 3011, 3013, 3017, 3030, 3031, 3052, 3071, 3077, 3128, 3168, 3211, 3221, 3260, 3261, 3268, 3269, 3283, 3300, 3301, 3306, 3322, 3323, 3324, 3325, 3333, 3351, 3367, 3369, 3370, 3371, 3372, 3389, 3390, 3404, 3476, 3493, 3517, 3527, 3546, 3551, 3580, 3659, 3689, 3690, 3703, 3737, 3766, 3784, 3800, 3801, 3809, 3814, 3826, 3827, 3828, 3851, 3869, 3871, 3878, 3880, 3889, 3905, 3914, 3918, 3920, 3945, 3971, 3986, 3995, 3998, 4000, 4001, 4002, 4003, 4004, 4005, 4006, 4045, 4111, 4125, 4126, 4129, 4224, 4242, 4279, 4321, 4343, 4443, 4444, 4445, 4446, 4449, 4550, 4567, 4662, 4848, 4899, 4900, 4998, 5000, 5001, 5002, 5003, 5004, 5009, 5030, 5033, 5050, 5051, 5054, 5060, 5061, 5080, 5087, 5100, 5101, 5102, 5120, 5190, 5200, 5214, 5221, 5222, 5225, 5226, 5269, 5280, 5298, 5357, 5405, 5414, 5431, 5432, 5440, 5500, 5510, 5544, 5550, 5555, 5560, 5566, 5631, 5633, 5666, 5678, 5679, 5718, 5730, 5800, 5801, 5802, 5810, 5811, 5815, 5822, 5825, 5850, 5859, 5862, 5877, 5900, 5901, 5902, 5903, 5904, 5906, 5907, 5910, 5911, 5915, 5922, 5925, 5950, 5952, 5959, 5960, 5961, 5962, 5963, 5987, 5988, 5989, 5998, 5999, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6009, 6025, 6059, 6100, 6101, 6106, 6112, 6123, 6129, 6156, 6346, 6389, 6502, 6510, 6543, 6547, 6565, 6566, 6567, 6580, 6646, 6666, 6667, 6668, 6669, 6689, 6692, 6699, 6779, 6788, 6789, 6792, 6839, 6881, 6901, 6969, 7000, 7001, 7002, 7004, 7007, 7019, 7025, 7070, 7100, 7103, 7106, 7200, 7201, 7402, 7435, 7443, 7496, 7512, 7625, 7627, 7676, 7741, 7777, 7778, 7800, 7911, 7920, 7921, 7937, 7938, 7999, 8000, 8001, 8002, 8007, 8008, 8009, 8010, 8011, 8021, 8022, 8031, 8042, 8045, 8080, 8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089, 8090, 8093, 8099, 8100, 8180, 8181, 8192, 8193, 8194, 8200, 8222, 8254, 8290, 8291, 8292, 8300, 8333, 8383, 8400, 8402, 8443, 8500, 8600, 8649, 8651, 8652, 8654, 8701, 8800, 8873, 8888, 8899, 8994, 9000, 9001, 9002, 9003, 9009, 9010, 9011, 9040, 9050, 9071, 9080, 9081, 9090, 9091, 9099, 9100, 9101, 9102, 9103, 9110, 9111, 9200, 9207, 9220, 9290, 9415, 9418, 9485, 9500, 9502, 9503, 9535, 9575, 9593, 9594, 9595, 9618, 9666, 9876, 9877, 9878, 9898, 9900, 9917, 9929, 9943, 9944, 9968, 9998, 9999, 10000, 10001, 10002, 10003, 10004, 10009, 10010, 10012, 10024, 10025, 10082, 10180, 10215, 10243, 10566, 10616, 10617, 10621, 10626, 10628, 10629, 10778, 11110, 11111, 11967, 12000, 12174, 12265, 12345, 13456, 13722, 13782, 13783, 14000, 14238, 14441, 14442, 15000, 15002, 15003, 15004, 15660, 15742, 16000, 16001, 16012, 16016, 16018, 16080, 16113, 16992, 16993, 17877, 17988, 18040, 18101, 18988, 19101, 19283, 19315, 19350, 19780, 19801, 19842, 20000, 20005, 20031, 20221, 20222, 20828, 21571, 22939, 23502, 24444, 24800, 25734, 25735, 26214, 27000, 27352, 27353, 27355, 27356, 27715, 28201, 30000, 30718, 30951, 31038, 31337, 32768, 32769, 32770, 32771, 32772, 32773, 32774, 32775, 32776, 32777, 32778, 32779, 32780, 32781, 32782, 32783, 32784, 32785, 33354, 33899, 34571, 34572, 34573, 35500, 38292, 40193, 40911, 41511, 42510, 44176, 44442, 44443, 44501, 45100, 48080, 49152, 49153, 49154, 49155, 49156, 49157, 49158, 49159, 49160, 49161, 49163, 49165, 49167, 49175, 49176, 49400, 49999, 50000, 50001, 50002, 50003, 50006, 50300, 50389, 50500, 50636, 50800, 51103, 51493, 52673, 52822, 52848, 52869, 54045, 54328, 55055, 55056, 55555, 55600, 56737, 56738, 57294, 57797, 58080, 60020, 60443, 61532, 61900, 62078, 63331, 64623, 64680, 65000, 65129, 65389)),
            "Nmap"
        ),
    ]
}
