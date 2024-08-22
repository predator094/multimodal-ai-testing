from unstructured.partition.pdf import partition_pdf

fname = r"C:\Users\preda\vs_files\testing\MachineLearningTechniques-7-29-cropped.pdf"

elements = partition_pdf(
    filename=fname,
    infer_table_structure=True,
    strategy="hi_res",
    extract_images_in_pdf=True,
    extract_image_block_output_dir="./imagess",
    extract_image_block_types=["Image", "Table"],
    extract_image_block_crop_horizontal=20,
    extract_image_block_crop_vertical=20,
)

tables = [el for el in elements if el.category == "Table"]

print(tables[0].text)
print(tables[0].metadata.text_as_html)
