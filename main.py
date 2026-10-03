import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        player = Player.objects.get_or_create(
            nickname=player_data["name"],
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=player_data["race"]),
            guild=Guild.objects.get(name=player_data["guild"]),
        )


if __name__ == "__main__":
    main()
