import os
from PIL import Image

print("Select an operation.")
print("1.Want an Image size to compress\n2.Want to compress a directory of Images")

while True:
  try:
    operation= int(input("Enter choice(1/2): "))
    if operation ==1 or operation ==2:
      break
    else:
      print("Please Enter 1 or 2.")
  except:
    print("Invalid choice.")
2
if operation ==1:
  image = input("Enter the path of the image: ")
  if image.lower().endswith(('.png','.jpg','jpeg')):
    picture = Image.open(image)
    picture.save(f"compressed_{image}", optimize=True, quality=10)
    print("Image has been compressed successfully! ")

  else:
    print("Please enter a valid Image.")

if operation ==2:
  input_directory = input("Enter the path of the directory: ")
  output_directory = input_directory
  for filename in os.listdir(input_directory):
    input_path = os.path.join(input_directory, filename)
    if filename.lower().endswith(('.png','.jpg','jpeg')):
      output_path = os.path.join(output_directory, f"compressed_{filename}")
      img = Image.open(input_path)
      img.save(output_path, optimize=True, quality=10)
      print(f"{filename} has been compressed successfully!")

    else:
      print("This Directory does not contain Images.")
      
      
