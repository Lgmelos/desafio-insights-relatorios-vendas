# Unificando os três dataframes
combined_df = pd.concat([aliexpress, etsy, shopee], ignore_index=True)

# Criando uma tabela de resumo de vendas por país
sales_by_country = combined_df.groupby("delivery_country").agg({
    "total_price": "sum",
    "quantity": "sum",
    "invoice_id": "count"
}).rename(columns={
    "total_price": "total_sales",
    "quantity": "total_units_sold",
    "invoice_id": "number_of_orders"
}).sort_values(by="total_sales", ascending=False)

sales_by_country.reset_index(inplace=True)
sales_by_country
