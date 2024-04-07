import streamlit as st

# Tytuł aplikacji
st.title('Konwerter jednostek')

# Rozszerzone opcje konwersji
conversion_type = st.selectbox('Wybierz rodzaj konwersji:',
                               ['Kilogramy na Funty', 'Kilometry na Mile', 'Stopnie Celsjusza na Stopnie Fahrenheita',
                                'Stopy na Metry', 'Cale na Centymetry'])

# Pole do wprowadzenia wartości przez użytkownika
value = st.number_input('Wprowadź wartość:', format="%.2f")

# Funkcja konwertująca
def convert(value, conversion_type):
    if conversion_type == 'Kilogramy na Funty':
        return value * 2.20462  # 1 kg to około 2.20462 funtów
    elif conversion_type == 'Kilometry na Mile':
        return value * 0.621371  # 1 km to około 0.621371 mili
    elif conversion_type == 'Stopnie Celsjusza na Stopnie Fahrenheita':
        return (value * 9/5) + 32  # Konwersja C na F
    elif conversion_type == 'Stopy na Metry':
        return value * 0.3048  # 1 stopa to około 0.3048 metra
    elif conversion_type == 'Cale na Centymetry':
        return value * 2.54  # 1 cal to około 2.54 centymetra

# Przycisk do wykonania konwersji
if st.button('Konwertuj'):
    result = convert(value, conversion_type)
    st.write(f'Wynik: {result:.2f}')
