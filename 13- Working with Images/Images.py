from PIL import Image

# ---------------------------------------------------
# OPEN IMAGE AND INSPECT BASIC PROPERTIES
# ---------------------------------------------------

# Open the image file
pencils = Image.open("pencils.jpg")

# Print the type of the image object
print("Image type:", type(pencils))

# Display the image
pencils.show()

# Print image size (width, height)
print("Image size:", pencils.size)

# Print image filename
print("Image filename:", pencils.filename)

# Print image format description
print("Image format:", pencils.format_description)


# ---------------------------------------------------
# CROP A SMALL REGION FROM THE IMAGE
# ---------------------------------------------------
# Crop box format -> (left, upper, right, lower)
cropped = pencils.crop((121, 74, 242, 148))

# Paste the cropped region at the top-left corner (0, 0)
pencils.paste(im=cropped, box=(0, 0))

# Show the image after pasting
pencils.show()


# ---------------------------------------------------
# RESIZE THE IMAGE
# ---------------------------------------------------
# Resize returns a new image; the original image remains unchanged
resized_image = pencils.resize((1080, 1440))

# Show resized image
resized_image.show()

# Print resized image size
print("Resized image size:", resized_image.size)

# Show original image again
pencils.show()


# ---------------------------------------------------
# WORKING WITH TRANSPARENCY (ALPHA CHANNEL)
# ---------------------------------------------------

# Open red image and convert to RGBA for transparency support
red = Image.open("red.jpg").convert("RGBA")
red.show()

# Apply transparency (0 = fully transparent, 255 = fully opaque)
red.putalpha(10)
red.show()

# Open blue image and convert to RGBA
blue = Image.open("blue.png").convert("RGBA")
blue.show()

# Apply transparency to blue image
blue.putalpha(10)
blue.show()


# ---------------------------------------------------
# PASTE ONE IMAGE OVER ANOTHER USING MASK
# ---------------------------------------------------
# Paste red image over blue using red image as mask
blue.paste(im=red, box=(0, 0), mask=red)

# Show the blended image
blue.show()


# ---------------------------------------------------
# SAVE AND REOPEN IMAGE
# ---------------------------------------------------
# Save the final blended image
blue.save("black.png")

# Open and display the saved image
black = Image.open("black.png")
black.show()
