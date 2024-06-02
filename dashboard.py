import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')


def product_category_counts(order_items_products_df):
    product_category_counts = order_items_products_df.groupby(
        by="product_category_name").order_id.nunique().sort_values()

    return product_category_counts


def product_category_prices(order_items_products_df):
    product_category_prices = order_items_products_df.groupby(
        by="product_category_name").price.sum().sort_values(ascending=False)

    return product_category_prices


def status_users_counts(active_customers_df, non_active_customers_df):
    active_customer_states = active_customers_df.groupby(
        by="customer_state").status.count().sort_values(ascending=False).head(10)
    non_active_customer_states = non_active_customers_df.groupby(
        by="customer_state").status.count().sort_values(ascending=False).head(10)

    return active_customer_states, non_active_customer_states


active_users_df = pd.read_csv("./data/active_customers.csv")
non_active_users_df = pd.read_csv("./data/non_active_customers.csv")
order_items_products_df = pd.read_csv("./data/order_items_products.csv")
customers_df = pd.read_csv("./data/customers_dataset.csv")
product_category_count = product_category_counts(order_items_products_df)
product_category_price = product_category_prices(order_items_products_df)
active_customer_states, non_active_customer_states = status_users_counts(
    active_users_df, non_active_users_df)


with st.sidebar:
    st.markdown(
        "<div style='display: flex; justify-content: center;'>"
        "<img src='https://media.licdn.com/dms/image/D5603AQHAAnWzc38Pow/profile-displayphoto-shrink_800_800/0/1698143495181?e=1715212800&v=beta&t=4fZaqhh0cTra3n-RszM8rjGBErTsFEhO3hhqWpg1w9A' "
        "width='200' style='border-radius: 50%;'>"
        "</div>",
        unsafe_allow_html=True
    )
    st.write(
        """
    # Wardiansyah Fauzi Abdillah
    Computer Science | Gunadarma University
    """
    )

st.header('E-commerce Data Analysis Dashboard')

with st.container():
    st.subheader('Category Analysis by Order')
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    axes[0].bar(product_category_count.tail(10).index[::-1],
                product_category_count.tail(10).values[::-1], color='skyblue')
    axes[0].set_title('Top 10 Most Ordered Product Categories')
    axes[0].set_xlabel('Product Category')
    axes[0].set_ylabel('Number of Orders')
    axes[0].tick_params(axis='x', rotation=45)
    axes[1].bar(product_category_count.head(10).index,
                product_category_count.head(10).values, color='lightcoral')
    axes[1].set_title('Top 10 Least Ordered Product Categories')
    axes[1].set_xlabel('Product Category')
    axes[1].set_ylabel('Number of Orders')
    axes[1].tick_params(axis='x', rotation=45)

    # Menampilkan visualisasi menggunakan st.pyplot()
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write(
            """
            Terlihat bahwa pada Top 10 kategori produk yang paling sering di order, 
            cama_mesa_banho menjadi kategori produk yang paling banyak dibeli.
            Sedangkan untuk Top 10 Kategori produk yang paling jarang di order,
            seguros_e_servicos menduduki nomor 1 produk yang paling jarang di order.
            """
        )

with st.container():

    st.subheader('Top 10 Product Categories by Total Price')

    # Membuat plot menggunakan matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    product_category_price.head(10).plot(kind='bar', color='lightgreen', ax=ax)

    # Menambahkan judul dan label sumbu
    ax.set_title('Top 10 Product Categories by Total Price')
    ax.set_xlabel('Product Category')
    ax.set_ylabel('Total Price')

    # Menampilkan visualisasi menggunakan st.pyplot()
    st.pyplot(fig)

    with st.expander("See explanation"):
        st.write(
            """
                Pada visualisasi diatas kita mendapatkan data Top 10 penyumbang revenue terbesar, 
                didapatkan beleza_saude sebagai kategori produk dengan penyumbang revenue terbesar
            """
        )

with st.container():
    st.subheader('Top 10 States with Active and Non-Active Customers')

    # Membuat plot menggunakan matplotlib
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Plot untuk active customers
    axes[0].bar(active_customer_states.index,
                active_customer_states.values, color='lightblue')
    axes[0].set_title('Top 10 States with Active Customers')
    axes[0].set_xlabel('Customer State')
    axes[0].set_ylabel('Number of Active Customers')
    axes[0].tick_params(axis='x', rotation=45)

    # Plot untuk non-active customers
    axes[1].bar(non_active_customer_states.index,
                non_active_customer_states.values, color='lightcoral')
    axes[1].set_title('Top 10 States with Non-Active Customers')
    axes[1].set_xlabel('Customer State')
    axes[1].set_ylabel('Number of Non-Active Customers')
    axes[1].tick_params(axis='x', rotation=45)

    # Menampilkan visualisasi menggunakan st.pyplot()
    st.pyplot(fig)
    with st.expander("See explanation"):
        st.write(
            """
            Dari visualisasi diatas dikategorikan menjadi Top 10 Most Active Users dan Top 10 Most Non Active Users,
            didapati bahwa kode state SP menjadi yang terbesar baik Active maupun Non Active usersnya
            """
        )

with st.container():
    st.header('Conclusion')
    st.subheader("**Kategori barang apa yang paling banyak diminati/dibeli dan paling sedikit diminati/dibeli?**")
    st.write("Berdasarkan analisa data dari dataset product dan order_items, dapat disimpulkan bahwa:")
    st.write("  - Kategori barang yang paling banyak diminati/dibeli adalah cama_mesa_banho.")
    st.write("  - Kategori dengan peminat paling sedikit adalah seguros_e_servicos.")
    st.write(" ")

    st.subheader("**Kategori barang mana yang menyumbang revenue paling banyak terhadap perusahaan?**")
    st.write("Berdasarkan analisis terhadap data product dan order_items, dapat disimpulkan bahwa:")
    st.write("  - Kategori produk yang menyumbang revenue paling banyak ke perusahaan adalah beleza_saude.")
    st.write(" ")

    st.subheader("**State mana yang memiliki customer active paling banyak?**")
    st.write("Berdasarkan analisa terhadap dataset customer dan order, dapat disimpulkan bahwa:")
    st.write("  - State dengan customer Active terbanyak adalah SP. SP juga menjadi state dengan customer Non Active paling banyak.")
    st.write(" ")

st.caption('Created by Wardiansyah Fauzi Abdillah, 2024')