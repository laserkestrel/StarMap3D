import unreal

# Define the struct name
struct_name = "StarStruct"

# Define the fields and their types
fields = [
    {"name": "id", "type": unreal.IntProperty},
    {"name": "hip", "type": unreal.IntProperty},
    {"name": "hd", "type": unreal.StrProperty},
    {"name": "ra", "type": unreal.FloatProperty},
    {"name": "dec", "type": unreal.FloatProperty},
    {"name": "x", "type": unreal.FloatProperty},
    {"name": "y", "type": unreal.FloatProperty},
    {"name": "z", "type": unreal.FloatProperty},
    {"name": "mag", "type": unreal.FloatProperty},
]

# Get the asset tools to create assets
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create the struct asset in the /Game directory
struct_package_path = "/Game"  # You can change this to your desired location
struct_asset = asset_tools.create_asset(
    asset_name=struct_name,
    package_path=struct_package_path,
    asset_class=unreal.UserDefinedStruct,
    factory=unreal.UserDefinedStructFactory()
)

# If the struct asset was created successfully, add the fields
if struct_asset:
    for field in fields:
        # Create the field and add it to the struct
        new_property = unreal.UserDefinedStructEditorLibrary.add_variable_to_struct(
            struct_asset,
            field["name"],
            field["type"]()
        )
    
    # Save the struct asset
    unreal.EditorAssetLibrary.save_loaded_asset(struct_asset)
    print(f"Struct '{struct_name}' created successfully with fields!")
else:
    print("Failed to create struct asset.")
