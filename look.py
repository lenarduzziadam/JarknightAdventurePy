class Room:
    def __init__(self, description, items=None, characters=None, exits=None):
        self.description = description
        self.items = items if items else []
        self.characters = characters if characters else []
        self.exits = exits if exits else {}


class Look:
    def __init__(self, room):
        self.room = room

    def describe(self):
        print(self.room.description)

        if self.room.items:
            print("You see the following items:")
            for item in self.room.items:
                print(f"- {item}")
        else:
            print("There are no items here.")

        if self.room.characters:
            print("You see the following characters:")
            for character in self.room.characters:
                print(f"- {character}")
        else:
            print("There are no characters here.")

        if self.room.exits:
            print("Exits available:")
            for direction, destination in self.room.exits.items():
                print(f"- {direction.title()} leads to {destination}")
        else:
            print("There are no exits from this room.")


def create_default_world():
    """Builds a tiny layout of rooms the player can explore."""
    village = Room(
        description="You are standing outside a humble village. Smoke curls from cottages to the north.",
        items=["Warm Lantern", "Notice Board"],
        characters=["Traveling Merchant"],
        exits={"north": "marketplace", "east": "forest_path"},
    )

    marketplace = Room(
        description="The marketplace bustles with shoppers. Stalls line every street.",
        items=["Shiny Dagger", "Fresh Bread"],
        characters=["Town Guard"],
        exits={"south": "village", "up": "wizard_tower"},
    )

    forest_path = Room(
        description="A mossy path winds between twisted oaks. The air hums with distant insects.",
        items=["Ancient Coin"],
        characters=[],
        exits={"west": "village"},
    )

    wizard_tower = Room(
        description="You enter the tower foyer. Arcane glyphs glow faintly.",
        items=["Cracked Crystal", "Spell Scroll"],
        characters=["Hermit Wizard"],
        exits={"down": "marketplace"},
    )

    return {
        "village": village,
        "marketplace": marketplace,
        "forest_path": forest_path,
        "wizard_tower": wizard_tower,
    }