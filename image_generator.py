from Match import Match
from PIL import Image, ImageDraw, ImageFilter
import os

numbers_mapping = {'0': 'cero', '1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco', '6': 'seis', '7': 'siete', '8': 'ocho', '9': 'nueve'}

def create_photo(match):
    home_team_image_path = os.path.join('badges/', match.home_team + '.png')
    away_team_image_path = os.path.join('badges/', match.away_team + '.png')
    background_image_path = 'test_images/Background.jpg'

    home_team_result_image_path = os.path.join('numbers/', numbers_mapping[str(match.home_team_score)] + '.png')
    away_team_result_image_path = os.path.join('numbers/', numbers_mapping[str(match.away_team_score)] + '.png')

    
    background_image = Image.open(background_image_path)
    home_team_badge = Image.open(home_team_image_path).convert("RGBA")
    away_team_badge = Image.open(away_team_image_path).convert("RGBA")
    home_team_result = Image.open(home_team_result_image_path).convert("RGBA")
    away_team_result = Image.open(away_team_result_image_path).convert("RGBA")

    home_team_badge = home_team_badge.resize((130, 130))
    away_team_badge = away_team_badge.resize((130, 130))
    home_team_result = home_team_result.resize((100, 100))
    away_team_result = away_team_result.resize((100, 100))

    background_image.paste(home_team_badge, (50, 100), home_team_badge)
    background_image.paste(away_team_badge, (450, 100), away_team_badge)
    background_image.paste(home_team_result, (190,110), home_team_result)
    background_image.paste(away_team_result, (350,110), away_team_result)
    background_image = background_image.resize((500, 500))

    photo_folder_name = 'photos'
    if not os.path.isdir(photo_folder_name):
        os.mkdir(photo_folder_name)

    photo_path = os.path.join(photo_folder_name, match.home_team + ' vs ' + match.away_team + '.jpg')
    background_image.save(photo_path)
    
    return '/' + photo_path