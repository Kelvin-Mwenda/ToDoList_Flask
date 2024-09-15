from flask import Blueprint, jsonify, render_template, request, url_for, redirect, request,flash
from flask_login import login_required, current_user
#from wtforms import Form, StringField, TextField,EmailField, PasswordField,DateField
from . import db
from .models import Event
import json
from datetime import datetime, date, timedelta


views = Blueprint('views',__name__)

@views.route('/',methods=['GET'])
@views.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        event = request.form.get('event')
        date_str = request.form.get('date')  # Change variable name to avoid conflict with built-in 'date'
        print(f"Received date: {date_str}")
        
        if len(event) < 2:
            flash('The event has to have at least two characters!', category='error')
        else:
            try:
                # Correctly parse the datetime if it includes a time part
                start_date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Keep it as a datetime object
                date_obj = start_date_obj.date()  # Get the date part as a date object
                print(f"Formatted Date: {date_obj}")
                
                new_event = Event(event=event, date=date_obj, user_id=current_user.id)
                db.session.add(new_event)
                db.session.commit()
                return render_template('home.html')
            except ValueError as e:
                # Log the error for debugging
                print(f"ValueError: {e}")
                flash('Invalid data format!', category='error')
                return f"ValueError: {e}", 400
    else:
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