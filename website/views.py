from flask import Blueprint, jsonify, render_template, request, url_for, redirect, request,flash
from flask_login import login_required, current_user
from . import db
from .models import Event
import json
from datetime import datetime, date, timedelta


views = Blueprint('views',__name__)

@views.route('/',methods=['GET'])
@views.route('/index',methods=['GET'])
def index():
    return render_template('index.html')


@views.route('/home',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        data = request.get_json()
        event = data.get('event')
        date_task = data.get('date')
        print(f"Received date: {date}")
        
        if len(event) < 2:
            flash('The event has to have at least two characters!', category='error')
        else:
            try:
                # Correctly parse the datetime if it includes a time part
                date = date.strptime(date_task, '%Y-%m-%d').date()
                #date = datetime.fromisoformat(date_task,'%d-%m-%Y').date()
                new_event = Event(event=event, date=date, user_id=current_user.id)
                db.session.add(new_event)
                db.session.commit()
                flash('Event added successfully!', category='success')
            except ValueError as e:
                # Log the error for debugging
                print(f"ValueError: {e}")
                return {"error": "Invalid date format. Use YYYY-MM-DD."}, 400
                flash('Invalid date format!', category='error')
    
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