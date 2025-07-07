from datetime import datetime
from . import db

class Postcard(db.Model):
    __tablename__='postcards'
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100), nullable=False)
    recipient_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'sender_name': self.sender_name,
            'recipient_name': self.recipient_name,
            'message': self.message,
            'image_url': self.image_url,
            'sent_at': self.sent_at.isoformat()
        }