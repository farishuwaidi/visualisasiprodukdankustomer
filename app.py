import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk membaca data
def load_data():
    order_dataset = pd.read_csv("/content/orders_dataset.csv")
    customers_df = pd.read_csv("/content/customers_dataset.csv")
    return order_dataset, customers_df

def main():
    # Sidebar dengan logo perusahaan
    st.sidebar.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=200)
    st.sidebar.header("Perusahaan E-Commerce")

    # Memuat data
    order_dataset, customers_df = load_data()

    # Menu untuk memilih visualisasi
    visualization_option = st.sidebar.selectbox("Pilih Visualisasi", ["Pie Chart Distribusi Pelanggan", "Order Items"])

    if visualization_option == "Pie Chart Distribusi Pelanggan":
        # Ambil 10 negara dengan pelanggan terbanyak
        top_10_states = customers_df['customer_state'].value_counts().nlargest(10)

        # Ambil nama-nama negara pada 10 teratas
        top_10_names = top_10_states.index.tolist()

        # Hitung total pelanggan di 10 negara teratas
        top_10_total = top_10_states.sum()

        # Hitung jumlah pelanggan dari negara-negara lainnya
        other_total = len(customers_df) - top_10_total

        # Jumlah pelanggan negara-negara lain dimasukkan ke dalam kategori "Lainnya"
        other_states = customers_df[~customers_df['customer_state'].isin(top_10_names)]
        other_states_count = other_states['customer_state'].value_counts().sum()

        # Buat list jumlah pelanggan untuk 10 negara teratas dan kategori "Lainnya"
        top_states_counts = top_10_states.tolist()
        top_states_counts.append(other_states_count)

        # Buat list label untuk 10 negara teratas dan kategori "Lainnya"
        labels = top_10_names + ['Lainnya']

        # Membuat pie chart
        st.pyplot(plt.figure(figsize=(8, 8)))
        plt.pie(top_states_counts, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Top 10 States with Most Customers')
        st.pyplot()

    elif visualization_option == "Order Items":
        # Ambil 20 produk dengan pesanan terbanyak
        top_20_products = order_dataset['product_name'].value_counts().nlargest(20)

        # Membuat bar chart
        st.pyplot(plt.figure(figsize=(10, 6)))
        top_20_products.plot(kind='bar')
        plt.title('Produk yang Paling Sering Diorder')
        plt.xlabel('Nama Produk')
        plt.ylabel('Jumlah Pesanan')
        st.pyplot()

if __name__ == '__main__':
    main()