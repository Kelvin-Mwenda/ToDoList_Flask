from flask import Blueprint, jsonify, render_template, request, url_for, redirect, request,flash
from flask_login import login_required, current_user
from . import db
from .models import Event
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['GET'])
@views.route('/index',methods=['GET'])
def index():
    return render_template('index.html')


@views.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        event = request.form.get('event')
        if len(event) < 2:
            flash('The event has to have at least two characters!',category='error')
        else:
            new_event = Event(data=event, user_id=current_user.id)
            db.session.add(new_event)
            db.session.commit()
            flash('Event added successfully!',category='success')
            
    return render_template('home.html')

@views.route('/delete-event',methods=['POST'])
def delete_event():
    event = json.loads(request.data)
    eventId = event['eventId']
    event = Event.query.get(eventId)
    
    if event and event.user_id == current_user.id:
        db.session.delete(event)
        db.session.commit()
        
    return jsonify({})