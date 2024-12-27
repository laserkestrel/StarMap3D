import csv

# Input your CSV file path here
csv_file_path = r"C:\Users\Andy\Documents\Unreal Projects\Starmap3D\hygdata_v40.csv.full"

# Default Unreal type mapping
def infer_unreal_type(value):
    try:
        float(value)  # Can it be a float?
        return "Float"
    except ValueError:
        try:
            int(value)  # Can it be an integer?
            return "Integer"
        except ValueError:
            if value == "":
                return "String"  # Empty fields default to String
            return "String"

# Read CSV header and example row
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # First line is the header
    example_row = next(reader)  # Second line is the example row

# Generate struct fields based on example row
print("Blueprint Struct Fields:\n")
for header, example_value in zip(headers, example_row):
    unreal_type = infer_unreal_type(example_value.strip())
    print(f"UPROPERTY(EditAnywhere, BlueprintReadWrite)")
    print(f"{unreal_type} {header};\n")
