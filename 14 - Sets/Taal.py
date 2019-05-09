# def behoort_tot_taal(tekst, taal):
#     st = set(tekst)
#     st.discard(' ')
#     return st.issubset(taal) and len(st) > 0
#
# def is_onleesbaar(tekst, taal):
#     st = set(tekst)
#     st.discard(' ')
#     return len(st.intersection(taal)) == 0
#
# def perfect_woord(tekst, taal):
#     st = set(tekst)
#     st.discard(' ')
#     return taal.issubset(tekst)







def behoort_tot_taal(woord, taal):
    st = set(woord)
    st.discard(' ')
    return st.issubset(taal)

def is_onleesbaar(woord, taal):
    st = set(woord)
    st.discard(' ')
    return st.intersection(taal) == set()

def perfect_woord(woord, taal):
    st = set(woord)
    st.discard(' ')
    return taal.issubset(st)














print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(perfect_woord('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))