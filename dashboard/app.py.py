
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk membaca data
def load_data():
    order_dataset = pd.read_csv("/content/orders_dataset.csv")
    customers_df = pd.read_csv("/content/customers_dataset.csv")
    return order_dataset, customers_df

def load_order_items_data():
    order_items = pd.read_csv("/content/order_items_dataset.csv")
    product_dataset = pd.read_csv("/content/products_dataset.csv")
    return order_items, product_dataset

# Membaca data
order_dataset, customers_df = load_data()

order_dataset['order_purchase_timestamp'] = pd.to_datetime(order_dataset['order_purchase_timestamp'])

def plot_histogram(data, column, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data[column], bins=30, edgecolor='black')
    ax.set_xlabel(column)
    ax.set_ylabel('Frekuensi')
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

def plot_bar_chart(data, column, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    data[column].value_counts().plot(kind='bar', edgecolor='black', ax=ax)
    ax.set_xlabel(column)
    ax.set_ylabel('Frekuensi')
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

def plot_order_items(order_items, product_dataset):
    fig, ax = plt.subplots(figsize=(20, 10))

    # Visualisasi histogram produk yang paling sering diorder
    merged_data = pd.merge(order_items, product_dataset, on='product_id')
    product_order_count = merged_data['product_category_name'].value_counts()
    product_order_count.plot(kind='bar', ax=ax)
    ax.set_title('Histogram Produk yang Paling Sering Diorder', fontsize=20)
    ax.set_xlabel('Nama Produk', fontsize=15)
    ax.set_ylabel('Jumlah Pesanan', fontsize=15)
    ax.tick_params(axis='x', rotation=45)

    st.pyplot(fig)

def main():
    # Sidebar dengan logo perusahaan
    st.sidebar.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=200)
    st.sidebar.header("Perusahaan E-Commerce")

    # Menu untuk memilih visualisasi
    visualization_option = st.sidebar.selectbox("Pilih Visualisasi", ["Histogram Waktu Pembelian", "Bar Chart Distribusi Pelanggan", "Order Items"])

    # Menampilkan visualisasi berdasarkan pilihan
    if visualization_option == "Histogram Waktu Pembelian":
        st.title("Histogram Waktu Pembelian Pesanan")
        plot_histogram(order_dataset, 'order_purchase_timestamp', 'Distribusi Waktu Pembelian Pesanan')

    elif visualization_option == "Bar Chart Distribusi Pelanggan":
        st.title("Distribusi Pelanggan Berdasarkan Negara Bagian")
        plot_bar_chart(customers_df, 'customer_state', 'Distribusi Pelanggan Berdasarkan Negara Bagian')

    elif visualization_option == "Order Items":
        order_items, product_dataset = load_order_items_data()
        plot_order_items(order_items, product_dataset)

if __name__ == '__main__':
    main()