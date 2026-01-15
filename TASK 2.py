import pandas as pd
try:
    file_path = input("Enter CSV file path: ")
    df = pd.read_csv(file_path)
    print("\nDataset loaded successfully.\n")
except Exception as e:
    print("Error loading file:", e)
    exit()
print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())
df.drop_duplicates(inplace=True)

numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values cleaned.")

if len(numeric_cols) > 0:
    col = numeric_cols[0]
    filtered_df = df[df[col] > df[col].mean()]
    print(f"\nFiltered data where {col} > average:")
    print(filtered_df.head())


if len(categorical_cols) > 0 and len(numeric_cols) > 0:
    group_col = categorical_cols[0]
    value_col = numeric_cols[0]

    grouped_data = df.groupby(group_col)[value_col].agg(
        count='count',
        average='mean',
        maximum='max',
        minimum='min'
    )

    print("\nGrouped Summary Statistics:")
    print(grouped_data)

print("\n📌 KEY INSIGHTS:")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

if len(numeric_cols) > 0:
    print("\nNumerical Data Summary:")
    print(df[numeric_cols].describe())

print("\nData analysis completed successfully.")
