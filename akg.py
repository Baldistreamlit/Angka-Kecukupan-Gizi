import streamlit as st

def hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin):
    # Hitung kebutuhan energi dasar (Basal Metabolic Rate/BMR) berdasarkan rumus Harris-Benedict
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi) - (5.677 * umur)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi) - (4.330 * umur)
    else:
        return "Jenis kelamin tidak valid"

    # Hitung Total Energy Expenditure (TEE) berdasarkan aktivitas fisik
    # Misalnya, menggunakan faktor aktivitas fisik sedentary (1.2)
    faktor_aktivitas = 1.2
    tee = bmr * faktor_aktivitas

    # Hitung kebutuhan energi total (Total Daily Energy Expenditure/TDEE) perhari
    tdee = tee

    return tdee

def main():
    st.title('Kalkulator Kecukupan Gizi')

    umur = st.number_input('Masukkan umur (tahun)', min_value=0, step=1)
    berat_badan = st.number_input('Masukkan berat badan (kg)', min_value=0.0, step=0.1)
    tinggi = st.number_input('Masukkan tinggi (cm)', min_value=0.0, step=0.1)
    jenis_kelamin = st.selectbox('Pilih jenis kelamin', ['Laki-laki', 'Perempuan'])

    # Informasi nama anggota kelompok dan tim
    st.sidebar.title('Informasi Tim')
    st.sidebar.write('Kelompok 4')
    st.sidebar.write('Anggota:')
    st.sidebar.write('- Amara Rifa Pratamy')
    st.sidebar.write('- Muhammad Baldiyansyah')
    st.sidebar.write('- Shofi Nabila Khoirunnisa')
    st.sidebar.write('- Tabitha Zoeana Salsabila')
    st.sidebar.write('- Afdatul Saputra')

    if st.button('Hitung'):
        kecukupan_gizi = hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin)
        st.write("Angka Kecukupan Gizi perhari:", kecukupan_gizi, "kcal")

if __name__ == "__main__":
    main()
