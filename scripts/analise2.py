from datetime import datetime

# Convertendo datas para datetime
combined_df['buyer_birth_date'] = pd.to_datetime(combined_df['buyer_birth_date'], errors='coerce')
combined_df['date'] = pd.to_datetime(combined_df['date'], errors='coerce')

# Calculando a idade do comprador no momento da compra
combined_df['buyer_age'] = combined_df.apply(
    lambda row: row['date'].year - row['buyer_birth_date'].year 
    if pd.notnull(row['date']) and pd.notnull(row['buyer_birth_date']) else None,
    axis=1
)

# Calculando a idade média por produto e país
average_age_by_product_country = combined_df.groupby(
    ['delivery_country', 'product_sold']
)['buyer_age'].mean().reset_index().rename(columns={'buyer_age': 'average_age'})

average_age_by_product_country.sort_values(by=['delivery_country', 'product_sold'], inplace=True)
average_age_by_product_country

