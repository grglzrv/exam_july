m_hrana = float(input())
m_suveniri = float(input())
m_hotel = float(input())

l_benzin_needed = (420 / 100) * 7
benzin_lv = l_benzin_needed * 1.85
tri_dena_prestoi = (3 * m_hrana) + (3 * m_suveniri)
hotel_den1 = m_hotel * 0.9
hotel_den2 = m_hotel * 0.85
hotel_den3 = m_hotel * 0.80
total_sum = benzin_lv + tri_dena_prestoi + hotel_den1 + hotel_den2 + hotel_den3

print(f'Money needed: {total_sum:.2f}')
