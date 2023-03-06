import pandas as pd
print(f"""
         .___      ________  ________  ______  
       __| _/______\_____  \/   __   \/  __  \ 
      / __ |\_  __ \/  ____/\____    />      < 
     / /_/ | |  | \/       \   /    //   --   \\
     \____ | |__|  \_______ \ /____/ \______  /
          \/               \/               \/ 
== good or bad? it depends on your point of view! ==
Follow this step to login to your truecaller account :
1. On Truecaller Android, tap on the 3 line menu on top left then click on setting's.
2. Tap on Privacy Center and then click on Download my data.
3. Now a JSON file is downloaded.
4. Save the JSON file at this tools file location
5. Rename the JSON file to truecaller.json
""")
# Mengatur nama file input dan output
input_file = "file.csv"
output_prefix = "file-"

# Membaca file CSV
df = pd.read_csv(input_file)

# Menghitung jumlah baris data
total_rows = df.shape[0]

# Menghitung jumlah baris per file output
rows_per_file = int(total_rows / 6) + 1

# Memecah data menjadi 6 file terpisah
for i in range(6):
    start_row = i * rows_per_file
    end_row = min((i + 1) * rows_per_file, total_rows)
    output_file = f"{output_prefix}{i+1}.csv"
    df[start_row:end_row].to_csv(output_file, index=False)
    print(f"File {output_file} created with {end_row - start_row} rows")
