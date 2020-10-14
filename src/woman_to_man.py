zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio',
                'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
Aries_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87'] #done
Taurus_to_all = ['72', '87', '73', '83', '88', '92', '92', '98', '81', '89', '83', '91'] #done
Gemini_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Cancer_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Leo_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Virgo_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Libra_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Scorpio_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Sagittarius_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Capricorn_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Aquarius_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']
Pisces_to_all = ['91', '81', '72', '81', '97', '84', '83', '76', '92', '82', '82', '87']

Aries = 'Aries '
Aries_list = Aries * 12
Aries_list = Aries_list.split()
Aries_list = list(zip(Aries_list, zodiac_signs, Aries_to_all))

Taurus = 'Taurus '
Taurus_list = Taurus * 12
Taurus_list = Taurus_list.split()
Taurus_list = list(zip(Taurus_list, zodiac_signs, Taurus_to_all))

Gemini = 'Gemini '
Gemini_list = Gemini * 12
Gemini_list = Gemini_list.split()
Gemini_list = list(zip(Gemini_list, zodiac_signs, Gemini_to_all))

Cancer = 'Cancer '
Cancer_list = Cancer * 12
Cancer_list = Cancer_list.split()
Cancer_list = list(zip(Cancer_list, zodiac_signs, Cancer_to_all))

Leo = 'Leo '
Leo_list = Leo * 12
Leo_list = Leo_list.split()
Leo_list = list(zip(Leo_list, zodiac_signs, Leo_to_all))

Virgo = 'Virgo '
Virgo_list = Virgo * 12
Virgo_list = Virgo_list.split()
Virgo_list = list(zip(Virgo_list, zodiac_signs, Virgo_to_all))

Libra = 'Libra '
Libra_list = Libra * 12
Libra_list = Libra_list.split()
Libra_list = list(zip(Libra_list, zodiac_signs, Libra_to_all))

Scorpio = 'Scorpio '
Scorpio_list = Scorpio * 12
Scorpio_list = Scorpio_list.split()
Scorpio_list = list(zip(Scorpio_list, zodiac_signs, Scorpio_to_all))

Sagittarius = 'Sagittarius '
Sagittarius_list = Sagittarius * 12
Sagittarius_list = Sagittarius_list.split()
Sagittarius_list = list(zip(Sagittarius_list, zodiac_signs, Sagittarius_to_all))

Capricorn = 'Capricorn '
Capricorn_list = Capricorn * 12
Capricorn_list = Capricorn_list.split()
Capricorn_list = list(zip(Capricorn_list, zodiac_signs, Capricorn_to_all))

Aquarius = 'Aquarius '
Aquarius_list = Aquarius * 12
Aquarius_list = Aquarius_list.split()
Aquarius_list = list(zip(Aquarius_list, zodiac_signs, Aquarius_to_all))

Pisces = 'Pisces '
Pisces_list = Pisces * 12
Pisces_list = Pisces_list.split()
Pisces_list = list(zip(Pisces_list, zodiac_signs, Pisces_to_all))

woman_list = Aries_list + Pisces_list + Aquarius_list + Capricorn_list + Sagittarius_list + Scorpio_list + Libra_list + \
    Virgo_list + Leo_list + Cancer_list + Gemini_list + Taurus_list
