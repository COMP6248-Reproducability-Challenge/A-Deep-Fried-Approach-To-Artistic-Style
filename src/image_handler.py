"""
Image helper functions.

Author: Joseph Early (je5g15@soton.ac.uk)
Created: 17/05/19
"""

import matplotlib.pyplot as plt
import torchvision
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms

# Consistent transform to scale image to 256 x 256
transform_256 = transforms.Compose([
                    transforms.Resize((256, 256)),
                    transforms.ToTensor()
                ])


def load_image_as_tensor(image_path, transform=transform_256):
    """
    Load a single image as a tensor from the given path. Applies a transformation if one is given.
    """
    image = Image.open(image_path)
    image = transform(image).float()
    image = Variable(image, requires_grad=False)
    image = image.unsqueeze(0)
    return image


def save_tensor_as_image(tensor, image_path):
    """
    Save a single 3D tensor to the given image path
    """
    torchvision.utils.save_image(tensor, image_path)


def plot_image_tensor(image_tensor):
    """
    Plot a single image using matplotlib.
    """
    plt.figure()
    plt.imshow(image_tensor[0].permute(1, 2, 0))
    plt.show()
