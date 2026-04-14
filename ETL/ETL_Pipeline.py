from Extract_MH_4W import run_extract
from Transform import batch_transform
from load import run_load   # your load file

def run_pipeline():
    print("🚀 Starting ETL Pipeline...\n")

    # STEP 1: Extract
    print("📥 Running Extract...")
    run_extract()

    # STEP 2: Transform
    print("\n🔄 Running Transform...")
    batch_transform(
        input_folder=r"C:\Users\sujal\Documents\Major Project\Project on System\Data",
        output_file="consolidated_fuel_data.csv"
    )

    # STEP 3: Load
    print("\n📤 Running Load...")
    run_load("consolidated_fuel_data.csv")

    print("\n✅ Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()