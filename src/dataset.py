import pandas as pd

data = {
    "Name": ["Sanpoorna", "Shri", "Poornima"],
    "Age": [15, 7, 41],
    "City": ["Heidelberg", "Schwetzingen", "Udupi"],
}
df = pd.DataFrame(data)
df = df.replace("Shri", "Shrigajanan")
