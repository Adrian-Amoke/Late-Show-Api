from server.app import app
from server.config import db

with app.app_context():
    from server.models.user import User
    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.appearance import Appearance
    from datetime import date

    # Clear existing data
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()

    # Create users
    user1 = User(username='late_admin')
    user1.set_password('adminlate')

    user2 = User(username='Show_user')
    user2.set_password('usershow')

    db.session.add_all([user1, user2])

    # Create guests
    guest1 = Guest(name='Steven Strange', occupation='Magician')
    guest2 = Guest(name='Tony Stark', occupation='Comedian')

    db.session.add_all([guest1, guest2])

    # Create episodes
    episode1 = Episode(date=date(2024, 1, 1), number=1)
    episode2 = Episode(date=date(2024, 1, 8), number=2)

    db.session.add_all([episode1, episode2])

    # Create appearances
    appearance1 = Appearance(rating=4, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=5, guest=guest2, episode=episode2)

    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print("Seeded data successfully.")
