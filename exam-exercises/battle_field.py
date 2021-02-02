
class Battlefield:
    @staticmethod
    def fight(attacker: 'Player', enemy: 'Player'):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker_bonus_health = sum([card.health_points for card in attacker.card_repository.cards])
        attacker.health += attacker_bonus_health

        enemy_bonus_health = sum([card.health_points for card in enemy.card_repository.cards])
        enemy.health += enemy_bonus_health

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)



