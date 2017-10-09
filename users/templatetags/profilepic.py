from django import template

register = template.Library()

# asks for a user object and returns appropriate img.
@register.simple_tag
def get_profile_pic(user):

    # get the image
    images = user.profilepicture_set.all().order_by('-id')
    if images.exists():
        user.image = images[0].imagefile.url
    else:
        user.image = 'images/default.jpeg'

    return user.image