
def get_dict_from_values(keys: list, values: list) -> dict:
    if len(keys) != len(values):
        print(f'not same length, {len(keys) = } /= {len(values) = }')
        return {}
    returning_dict:dict = {}
    for i, key in enumerate(keys):
        returning_dict[f'{key}'] = values[i]
    return returning_dict


strength_temps=[100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

db = {
    "dn": {
        "6": {
            "od": 10.3,
            "walls": [1.24, 1.73, 2.41]
        },
        "8": {
            "od": 13.7,
            "walls": [1.65, 2.24, 3.02]
        },
        "10": {
            "od": 17.1,
            "walls": [1.65, 2.31, 3.02]
        },
        "15": {
            "od": 21.3,
            "walls": [2.11, 2.77, 3.73]
        },
        "20": {
            "od": 26.7,
            "walls": [2.11, 2.87, 3.91]
        },
        "25": {
            "od": 33.4,
            "walls": [2.77, 3.38, 4.55]
        },
        "32": {
            "od": 42.2,
            "walls": [2.77, 3.56, 4.85]
        },
        "40": {
            "od": 48.3,
            "walls": [2.77, 3.68, 5.08]
        },
        "50": {
            "od": 60.3,
            "walls": [2.77, 3.91, 5.54]
        },
        "65": {
            "od": 73.0,
            "walls": [3.05, 5.16, 7.01]
        },
        "80": {
            "od": 88.9,
            "walls": [3.05, 5.49, 7.62]
        },
        "100": {
            "od": 116.3,
            "walls": [3.05, 6.02, 8.56]
        },
        "125": {
            "od": 141.3,
            "walls": [3.40, 6.55, 9.53]
        },
        "150": {
            "od": 168.3,
            "walls": [3.40, 7.11, 10.97]
        },
        "200": {
            "od": 219.1,
            "walls": [3.76, 8.18, 12.70]
        },
        "250": {
            "od": 273.1,
            "walls": [4.19, 9.27, 12.70]
        },
        "300": {
            "od": 323.9,
            "walls": [4.57, 9.53, 12.70]
        },
        "350": {
            "od": 355.6,
            "walls": [4.78, 9.53, 12.70]
        },
        "400": {
            "od": 406.4,
            "walls": [4.78, 9.53, 12.70]
        },
        "450": {
            "od": 457.2,
            "walls": [4.78, 9.53, 12.70]
        },
        "500": {
            "od": 508.0,
            "walls": [5.54, 9.53, 12.70]
        },
    },
    "walls": [1.6, 1.8, 2.0, 2.3, 2.6, 2.9, 3.2, 3.6, 4.0, 4.5, 5.0, 5.6, 6.3, 7.1, 8.0, 8.8, 10, 11, 12.5, 14.2, 16, 17.5, 20, 22.2, 25, 28, 30, 32, 36, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100],
    "joint_coefficient": {
        "1.0 Seamless / destructive and non-destructive testing": 1.0,
        "0.85 Random non-destructive testing": 0.85,
        "0.7 NOT non-destructive testing": 0.7,
    },
    "creep_durations": {
        "10_000 H": "creep_10k",
        "100_000 H": "creep_100k",
        "200_000 H": "creep_200k",
    },
    "materials": {
        "P195GH 1.0348": {
            "tensile_strength_Rm": 320,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[175, 165, 150, 130, 113, 102, 94, 0, 0, 0, 0]
            ),
        },
        "P235GH 1.0345": {
            "tensile_strength_Rm": 360,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[198, 187, 170, 150, 132, 120, 112, 108, 0, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500],
                "creep_10k": [182, 166, 151, 138, 125, 112, 100, 88, 77, 67, 58],
                "creep_100k": [141, 128, 114, 100, 88, 77, 66, 56, 47, 39, 32],
                "creep_200k": [128, 115, 102, 89, 77, 66, 56, 46, 33, 26, 24],
            },
        },
        "P265GH 1.0425": {
            "tensile_strength_Rm": 410,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[226, 213, 192, 171, 154, 141, 134, 128, 0, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500],
                "creep_10k": [182, 166, 151, 138, 125, 112, 100, 88, 77, 67, 58],
                "creep_100k": [141, 128, 114, 100, 88, 77, 66, 56, 47, 39, 32],
                "creep_200k": [128, 115, 102, 89, 77, 66, 56, 46, 33, 26, 24],
            },
        },
        "20MnNb6 1.0471": {
            "tensile_strength_Rm": 500,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[312, 292, 265, 241, 219, 200, 186, 174, 0, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500],
                "creep_10k": [243, 221, 200, 180, 161, 143, 126, 110, 96, 84, 74],
                "creep_100k": [179, 157, 136, 117, 100, 85, 73, 63, 55, 47, 41],
                "creep_200k": [157, 135, 115, 97, 82, 70, 60, 52, 44, 37, 0],
            },
        },
        "16Mo3 1.5415": {
            "tensile_strength_Rm": 450,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[243, 237, 224, 205, 173, 159, 156, 150, 146, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550],
                "creep_10k": [298, 273, 247, 221, 196, 171, 148, 125, 104, 84, 64],
                "creep_100k": [236, 205, 176, 149, 124, 102, 83, 65, 51, 40, 32],
                "creep_200k": [218, 188, 158, 129, 105, 84, 67, 53, 42, 34, 25],
            },
        },
        "8MoB5-4 1.5450": {
            "tensile_strength_Rm": 540,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[368, 368, 368, 368, 368, 368, 368, 0, 0, 0, 0]
            ),
        },
        "14MoV6-3 1.7715": {
            "tensile_strength_Rm": 460,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[282, 276, 268, 241, 225, 216, 209, 203, 200, 197, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [337, 349, 324, 298, 274, 249, 225, 203, 181, 162, 143, 126, 112, 97, 85, 74],
                "creep_100k": [305, 276, 249, 224, 200, 177, 155, 135, 117, 102, 87, 75, 65, 58, 48, 41],
                "creep_200k": [282, 255, 226, 202, 179, 158, 136, 117, 101, 86, 74, 63, 54, 47, 40, 34],
            },
        },
        "10CrMo5-5 1.7338": {
            "tensile_strength_Rm": 410,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[240, 228, 219, 208, 165, 156, 148, 144, 143, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [377, 347, 319, 292, 264, 238, 209, 181, 155, 131, 109, 90, 74, 60, 50, 41],
                "creep_100k": [290, 258, 227, 198, 170, 145, 121, 100, 80, 65, 53, 44, 38, 31, 26, 20],
                "creep_200k": [264, 233, 203, 175, 148, 123, 103, 82, 66, 51, 41, 35, 30, 25, 0, 0],
            },
        },
        "13CrMo4-5 1.7335": {
            "tensile_strength_Rm": 440,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[264, 253, 245, 236, 192, 182, 174, 168, 166, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [377, 347, 319, 292, 264, 238, 209, 181, 155, 131, 109, 90, 74, 60, 50, 41],
                "creep_100k": [290, 258, 227, 198, 170, 145, 121, 100, 80, 65, 53, 44, 38, 31, 26, 20],
                "creep_200k": [264, 233, 203, 175, 148, 123, 103, 82, 66, 51, 41, 35, 30, 25, 0, 0],
            },
        },
        "10CrMo9-10 1.7380": {
            "tensile_strength_Rm": 480,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[249, 241, 234, 224, 219, 212, 207, 193, 180, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [308, 284, 261, 238, 216, 195, 176, 158, 142, 126, 111, 99, 88, 78, 69, 60],
                "creep_100k": [229, 212, 194, 177, 160, 141, 124, 105, 95, 81, 70, 61, 53, 46, 40, 35],
                "creep_200k": [204, 188, 172, 156, 140, 124, 108, 94, 80, 68, 57, 49, 43, 38, 33, 28],
            },
        },
        "11CrMo9-10 1.7383": {
            "tensile_strength_Rm": 540,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[323, 312, 304, 396, 389, 380, 275, 257, 239, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520],
                "creep_10k": [382, 355, 333, 312, 294, 276, 259, 242, 225, 208, 191, 174, 157],
                "creep_100k": [313, 289, 272, 255, 238, 221, 204, 187, 170, 153, 137, 122, 107],
                "creep_200k": [],
            },
        },
        "25CrMo4 1.7218": {
            "tensile_strength_Rm": 540,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[315, 315, 305, 295, 285, 265, 225, 185, 0, 0, 0]
            ),
        },
        "20CrMoV13-5-5 1.7779": {
            "tensile_strength_Rm": 740,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[575, 575, 570, 560, 550, 510, 470, 420, 370, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550],
                "creep_10k": [470, 440, 410, 360, 310, 270, 240, 210, 186, 169, 152, 134, 117, 98],
                "creep_100k": [420, 370, 310, 260, 220, 190, 165, 145, 127, 114, 101, 87, 74, 59],
                "creep_200k": [],
            },
        },
        "15NiCuMoNb5-6-4 1.6368": {
            "tensile_strength_Rm": 610,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[422, 412, 402, 392, 382, 373, 343, 304, 0, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500],
                "creep_10k": [402, 385, 368, 348, 328, 304, 274, 242, 212, 179, 147],
                "creep_100k": [373, 349, 325, 300, 273, 245, 210, 175, 139, 104, 69],
                "creep_200k": [],
            },
        },
        "7CrWVMoNb9-6 1.8201": {
            "tensile_strength_Rm": 510,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[379, 370, 363, 361, 359, 351, 345, 338, 330, 299, 266]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570],
                "creep_10k": [275, 260, 246, 232, 219, 206, 194, 182, 170, 159, 148, 137, 125],
                "creep_100k": [233, 219, 206, 193, 181, 169, 157, 145, 134, 122, 110, 97, 79],
                "creep_200k": [],
            },
        },
        "7CrMoVTiB10-10 1.7378": {
            "tensile_strength_Rm": 565,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[397, 383, 373, 366, 359, 352, 345, 336, 324, 301, 248]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [278, 262, 247, 231, 214, 198, 171, 165, 148, 130, 113, 0, 0, 0, 0, 0],
                "creep_100k": [378, 342, 311, 281, 257, 240, 222, 205, 187, 170, 152, 134, 117, 99, 82, 64],
                "creep_200k": [],
            },
        },
        "X11CrMo5+I 1.7362+I": {
            "tensile_strength_Rm": 430,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[156, 150, 148, 147, 145, 142, 137, 129, 116, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630],
                "creep_10k": [196, 180, 166, 152, 140, 128, 116, 105, 95, 85, 77, 69, 63, 58, 50, 45, 41, 37, 33],
                "creep_100k": [147, 133, 119, 108, 98, 89, 79, 69, 62, 55, 49, 44, 38, 34, 30, 26, 24, 0, 0],
                "creep_200k": [130, 118, 107, 96, 86, 76, 67, 58, 52, 46, 41, 36, 31, 27, 24, 22, 0, 0, 0],
            },
        },
        "X11CrMo5+NT1 1.7362+NT1": {
            "tensile_strength_Rm": 480,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[245, 237, 230, 223, 216, 206, 196, 181, 167, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [242, 242, 242, 215, 188, 164, 145, 128, 113, 100, 88, 78, 69, 60, 53, 46],
                "creep_100k": [270, 255, 188, 157, 131, 113, 96, 82, 70, 60, 50, 0, 0, 0, 0, 0],
                "creep_200k": [237, 202, 170, 141, 116, 96, 80, 68, 58, 48, 40, 0, 0, 0, 0, 0],
            },
        },
        "X11CrMo5+NT2 1.7362+NT2": {
            "tensile_strength_Rm": 570,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[366, 350, 334, 332, 309, 299, 289, 280, 265, 0, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [242, 242, 242, 215, 188, 164, 145, 128, 113, 100, 88, 78, 69, 60, 53, 46],
                "creep_100k": [270, 255, 188, 157, 131, 113, 96, 82, 70, 60, 50, 0, 0, 0, 0, 0],
                "creep_200k": [237, 202, 170, 141, 116, 96, 80, 68, 58, 48, 40, 0, 0, 0, 0, 0],
            },
        },
        "X11CrMo9-1+I 1.7386+I": {
            "tensile_strength_Rm": 460,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[187, 186, 178, 177, 175, 171, 164, 153, 142, 120, 0]
            ),
            "creep_strength": {
                "creep_temps": [460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600],
                "creep_10k": [275, 240, 210, 190, 170, 152, 134, 118, 104, 90, 78, 68, 60, 53, 48],
                "creep_100k": [190, 170, 150, 130, 115, 102, 89, 78, 67, 58, 49, 42, 37, 33, 30],
                "creep_200k": [],
            },
        },
        "X11CrMo9-1+NT 1.7386+NT": {
            "tensile_strength_Rm": 590,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[363, 348, 334, 330, 326, 322, 316, 311, 290, 235, 0]
            ),
            "creep_strength": {
                "creep_temps": [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650],
                "creep_10k": [335, 308, 284, 261, 239, 219, 200, 182, 164, 148, 132, 117, 102, 89, 77, 65, 55, 47, 40, 34, 30],
                "creep_100k": [276, 253, 231, 211, 192, 174, 156, 139, 123, 107, 92, 78, 66, 55, 45, 37, 31, 27, 24, 21, 0],
                "creep_200k": [259, 236, 215, 196, 177, 160, 142, 126, 111, 95, 80, 67, 55, 45, 37, 32, 27, 24, 0, 0, 0],
            },
        },
        "X10CrMoVNb9-1 1.4903": {
            "tensile_strength_Rm": 630,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[410, 395, 380, 370, 360, 350, 340, 320, 300, 270, 215]
            ),
            "creep_strength": {
                "creep_temps": [500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670],
                "creep_10k": [289, 270, 251, 234, 216, 200, 183, 167, 152, 137, 122, 109, 97, 86, 76, 68, 61, 54],
                "creep_100k": [255, 236, 217, 199, 182, 164, 148, 132, 117, 103, 90, 79, 70, 62, 55, 48, 42, 36],
                "creep_200k": [245, 225, 206, 188, 170, 153, 136, 121, 106, 93, 81, 71, 63, 56, 49, 43, 36, 0],
            },
        },
        "X10CrWMoVNb9-2 1.4901": {
            "tensile_strength_Rm": 620,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[420, 412, 405, 400, 392, 382, 372, 360, 340, 300, 248]
            ),
            "creep_strength": {
                "creep_temps": [520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650],
                "creep_10k": [272, 256, 240, 225, 210, 195, 181, 167, 153, 139, 126, 113, 100, 88],
                "creep_100k": [235, 218, 202, 187, 172, 157, 142, 127, 113, 100, 87, 75, 65, 56],
                "creep_200k": [129, 115, 101, 88, 76, 65, 56, 48, 0, 0, 0, 0, 0, 0],
            },
        },
        "X11CrWMoVNb9-1-1 1.4905": {
            "tensile_strength_Rm": 620,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[412, 401, 390, 383, 376, 367, 356, 342, 319, 287, 231]
            ),
            "creep_strength": {
                "creep_temps": [520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650],
                "creep_10k": [252, 237, 222, 208, 194, 180, 166, 152, 139, 125, 111, 99, 88, 78],
                "creep_100k": [220, 204, 188, 173, 157, 142, 126, 111, 98, 85, 75, 65, 56, 0],
                "creep_200k": [113, 98, 86, 75, 65, 56, 0, 0, 0, 0, 0, 0, 0, 0],
            },
        },
        "X20CrMoV11-1 1.4922": {
            "tensile_strength_Rm": 690,
            "strenght_at_temp": get_dict_from_values(
                keys=strength_temps,
                values=[430, 430, 430, 415, 390, 380 ,360, 330, 290, 250, 0]
            ),
            "creep_strength": {
                "creep_temps": [480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650],
                "creep_10k": [348, 319, 292, 269, 27, 225, 205, 184, 165, 147, 130, 113, 97, 84, 72, 61, 52, 44],
                "creep_100k": [289, 263, 236, 212, 188, 167, 147, 128, 111, 95, 81, 69, 59, 51, 43, 36, 31, 26],
                "creep_200k": [270, 242, 218, 194, 170, 149, 129, 112, 96, 81, 68, 58, 49, 42, 36, 30, 0, 0],
            },
        }
    }
}
